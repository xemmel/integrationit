- Create a *Web App/App Service* in the same process create new *Resource Group* (**rg-student-*your intitals*-webapp**)
  - Needs a unique name
  - Choose *Code*  *.NET 8 (LTS)* 
  - Choose region 
  - Choose Linux for *Operation System*
  - Under **Pricing Plans** -> **Pricing Plan** leave it as **Premium V3 P0V3**
  - **Review + create ** -> **Create**

- Make a note of your *Resource Group* and the name or the *Web App*

- Back in your *Web App* go to the *Overview* page (it might take a minute or so to load the first time)
  - Click on **Default domain** and verify that your web app is up and running


- Create a C# Web Api
  - In your root folder execute the following *dotnet command*

```powershell

dotnet new webapi -controllers -o integrationit.test.api

cd .\integrationit.test.api\

dotnet run

### Not the http://localhost:.... address

``` 

- In another powershell session run the following (replace xxxx with port)

```powershell

curl http://localhost:xxxx/weatherforecast

```

- Verify that the default *weatherforecast* api is working

- exit the running web api (CTRL+C)

- open *visual studio code* inside the folder *integrationit.test.api*

```powershell

code .

```

- Under the *Controllers* folder create a new Controller file *VersionController.cs*

- Paste the following C# code into the file and save it

```csharp

using Microsoft.AspNetCore.Mvc;

namespace integrationit.test.api.Controllers;

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


```

- run the web api again (dotnet run) and verify that the new *VersionController* is working

```powershell

curl http://localhost:xxxx/version

### Should return "1.0"

```

- Now deploy the local C# project web api to the *Azure Web App* created previously
  - Verify that your are logged into *Azure CLI* and pointing at the correct *Azure Subscription*

```powershell

az account show

### If you need to change subscription (remove square brackets, replace with correct Subscription Id)

az account set -s [subscriptionId]

```


- Inside the web api folder execute the following code (insert the correct *Resource Group Name* and *Web App Name*)

```powershell

$rgName = "rg-replace";
$webAppName = "replace";

Write-Host("Removing existing published files");

if (Test-Path .\publish\) {
    Get-Item .\publish\ | Remove-Item -Recurse -Force
}

if (Test-Path .\publish.zip) {
    Get-Item .\publish.zip | Remove-Item -Recurse -Force
}


Write-Host("Build/Publish .NET code");

dotnet publish -c Release -o ./publish

Write-Host("Zip..");

cd .\publish
Compress-Archive -Force -Path * -DestinationPath ..\publish.zip
cd ..

 az webapp deploy `
        --resource-group $rgName `
        --name $webAppName `
        --src-path ./publish.zip
;

```

- After successful deployment, verify that the deployed worked by calling (replace *webappname*)

```powershell

curl https://webappname.azurewebsites.net/version

```

- **Now change version number from *1.0* to *1.1* (remember to save VersionController)
  - Run the deployment script again
  - Once deployed call the *version endpoint* again. Notice that there might be some downtime before the new deployed version comes into effect

  


