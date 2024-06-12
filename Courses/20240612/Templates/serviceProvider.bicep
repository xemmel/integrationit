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
  }
}

//Add Role Assignment (Storage Blob Data Owner)
//RoleId: b7e6dc6d-f1e8-4753-8033-0f276bb0955b
module rbacDataOwner 'Common/roleAssignment.bicep' = {
  name: 'rbacDataOwner'
  params: {
    identityId: functionApp.outputs.principalId
    roleId: 'b7e6dc6d-f1e8-4753-8033-0f276bb0955b'
  }
}
