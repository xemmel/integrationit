### List all Entra external users

```sql

select
dp.principal_id,
dp.name,
CONVERT(UNIQUEIDENTIFIER, dp.sid) AS ClientId,
dp.type_desc,
dp.default_schema_name
from
sys.database_principals dp
where dp.[type] = 'E'

```

### List all Entra external role members 

```sql

select
dp_role.[name] as 'Role Name',
dp_principal.[name] as 'Principal',
CONVERT(UNIQUEIDENTIFIER, dp_principal.sid) AS ClientId
from
sys.database_role_members drm
inner join 
sys.database_principals dp_role
on (drm.role_principal_id = dp_role.principal_id)
inner join
sys.database_principals dp_principal
on (drm.member_principal_id = dp_principal.principal_id)
where dp_principal.type = 'E'

```

### Add a Entra Service Account

```powershell

$accountName = "sqlaccount3";

Connect-MgGraph -Scopes "Application.ReadWrite.All"

$appReg = New-MgApplication -DisplayName $accountName

$servicePrincipal = New-MgServicePrincipal -AppId $appReg.AppId

$secret = Add-MgApplicationPassword -ApplicationId $appReg.Id

```

### Set existing appReg/SP vars

```powershell

$accountName = "sqlaccount3";

Connect-MgGraph -Scopes "Application.ReadWrite.All"

$appReg = get-mgapplication -all | Where-Object {$_.DisplayName -eq $accountName}
$servicePrincipal = get-mgservicePrincipal -All | Where-Object {$_.AppId -eq $appReg.AppId}
$secret = Add-MgApplicationPassword -ApplicationId $appReg.Id

```

### Remove Entra Service Account

```powershell

Remove-MgServicePrincipal -ServicePrincipalId $servicePrincipal.Id
Remove-MgApplication -ApplicationId $appReg.Id

```

### Set Variables according to new AppReg and SP

```powershell

$env:AZURE_CLIENT_ID = $appReg.AppId;
$env:AZURE_TENANT_ID = (Get-MgContext).TenantId;
$env:AZURE_CLIENT_SECRET = $secret.secretText;

```

### Reset Vars

```powershell

$env:AZURE_CLIENT_ID = $null;
$env:AZURE_TENANT_ID = $null;
$env:AZURE_CLIENT_SECRET = $null;

```




### Add an External User

```sql

CREATE USER [sqlaccount3] FROM EXTERNAL PROVIDER;
GO


```

### Add Role to External User

```sql
ALTER ROLE [db_datareader] ADD MEMBER [sqlaccount3]
ALTER ROLE [db_datawriter] ADD MEMBER [sqlaccount3]

GO

```

### Remove Role from External User

```sql
ALTER ROLE [db_datareader] DROP MEMBER [sqlaccount2];
GO

```




### Run with App Registration

```powershell

$env:AZURE_CLIENT_ID = "d51bb746-6d63-4270-a267-f9fb7b53a20e";
$env:AZURE_TENANT_ID = "551c586d-a82d-4526-b186-d061ceaa589e";
$env:AZURE_CLIENT_SECRET = "Koq8......";

```