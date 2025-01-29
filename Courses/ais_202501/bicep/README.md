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


### Get Role Definition Name from roleName

az role definition list -o json | ConvertFrom-Json | Out-GridView -PassThru | ForEach-Object {Write-Host $_.name}

### Cleanup

az group delete --name $rgName --no-wait --yes


```