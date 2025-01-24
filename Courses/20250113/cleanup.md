```powershell

az group list -o json | ConvertFrom-Json | Select-Object -ExpandProperty SyncRoot | Out-GridView -PassThru | ForEach-Object { az group delete --name $_.name --yes --no-wait}

```