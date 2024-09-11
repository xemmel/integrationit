param (
    [string]$appName,
    [string]$env,
    [string]$location,
    [string]$companyShortName
)

$rgName = "rg-${appName}-common-${env}";

### TODO Talk about tags

### Create Resource Group
az group create --name $rgName --location $location;


az deployment group create `
   --resource-group $rgName `
   --template-file .\commonApp.bicep `
   --parameters appName=$appName `
   --parameters env=$env `
   --parameters companyShortName=$companyShortName
;

