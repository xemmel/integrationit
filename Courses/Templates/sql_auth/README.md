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

### Add an External User

```sql

CREATE USER [sqlaccount2] FROM EXTERNAL PROVIDER;

```

### Add Role to External User

```sql
ALTER ROLE [db_datareader] ADD MEMBER [sqlaccount2]
GO

```

### Remove Role from External User

```sql
ALTER ROLE [db_datareader] DROP MEMBER [sqlaccount2];
GO

```