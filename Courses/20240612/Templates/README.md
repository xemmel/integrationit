### Create Resource Group and deploy bicep (functionapp) with Azure CLI

```powershell

### Place in Courses\20240612 folder

$appName = "dktvmlc";
$env = "test";
$location = "northeurope";


### Create Resource Group
az group create --name "rg-${appName}-${env}" --location $location;

az deployment group create `
    --resource-group "rg-${appName}-${env}" `
    --template-file .\Templates\serviceProvider.bicep `
    --parameters appName=$appName `
    --parameters env=$env
;


```

### Deploy function app code

```powershell

### In code/functionapp1 folder

func azure functionapp publish "func-${appName}-${env}"

```