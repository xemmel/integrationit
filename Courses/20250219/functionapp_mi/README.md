## Queue trigger

```

Storage Queue Data Contributor

key: externalstorage__queueServiceUri

value: https://az204mlcmiexternal.queue.core.windows.net

```

### System Storage Account

```
Storage Account Contributor
Storage Blob Data Owner
Storage Queue Data Contributor


key: AzureWebJobsStorage__accountname
value: az204mlcmiba1b

```


### Key Vault reference

```

https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references?tabs=azure-cli

@Microsoft.KeyVault(VaultName=az204mlcmi;SecretName=theftppassword)

```

### create web api with controllers

```powershell
dotnet new webapi -o thesecureapi --use-controllers

```