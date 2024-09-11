param (
    [string]$appName,
    [string]$entity,
    [string]$env,
    [string]$location
)

$rgCommonName = "rg-${appName}-common-${env}";
$rgName = "rg-${appName}-${entity}-${env}";

### Create Resource Group
az group create --name $rgName --location $location;

az deployment group create `
   --resource-group $rgName `
   --template-file .\appEntity.bicep `
   --parameters appName=$appName `
   --parameters entity=$entity `
   --parameters env=$env `
;

