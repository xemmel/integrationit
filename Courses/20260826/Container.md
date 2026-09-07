## Web App Container

```powershell

### Create Resource Group

$RGNAME="ai-200-mlc-container2"
$APPNAME="ai200mlc"
$LOCATION="germanywestcentral"


az group create `
  --name $RGNAME `
  --location $LOCATION

 

### Create App Service Plan

$aspJson = az appservice plan create `
  --resource-group $RGNAME `
  --name $APPNAME `
  --location $LOCATION `
  --is-linux true  `
  --sku P0V3

$aspId = $aspJson | ConvertFrom-Json | select-object -expandProperty id


### Create webApp

$imageName = "teknomlc.azurecr.io/myapi:1.3";


az webapp create `
  --resource-group $RGNAME `
  --name $APPNAME `
  --plan $aspId `
  --container-image-name $imageName `
  --acr-use-identity 


```

### 

```

- Enable System Managed Identity on the web app
- ACR (teknomlc) 
  -> Access Control (IAM)
     -> Add -> Add Role Assignment
        -> AcrPull
        -> "User" : [The name of your webapp]
           -> Review+Assign (2 times)

- Deployment 
   - Deployment Center 
     - Logs


- Overview in Web App (URL)

URL/version
 -> 1.2

 ```