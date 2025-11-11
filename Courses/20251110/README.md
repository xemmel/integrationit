## AIS Course 2025


### Deploy the platform

#### Azure CLI

```powershell

$env = "test"
$init = "mlc" ## Change
$appName = "${init}theplatform";

$rgName = "rg-ais-${appName}-${env}";
$storageAccountName = "${appName}${env}"
$location = "germanywestcentral"


## Create resource group

az group create --location $location --name $rgName


## Create storage account

az storage account create `
   --name $storageAccountName `
   --resource-group $rgName `
   --location $location `
   --sku Standard_LRS


az storage container create `
  --name process `
  --account-name $storageAccountName



```