### Deploy arm template

```powershell
$rgName = "rg-mlc-deploydemo-remove"

az group create --name $rgName --location germanywestcentral



$env="test"
$env="prod"

az deployment group create --resource-group $rgName --template-file .\template\bicep\storageaccount.bicep --parameters appName=mlcappen --parameters .\template\parameters\$env\app.json
