### Create a custom-app Resource Group

```powershell
$rgAppName = "rg-${appName}-${yourinit}-apps";

### Check if exists
az resource list -g $rgAppName --subscription $subscriptionId -o table;


### Create Resource Group
az group create `
   --name $rgAppName `
   --location $location `
   --subscription $subscriptionId
;

```




#### Get the OIDC Issuer URL

```powershell

$aksIssuer = az aks show --name $aksCluster.name `
    --resource-group $rgName `
    --query "oidcIssuerProfile.issuerUrl" `
    --subscription $subscriptionId `
    --output tsv
;

$aksIssuer;

```

### Create a User Managed Identity

```powershell

$appIdJson = az identity create `
    --name  "id-${appName}-${yourinit}-apps" `
    --resource-group $rgAppName `
    --location $location `
    --subscription $subscriptionId
;

$appId = $appIdJson | ConvertFrom-Json;


```


### Create a kubernetes namespace

```powershell

kubectl create namespace workloadtest

kubectl config set-context --current --namespace workloadtest



```

### Create a Service Account

Make a copy of **templates\workload\serviceAccount.yaml** and change the *azure.workload.identity/client-id* to **$appId.ClientId**

```powershell

kubectl apply --filename .\templates\workload\serviceAcount2.yaml

```

### Create a federated identity between the User MI and the kubernetes SA

```powershell

az identity federated-credential create `
    --name "fedidentity" `
    --identity-name $appId.Name `
    --resource-group $rgAppName `
    --issuer $aksIssuer `
    --subject system:serviceaccount:workloadtest:sa-testaccount `
    --audience api://AzureADTokenExchange `
    --subscription $subscriptionId

```

### Apply a template to test

```powershell

kubectl apply --filename .\templates\workload\deployment.yaml


curl 10.......:8080/token?resource=https://storage.azure.com/.default

```