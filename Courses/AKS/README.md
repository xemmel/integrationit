### Set up

```powershell

$location = "germanywestcentral";


### Check available AKS (kubernetes) versions and upgrade possibilities

az aks get-versions --location $location -o table | more


$version = "1.30.1"  ## Can upgrade to "1.30.4"

$location = "germanywestcentral";
$appName = "intitaks";
$yourinit = "mlc";
$subscriptionId = "9bc198aa-089c-4698-a7ef-8af058b48d90"; ## Teaching Test

$rgName = "rg-${appName}-${yourinit}";

### Check if exists
az resource list -g $rgName --subscription $subscriptionId -o table;


### Create Resource Group
az group create `
   --name $rgName `
   --location $location `
   --subscription $subscriptionId
;


### Create Log Analytics Workspace

$workspaceJson = az monitor log-analytics workspace create `
    --name "log-${appName}-${yourinit}" `
    --resource-group $rgName `
    --location $location `
   --subscription $subscriptionId
;

$workspace = $workspaceJson | ConvertFrom-Json;

### Create ACR (Azure Container registry)   -> Note argument --workspace is still in preview

$acrJson = az acr create `
  --name "acr${appName}${yourinit}" `
  --resource-group $rgName `
  --sku "Basic" `
  --admin-enabled $false `
  --location $location `
  --workspace $workspace.id `
  --subscription $subscriptionId
;


$acr = $acrJson | ConvertFrom-Json;


### Create AKS Cluster using Azure CLI

$aksClusterJson = az aks create `
    --name "aks-${appName}-${yourinit}" `
    --resource-group $rgName `
    --attach-acr $acr.id `
    --enable-msi-auth-for-monitoring `
    --generate-ssh-keys `
    --kubernetes-version $version `
    --location $location `
    --enable-oidc-issuer `
    --enable-workload-identity `
    --enable-cluster-autoscaler `
    --min-count 2 `
    --max-count 3 `
    --node-count 2 `
    --subscription $subscriptionId
;


$aksCluster = $aksClusterJson | ConvertFrom-Json;


--enable-azure-rbac

```

### Register kubectl to new AKS Cluster

```powershell

az aks get-credentials --name "aks-${appName}-${yourinit}"  --resource-group $rgName --subscription $subscriptionId --overwrite-existing;


```

### Add Log Analytics Workspace addin

```powershell

az aks enable-addons -a monitoring `
    --name $aksCluster.name `
    --resource-group $rgName `
    --workspace-resource-id $workspace.id `
    --enable-msi-auth-for-monitoring `
    --subscription $subscriptionId
    ;

```



### View

```powershell

az resource list -g "MC_${rgName}_aks-${appName}-${yourinit}_${location}" --subscription $subscriptionId -o table;

az resource list -g $rgName --subscription $subscriptionId -o table;


```




#### Show upgrade possibilities

```powershell

az aks get-upgrades --name $aksCluster.name --resource-group $rgName --subscription $subscriptionId -o table

```


#### Upgrade cluster

```powershell

$newKubernetesVersion = "1.30.3";

az aks upgrade `
    --name $aksCluster.name `
    --resource-group $rgName `
    --kubernetes-version $newKubernetesVersion `
    --yes `
    --subscription $subscriptionId
;

```


### Cleanup

```powershell

az group delete --name $rgName --yes --no-wait --subscription $subscriptionId;



```