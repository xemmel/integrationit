targetScope = 'resourceGroup'

param appName string
param env string
param retention int = 93
param location string = resourceGroup().location

//Log Analytics Workspace
var workspaceName = 'log-${appName}-${env}'

module workspace 'Common/logAnalyticsWorkspace.bicep' = {
  name: 'workspace'
  params: {
    location: location
    workspaceName: workspaceName
    retention: retention
  }
}

//Application Insight
var appInsightName = 'appi-${appName}-${env}'
module appInsight 'Common/applicationInsight.bicep' = {
  name: 'appInsight'
  params: {
    appInsightName: appInsightName
    location: location
    workspaceId: workspace.outputs.id
  }
}

//Storage Account

var storageAccountName = 'st${appName}${env}'
module storageAccount 'Common/storageAccount.bicep' = {
  name: 'storageAccount'
  params: {
    accountName: storageAccountName
    location: location
  }
}

//Key Vault 
var vaultName = 'kv-${appName}-${env}'
module vault 'Common/keyVault.bicep' = {
  name: 'vault'
  params: {
    location: location
    vaultName: vaultName
    adminGroupId: '3f6abe16-efc8-4b34-9fd7-8d917de9c592'
    purgeProtection: true
    softDelete: false
  }
}

//App Service Plan

var planName = 'asp-${appName}-${env}'
module plan 'Common/appServicePlan.bicep' = {
  name: 'plan'
  params: {
    appServicePlanName: planName
    location: location
  }
}

//Function App
var functionAppName = 'func-${appName}-${env}'
module functionApp 'Common/functionapp.bicep' = {
  name: 'functionApp'
  params: {
    appInsightConnectionString: appInsight.outputs.connectionString
    functionAppName: functionAppName
    location: location
    planId: plan.outputs.id
    storageAccountName: storageAccount.outputs.name
    keyVaultName: vault.outputs.name
    secretName: 'thesecret'
  }
}



//Manual entry of secret

//Add Role Assignment (Storage Blob Data Owner)
//RoleId: b7e6dc6d-f1e8-4753-8033-0f276bb0955b
module rbacDataOwner 'Common/roleAssignment.bicep' = {
  name: 'rbacDataOwner'
  params: {
    identityId: functionApp.outputs.principalId
    roleId: 'b7e6dc6d-f1e8-4753-8033-0f276bb0955b'
  }
}

//Add Role Assignment (Key Vault Secrets User)
//RoleId: 4633458b-17de-408a-b874-0445c86b69e6 
//Resource Group ok, if each domain has its own Vault
module rbacSecretReader 'Common/roleAssignment.bicep' = {
  name: 'rbacSecretReader'
  params: {
    identityId: functionApp.outputs.principalId
    roleId: '4633458b-17de-408a-b874-0445c86b69e6'
  }
}


