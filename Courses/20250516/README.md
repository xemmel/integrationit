### Agenda

```

MS Agenda:


- Web Apps (x)
- Function Apps (x)
- Storage (x)
- Cosmos
- Containers
- Auth/Auth
- Security 
     -Key Vault
     - MI (x)
     - App Configuration
- API Management
- Event Based
     - Grid/Hub
- Message Based (x)
- App Insight / Monitoring

```


### Missing

- Cosmos
- Containers
- Secure your own apps
- Key vault
- API M
- Events
- Monitoring




### Clean up with CLI

#### In powershell ISE 


```powershell

az group list -o json | ConvertFrom-Json | Select-Object -ExpandProperty SyncRoot | Out-GridView -PassThru | ForEach-Object { az group delete --name $_.name --no-wait --yes }

 ```

 #### In powershell core (filter in out-gridview not working!!)

```powershell

az group list -o json | ConvertFrom-Json  | Out-GridView -PassThru | ForEach-Object { az group delete --name $_.name --no-wait --yes }

```