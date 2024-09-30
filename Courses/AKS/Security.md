### WhiteList IP's in a public AKS

```powershell



```

### View IpList

```powershell

az aks show `
    --resource-group $rgName `
    --name $aksCluster.name `
    --subscription $subscriptionId
;

```