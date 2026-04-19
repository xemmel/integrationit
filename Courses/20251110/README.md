## AIS Course 2025


### Deploy the platform

#### Azure CLI

```powershell

$env = "test"
$init = "mlc2" ## Change
$appName = "${init}theplatform";

$rgName = "rg-ais-${appName}-${env}";
$storageAccountName = "${appName}${env}"
$location = "germanywestcentral"


## Create resource group

az group create --location $location --name $rgName


## Create storage account

az storage account create `
   --name $storageAccountName `
   --resource-group $rgName `
   --location $location `
   --sku Standard_LRS

### Create Container: process


az storage container create `
  --name process `
  --account-name $storageAccountName


### Create Queue: process


az storage queue create `
  --name process `
  --account-name $storageAccountName



```

### Cleanup

```powershell

az group delete --name $rgName --yes



```



### Deploy as bicep

```powershell

az group create --location $location --name $rgName

$deploymentJson = az deployment group create `
  --template-file .\templates\theplatform.bicep `
  --resource-group $rgName `
  --parameters appName=$appName `
  --parameters env=$env

$deployment = $deploymentJson | ConvertFrom-Json
$logicappUrl = $deployment.properties.outputs.receiveHttpLogicAppUrl.value

curl $logicappUrl -X POST -d "hello logic app"


```


### Delete Resource Group

```powershell

az group delete --name $rgName --yes

```


#### Queries


AppRequests
| where Name == 'Calculator'
| summarize count() by tostring(Success)
| render piechart 


AppRequests
| where Name == 'Calculator'
| summarize count() by bin(TimeGenerated,1m), tostring(Success)
| render barchart 

AppTraces
| extend number_ = tostring(Properties.number)
| where number_ != ''
| summarize count() by number_
| render piechart 


AppRequests
| where Name == 'Calculator'
| project TimeGenerated, Success,DurationMs,OperationId
| order by TimeGenerated desc
