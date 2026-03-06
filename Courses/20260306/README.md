### All Key Vaults and Access Control

$keyvaults = az keyvault list | ConvertFrom-Json;
foreach($keyvaultsimple in $keyvaults) {
   $keyvault = az keyvault show --name $keyvaultsimple.name | ConvertFrom-Json;
   $mode = $keyvault.properties.enableRbacAuthorization;
   Write-Host("$($keyvaultsimple.name) RBAC: ${mode}");
}


### Azure CLI

az login --use-device-code

az group list -o table

### Func

#### New Function App Project

func init myfunctions --worker-runtime dotnet-isolated --target-framework net10.0

#### New Function

func new -n Calculator


#### List current directory
ls 

#### Create directory
mkdir code

#### Go to directory
cd code


