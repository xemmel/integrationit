## Init

```PowerShell
$SUBSCRIPTIONID="9bc198aa-089c-4698-a7ef-8af058b48d90"
$INIT = READ-HOST("init")
$APPNAME="ai103${INIT}mcp"
$LOCATION="swedencentral"

```

### Create Resource Group

```powershell
az group create `
  --subscription $SUBSCRIPTIONID `
  --name "rg-${APPNAME}" `
  --location $LOCATION

```

### Create Container Registry

```PowerShell
$ACRJSON=az acr create `
  --subscription $SUBSCRIPTIONID `
  --resource-group "rg-${APPNAME}" `
  --name $APPNAME `
  --sku Basic `
  --location $LOCATION

$ACR = $ACRJSON | ConvertFrom-Json


$ACR_ID=$ACR.id
$ACR_SERVER=$ACR.loginServer

$ACR_ID
$ACR_SERVER

```


### Build image in ACR

```PowerShell
$version = Read-Host("version")

az acr build `
  --subscription $SUBSCRIPTIONID `
  --registry $APPNAME `
  --image "${ACR_SERVER}/webapi:${version}" .


```

### Create User Managed Identity

```PowerShell
$MIDJSON=az identity create `
  --subscription $SUBSCRIPTIONID `
  --resource-group "rg-${APPNAME}" `
  --name "id-${APPNAME}" `
  --location $LOCATION

$MID = $MIDJSON | ConvertFrom-Json


$MID_ID=$MID.id
$MID_PRINCIPALID=$MID.principalId

```

### Add role assignment ACRPull to User MI scope ACR

```PowerShell
az role assignment create `
  --subscription $SUBSCRIPTIONID `
  --role "AcrPull" `
  --scope $ACR_ID `
  --assignee $MID_PRINCIPALID

```

### Create Container App Env

```PowerShell
az containerapp env create `
  --subscription $SUBSCRIPTIONID `
  --resource-group "rg-${APPNAME}" `
  --name "aca-env-${APPNAME}" `
  --location $LOCATION

```

### Create Container App

```PowerShell
$ACAJSON=az containerapp create `
  --subscription $SUBSCRIPTIONID `
  --resource-group "rg-${APPNAME}" `
  --name "aca-${APPNAME}" `
  --environment "aca-env-${APPNAME}" `
  --registry-identity $MID_ID `
  --registry-server $ACR_SERVER `
  --image "${ACR_SERVER}/webapi:1.0" `
  --user-assigned $MID_ID `
  --ingress external `
  --min-replicas 0

$ACA = $ACAJSON | ConvertFrom-Json


$ACA_INGRESS_URL=$ACA.properties.configuration.ingress.fqdn

```

### Build image in ACR

```PowerShell
$version = Read-Host("version")

az acr build `
  --subscription $SUBSCRIPTIONID `
  --registry $APPNAME `
  --image "${ACR_SERVER}/mcpserver:${version}" .


```


### Update container app image

```PowerShell
az containerapp update `
  --subscription $SUBSCRIPTIONID `
  --resource-group "rg-${APPNAME}" `
  --name "aca-${APPNAME}" `
  --image "${ACR_SERVER}/mcpserver:${version}" `
  --no-wait

```