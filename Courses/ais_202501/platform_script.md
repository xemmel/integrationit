```powershell

$location = "germanywestcentral"
$appName = "thefinalmlcintplat"
$env = "test"

$rgName = "rg-${appName}-${env}"

## Create resource group
$rgJson = az group create --name $rgName --location $location;

$rg = $rgJson | ConvertFrom-json;

### Create identity
$identityJson = az identity create `
  --resource-group $rgName  `
  --name "id-${appName}-${env}"



## Create storage account
$saJson = az storage account create `
  --resource-group $rgName `
  --name "${appName}${env}"
$sa = $saJson | ConvertFrom-Json;


### Create Service Bus Namespace
$sbJson = az servicebus namespace create `
  --name "sb-${appName}-${env}" `
  --resource-group $rgName
;
$sb = $sbJson | ConvertFrom-Json;




$identity = $identityJson | ConvertFrom-Json

### Create role assignment (User MI)
#### Storage Account
#### Storage Account Blob Owner
az role assignment create `
   --role "Storage Blob Data Owner" `
   --scope $sa.id `
   --assignee $identity.clientId
;

### Create role assignment (User MI)
#### Service Bus Namespace 
#### Storage Account Blob Owner
az role assignment create `
   --role "Azure Service Bus Data Owner" `
   --scope $sb.id `
   --assignee $identity.clientId
;



```

```powershell


### Cleanup

az group delete --name $rgName --no-wait --yes

```