```powershell
> ..\ais_202501\bicep

$rgName = "rg-***template-remove"
$location = "germanywestcentral"

az group create --name $rgName --location $location;

az deployment group create `
    --resource-group $rgName `
    --template-file .\integrationInfrastructure.bicep `
    --parameters platformName=***intplatform `
    --parameters env=test



### Cleanup

az group delete --name $rgName --no-wait --yes


```