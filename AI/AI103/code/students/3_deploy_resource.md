## Deploy with Bicep

### Init Variables 
```powershell

$personalInitials = Read-Host("Your initials")

$appName = "ai103-deploy-${personalInitials}"
$rgName = "rg-${appName}"

$location = "swedencentral"

```

### Create Resource Group

```powershell

az group create --name $rgName --location $location

```

### Deploy Foundry Resource + AUX

```powershell

$deploymentResult = az deployment group create `
  --resource-group $rgName `
  --template-file 3_deployment.bicep `
  --parameters appName=$appName


```

### Test 

```powershell

$key = az cognitiveservices account keys list --name "aif-$appName" --resource-group $rgName | 
    ConvertFrom-Json | 
    Select-Object -ExpandProperty key1


$body = @"
{
   "messages" : [
	{
             "role" : "user",
             "content" : "What is the capital of France"
        }
  ], 
  "model" : "mini"
}
"@




$response = curl "https://aif-${appName}.openai.azure.com/openai/v1/chat/completions" -X POST `
  -H "Authorization: Bearer $key" `
  -H "Content-Type:application/json" `
  -d $body -s

$response = $response | ConvertFrom-Json
$response.choices.message.content


```` 

### Cleanup

```powershell

az group delete --name $rgName --yes 



```