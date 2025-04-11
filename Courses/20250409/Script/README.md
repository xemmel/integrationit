CLI:

```powershell

az login --use-device-code
az logout

az group list --output table   ## List all resource groups (in a part. subscription)

az group list | ConvertFrom-Json | Where-Object {$_.location -eq 'westeurope'}


az account show ## Show current subscription etc.

az account list --output table ## list all subscriptions avai.

az account set -s 5a0... ## Change default subscription

--subscription 5a05f... ### Use/view other subscription

```

Powershell:

```powershell

get-azresourcegroup

get-azresourcegroup | Where-Object {$_.Location -eq 'westeurope'}


```


## Create a resource group
### Inside rg create a storage account
### Azure cli

```powershell

$rgName = "rg-mlc-falck-demo2-remove";
$storageAccountName = "falckmlc18";
$containerName = "container1";
$location = "germanywestcentral";

### Create a resource group
az group create --name $rgName --location $location

### Create Storage account
az storage account create `
   --resource-group $rgName `
   --name $storageAccountName `
   --location $location

### Create a container
az storage container create `
  --name $containerName `
  --account-name $storageAccountName


## Upload blob

echo 'Stuff' > test01.txt

az storage blob upload `
  --container-name $containerName `
  --file test01.txt `
  --overwrite `
   --account-name $storageAccountName

### Remove resource group
az group delete --name $rgName --yes --no-wait
  
```
