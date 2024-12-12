>   ...`integrationit

```powershell
$APPNAME="....."
$LOCATION="northeurope"


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
    --template-file .\Courses\Templates\armtemplates\templates\bicep\securelogicapp.bicep `
    --parameters workflowName="la-${APPNAME}" `
    --parameters tenantId=551c586d-a82d-4526-b186-d061ceaa589e `
    --parameters audience=https://management.azure.com/ `
    --parameters oid="$($mid.principalId)"

$laDeployment = $laDeploymentJson | ConvertFrom-Json;

### WILL NOT WORK!!
$fulllaUrl = $laDeployment.properties.outputs.callbackUrl.value   

### Will work WITH token
$laUrl = $fulllaUrl.Split('&')[0]

curl $fulllaUrl -X Post -d "body"

> evaluation failed: 'The template language function 'startsWith''

curl $laUrl -X Post -d "body"

> {"error":{"code":"DirectApiAuthorizationRequired","message":"The request must be authenticated only by Shared Access scheme."}}
> Not correct error

### Try with your own Token, will not work, ONLY MID can call

$ownToken = az account get-access-token --resource https://management.azure.com/ | ConvertFrom-Json | Select-Object -ExpandProperty accessToken

curl $laUrl -X Post -d "body" -H "Authorization:Bearer $ownToken"

> {"error":{"code":"MisMatchingOAuthClaims","message":"One or more claims either missing or does not match with the open authentication access control policy."}}

### Create API M Service
#### Change name/email, but not required

$apimJson =  az apim create `
  --name "api-${APPNAME}" `
  --publisher-email "lacour@gmail.com" `
  --publisher-name "Morten la Cour" `
  --resource-group "rg-${APPNAME}-remove" `
  --location $LOCATION `
  --sku-name Consumption

$apim = $apimJson | ConvertFrom-Json;


### clean up

az group delete --name "rg-${APPNAME}-remove" --yes --no-wait

### List purged APIM

az apim deletedservice list --output table;


```