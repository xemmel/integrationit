###

```bash

export FOUNDRY_PROJECT_ENDPOINT="https://aimorten.services.ai.azure.com/api/projects/aimorten-project"
export OPENAI_ENDPOINT="https://aimorten.openai.azure.com/openai/v1"
export FOUNDRY_MODEL="medium"

read -p "Enter key: " FOUNDRY_KEY
export FOUNDRY_KEY


```

###

```powershell

$ENV:FOUNDRY_PROJECT_ENDPOINT="https://aimorten.services.ai.azure.com/api/projects/aimorten-project"
$ENV:OPENAI_ENDPOINT="https://aimorten.openai.azure.com/openai/v1"
$ENV:FOUNDRY_MODEL="medium"


$ENV:FOUNDRY_KEY=Read-Host("key")


$ENV:SQL_CONNECTION_STRING="Server=sql-mytripsworld.database.windows.net,1433;Database=mytrips;Authentication=ActiveDirectoryDefault;Encrypt=yes;TrustServerCertificate=no;"




```