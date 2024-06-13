targetScope = 'resourceGroup'

param appName string
param subDomainName string
param env string
param location string

//Storage Account
var storageAccountName = 'st${appName}${subDomainName}${env}'
module storageAccount 'storageAccount.bicep' = {
  name: 'storageAccount${subDomainName}'
  params: {
    accountName: storageAccountName
    location: location
  }
}

//Existing Log Analytics Workspace
var workspaceName = 'log-${appName}-${env}'
resource workspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' existing = {
  name: workspaceName
}

//Application Insight
var applicationInsightName = 'appi-${appName}-${subDomainName}-${env}'
module appInsight 'applicationInsight.bicep' = {
  name: 'appInsight${subDomainName}'
  params: {
    appInsightName: applicationInsightName
    location: location
    workspaceId: workspace.id
  }
}

//Consumption Plan
var planName = 'asp-${appName}-${subDomainName}-${env}'
module plan 'appServicePlan.bicep' = {
  name: 'plan${subDomainName}'
  params: {
    appServicePlanName: planName
    location: location
    skuName: 'Y1'
    skuTier: 'Dynamic'
  }
}


//Function App
var functionAppName = 'func-${appName}-${subDomainName}-${env}'
module functionApp 'functionapp.bicep' = {
  name: 'functionApp${subDomainName}'
  params: {
    appInsightConnectionString: appInsight.outputs.connectionString
    functionAppName: functionAppName
    keyVaultName: 'kv-${appName}-${env}'
    location: location
    planId: plan.outputs.id
    secretName: 'thesecret'
    serviceBusConnectionAlias: 'andersand'
    serviceBusNamespaceName: 'andersand'
    storageAccountName: storageAccount.outputs.name
    alwaysOn: false
  }
}

//Manual entry of secret

//Add Role Assignment (Storage Blob Data Owner)
//RoleId: b7e6dc6d-f1e8-4753-8033-0f276bb0955b
module rbacDataOwner 'roleAssignment.bicep' = {
  name: 'rbacDataOwner${subDomainName}'
  params: {
    identityId: functionApp.outputs.principalId
    roleId: 'b7e6dc6d-f1e8-4753-8033-0f276bb0955b'
  }
}

//Add Role Assignment (Key Vault Secrets User)
//RoleId: 4633458b-17de-408a-b874-0445c86b69e6 
//Resource Group ok, if each domain has its own Vault
module rbacSecretReader 'roleAssignment.bicep' = {
  name: 'rbacSecretReader${subDomainName}'
  params: {
    identityId: functionApp.outputs.principalId
    roleId: '4633458b-17de-408a-b874-0445c86b69e6'
  }
}

//Add Role Assignment (Azure Service Bus Data Owner)
//RoleId: 090c5cfd-751d-490a-894a-3ce6f1109419
//Resource Group ok, if each domain has its own Vault
module rbacSBOwner 'roleAssignment.bicep' = {
  name: 'rbacSBOwner${subDomainName}'
  params: {
    identityId: functionApp.outputs.principalId
    roleId: '090c5cfd-751d-490a-894a-3ce6f1109419'
  }
}

output appInsightId string = appInsight.outputs.id
output storageAccountName string = storageAccount.outputs.name
output functionAppIdentity string = functionApp.outputs.principalId

