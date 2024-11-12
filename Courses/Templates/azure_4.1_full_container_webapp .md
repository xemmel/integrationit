- Create a new *Container Registry*

```powershell

$yourInit = Read-Host("Your initials");

$rgName = "rg-student-${yourInit}-webappcontainer";
$location = "germanywestcentral";
$acrName = "acr${yourInit}intit";



az group create --name $rgName --location $location

$acrJson = az acr create `
  --name $acrName `
  --resource-group $rgName `
  --sku Standard `
  --location $location
;

$acr = $acrJson | ConvertFrom-Json


### Create new web api project

dotnet new sln -o "${yourInit}webapi"

cd "${yourInit}webapi"

dotnet new webapi --use-controllers -o "${yourInit}webapi"

dotnet sln add "${yourInit}webapi"

cd "${yourInit}webapi"


#### Create Version Controller

$versionControllerContent = @"

using Microsoft.AspNetCore.Mvc;

namespace ${yourInit}webapi.Controllers;

[ApiController]
[Route("[controller]")]
public class VersionController : ControllerBase
{

    private readonly ILogger<VersionController> _logger;

    public VersionController(ILogger<VersionController> logger)
    {
        _logger = logger;
    }

    [HttpGet(Name = "GetVersion")]
    public string Get()
    {
        return "1.0";
    }
}
"@

echo $versionControllerContent >> .\Controllers\VersionController.cs

### Create .dockerignore and Dockerfile

$dockerIgnoreContent = @"
bin
obj
publish
publish.zip
"@

echo $dockerIgnoreContent >> .dockerignore

$dockerFileContent = @"
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /source

# copy csproj and restore as distinct layers
COPY *.csproj .
RUN dotnet restore

# copy everything else and build app
COPY . .
WORKDIR /source
RUN dotnet publish -c release -o /app --no-restore

# final stage/image
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
ENV ASPNETCORE_HTTP_PORTS=80
COPY --from=build /app ./
ENTRYPOINT ["dotnet", "${yourInit}webapi.dll"]
"@

echo $dockerFileContent >> Dockerfile

```




- Now run the following command to build a *container image* and push it to your *ACR* (**Azure Container Registry**) 
  - Note: You do **not** need Docker etc. locally to do this, since we are using *ACR* to build the image. Make sure you are logged in in *Azure CLI* and that it is pointing at the correct *Azure Subscription*



```powershell

az acr build -t mytestapi:1.0 . -r $acrName

```

- Verify that the *Repository* was packaged and pushed to your *Azure Container Registry* by either:
  - Go to the portal and open your **ACR**
    - Look under *Services/Repositories*
  - Run this *Azure CLI* command

```powershell

az acr repository list --name $acrName

az acr repository show-tags --name $acrName --repository mytestapi

 
```

### Create a web app

```powershell

$aspJson = az appservice plan create `
  --name "${yourInit}intitwebapi" `
  --resource-group $rgName `
  --location $location `
  --is-linux `
  --sku P0V3
;


$asp = $aspJson | ConvertFrom-Json

$webAppJson = az webapp create `
  --resource-group $rgName `
  --name "${yourInit}intitwebapi" `
  --plan $asp.Id `
  --container-image-name "${acrName}.azurecr.io/mytestapi:1.0" `
  --acr-identity [system] `
  --acr-use-identity `
  --assign-identity [system]
;

$webApp = $webAppJson | ConvertFrom-Json

### Create AcrPull role on ACR for webapp

az role assignment create `
    --role AcrPull `
    --scope $acr.Id `
    --assignee $webApp.identity.principalId
;


### You may need to restart the webapp

az webapp restart --ids $webapp.id


### Test the api

curl "https://${yourInit}intitwebapi.azurewebsites.net/version"


### Change version

```powershell

#### Replace 1.0 with 1.1

(Get-Content -Path 'Controllers/VersionController.cs') -replace '1.0', '1.1' | Set-Content -Path 'Controllers/VersionController.cs'



#### Build and push a new container image to ACR with version 1.1
az acr build -t mytestapi:1.1 . -r $acrName

#### Change the webapp container from 1.0 to 1.1

az webapp config container set `
   --container-image-name "${acrName}.azurecr.io/mytestapi:1.1" `
   --name "${yourInit}intitwebapi" `
   --resource-group $rgName


#### Replace x with y

$from = Read-Host("from");
$to = Read-Host("to");


(Get-Content -Path 'Controllers/VersionController.cs') -replace $from, $to | Set-Content -Path 'Controllers/VersionController.cs'

#### Build and push a new container image to ACR with version (to)
az acr build -t mytestapi:$to . -r $acrName

#### Change the webapp container from (from) to (to)

az webapp config container set `
   --container-image-name "${acrName}.azurecr.io/mytestapi:$to" `
   --name "${yourInit}intitwebapi" `
   --resource-group $rgName

az webapp restart --ids $webapp.id

```

#### Cleanup

az group delete --name $rgName --yes --no-wait

##### Fails when done

az resource list --resource-group $rgName --output table
