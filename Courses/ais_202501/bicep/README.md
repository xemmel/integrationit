```powershell
> ..\ais_202501\bicep

$rgName = "rg-***template-remove"

az group create --name $rgName --location $location;

az deployment group create --resource-group $rgName --template-file .\integrationInfrastructure.bicep --parameters storageAccountName=***bicepstorage

```