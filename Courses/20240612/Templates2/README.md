
## Common App Deployment

.\script\deploy_common_app.ps1 -appName $appName -env $env -location $location -companyShortName $companyShortName;

## App Entity Deployment

.\script\deploy_app_entity.ps1 -appName $appName -entity $entity -env $env -location $location -companyShortName $companyShortName -createQueue $true





### Naming

$appName = "mb";
$env = "test";
$entity = "user";
$companyShortName = "mlc";
$location = "northeurope";


##### Common

Resource Group: rg-${appName}-common-${env}
   Log Ana Workspace: log-${appName}-${env}
   App Service Plan: asp-${appName}-${env}
   App Configuration Store: appcs-${appName}-${companyShortName}-${env}

##### Entity

Resource Group: rg-${appName}-${entity}-${env}
   Application Insight: appi-${appName}-${entity}-${env}
   Storage Account: st${appName}${entity}${companyShortName}${env}
   Function App: func-${appName}-${entity}-${env}


### functionApp.bicep

   - 



### Get Role Definition id/name from DisplayName

```powershell
$roleName = "Storage Account Contributor";

az role definition list | ConvertFrom-Json | Where-Object {$_.RoleName -eq "${roleName}"} | Select-Object -ExpandProperty name

```