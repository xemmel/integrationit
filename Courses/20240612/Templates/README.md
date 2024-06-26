### Create Resource Group and deploy bicep (functionapp) with Azure CLI

```powershell

### Place in Courses\20240612 folder

$appName = "dktvmlc";
$env = "test";
$location = "northeurope";
$vaultIdentity = "....";


### Create Resource Group
az group create --name "rg-${appName}-${env}" --location $location;

az deployment group create `
    --resource-group "rg-${appName}-${env}" `
    --template-file .\Templates\serviceProvider.bicep `
    --parameters appName=$appName `
    --parameters env=$env `
    --parameters vaultIdentity=$vaultIdentity
;


```

### Deploy function app code

```powershell

### In code/functionapp1 folder

func azure functionapp publish "func-${appName}-${env}"


func azure functionapp list-functions "func-${appName}-${env}" --show-keys

```

### Remove Resource Group

```powershell

az group delete --name "rg-${appName}-${env}" --yes --no-wait

```


#### Add your own local.settings

local.settings.json

```json

{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "dotnet"
    }
}

```

### Event Grid

```

Create new Event Grid Topic

  - Endpoint url (overview)

Postman   

 POST -> url  -> 401
Header: aeg-sas-key : key

body -> raw -> Json

[
    {
        "id" : "12345",
        "subject" : "c:\\temp\\1234.txt",
        "eventType" : "fileCreated",
        "eventTime" : "2024-06-26",
        "data" : {
            "customer" : "stofa"
        }
    }
]  -> 200 ok
-------------------

create requestbin.com (public bin)

Get the url 

Create new subscription in the Topic 

WebHook paste address (manuel reg.)





```