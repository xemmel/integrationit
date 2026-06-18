## Delete resource groups
> CAUTION!!!!!

```powershell
az group list -o json | convertfrom-json | out-gridview -PassThru | ForEach-Object { az group delete --name $_.name --yes --no-wait }

```