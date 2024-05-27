- Create a new *Function App* (Resource Group: *rg-course-[init]-functionapp)
  - Choose **App Service** and **Select**
  - Create new *Resource Group*
  - Choose unique name (Note the name for later use)
    - Runtime Stack: .NET
    - Version: 8 (LTS) isolated..
    - Region: Appropriate region
    - Operation System: Windows
  - Leave the rest *as is* and select **Review + create** and **Create**

- After creation goto the newly created *Resource Group* and examine the *Azure resources* created
  - Function App
  - Application Insight 
  - System *Storage Account*
  - App Service Plan (S1)

- In the *Overview* Page, verify that no *Functions* are currently deployed

- Create a new *Function App C# Project* with a single *HTTP Trigger*

```powershell

func init integrationit-functions --worker-runtime dotnetIsolated

cd .\integrationit-functions\

func new -n Myhttptrigger -t HttpTrigger

```

- run the function app locally

```powershell

func start

```

- Notice the *HTTP Trigger's* local endpoint

```powershell

Myhttptrigger: [GET,POST] http://localhost:7071/api/Myhttptrigger

```

- In another session call the endpoint

```powershell

curl http://localhost:7071/api/Myhttptrigger

```

- Verify that the call works

- Stop the Function App running locally **CTRL+C**
- deploy the code to your *Function App* provisioned before in *Azure* (Azure CLI (az) needs to be logged in and pointing at the correct *Azure Subscription*)

- Run this command replace [functionappName] with your function app name (no square brackets)
```powershell

dotnet clean;

func azure functionapp publish [functionappName]

### Once deployed get the HTTP Trigger endpoint with Function key

func azure functionapp list-functions [functionappName] --show-keys

```
- Get the URL (with the code query string) and call it.
- In the Portal in your *Function App* in *Overview* refresh and verify that there now is a *Function* 



- Create a *Storage Queue Trigger*
  - Create a new *Storage Account* inside your Function App *Resource Group*
