param (
    [string]$appName,
    [string]$entity,
    [string]$env,
    [string]$location,
    [string]$companyShortName,
    [bool]$createQueue
)

$rgName = "rg-${appName}-${entity}-${env}";

### Create Resource Group
az group create --name $rgName --location $location;

az deployment group create `
   --resource-group $rgName `
   --template-file .\appEntity.bicep `
   --parameters appName=$appName `
   --parameters entity=$entity `
   --parameters env=$env `
   --parameters companyShortName=$companyShortName `
   --parameters createQueue=$createQueue
;


