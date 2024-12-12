>   ...\integrationit

```powershell
$APPNAME="....."
$LOCATION="germanywestcentral"


### Create REsource Group

az group create --name "rg-${APPNAME}-remove" --location $LOCATION

### Create User Managed Identity

$midJson = az identity create `
     --resource-group "rg-${APPNAME}-remove" `
     --name "id-${APPNAME}" `
     --location $LOCATION

$mid = $midJson | ConvertFrom-Json;

### Deploy Secure Logic App, where MID is the ONLY identity allowed to call

$laDeploymentJson = az deployment group create `
    --resource-group "rg-${APPNAME}-remove" `
    --template-file secure_logicapp.bicep `
    --parameters workflowName="la-${APPNAME}" `
    --parameters tenantId=551c586d-a82d-4526-b186-d061ceaa589e `
    --parameters audience=https://management.azure.com/ `
    --parameters oid=$mid.principalId

$laDeployment = $laDeploymentJson | ConvertFrom-Json;


```