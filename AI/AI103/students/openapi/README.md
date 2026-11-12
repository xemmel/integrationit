## Init

```PowerShell
$SUBSCRIPTIONID="9bc198aa-089c-4698-a7ef-8af058b48d90"
$INIT = READ-HOST("init")
$APPNAME="ai103${INIT}mcp"

$APIAPPNAME = "ai103${INIT}openai"
$LOCATION="swedencentral"

```

```PowerShell
$version = Read-Host("version")

az acr build `
  --subscription $SUBSCRIPTIONID `
  --registry $APPNAME `
  --image "${ACR_SERVER}/openapi:${version}" .


```

### Create Container App

```PowerShell
$ACAJSON=az containerapp create `
  --subscription $SUBSCRIPTIONID `
  --resource-group "rg-${APPNAME}" `
  --name "aca-${APPNAME}-openapi" `
  --environment "aca-env-${APPNAME}" `
  --registry-identity $MID_ID `
  --registry-server $ACR_SERVER `
  --image "${ACR_SERVER}/openapi:${version}" `
  --user-assigned $MID_ID `
  --ingress external `
  --min-replicas 0

$ACA = $ACAJSON | ConvertFrom-Json


$ACA_INGRESS_URL=$ACA.properties.configuration.ingress.fqdn

```


### Update container app image

```PowerShell
az containerapp update `
  --subscription $SUBSCRIPTIONID `
  --resource-group "rg-${APPNAME}" `
  --name "aca-${APPNAME}-openapi" `
  --image "${ACR_SERVER}/openapi:${version}" `
  --no-wait

```

### Test

```powershell

curl "https://$ACA_INGRESS_URL/version"

curl "https://$ACA_INGRESS_URL/funnyquote"

```


### Create agent with openapi

```powershell

$openapi_url = "https://aca-ai103mlcmcp-openapi.politeplant-a3834678.swedencentral.azurecontainerapps.io"
$model = "large"

python .\agent.py --agent_name agentopenapi --model $model --openapi_url $openapi_url


```