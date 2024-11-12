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
  --admin-enabled `
  --location $location
;

$acr = $acrJson | ConvertFrom-Json


### Create new web api project

dotnet new sln -o "${yourInit}webapi"

cd "${yourInit}webapi"

dotnet new webapi --use-controllers -o "${yourInit}webapi"

dotnet sln add "${yourInit}webapi"

```

- Open the solution in *Visual Studio Code*
- Inside the webapi project (Not on solution level) add a *.dockerignore* file with the following content
```
bin
obj
publish
publish.zip

```

- Inside the webapi project (Not on solution level) add a *Dockerfile* file with the following content
  - Remember to replace *nameofproject* with **[yourInitials]webapi**  (example: *mlcwebapi*)

  ```

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
ENTRYPOINT ["dotnet", "nameofproject.dll"]

```



- Now run the following command (inside the webapi folder) to build a *container image* and push it to your *ACR* (**Azure Container Registry**) 
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

curl "https://${yourInit}intitwebapi.azurewebsites.net/weatherforecast"


#### Cleanup

az group delete --name $rgName --yes --no-wait

##### Fails when done

az resource list --resource-group $rgName --output table
