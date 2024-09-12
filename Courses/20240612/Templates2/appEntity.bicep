param appName string
param companyShortName string
param entity string
param env string
param location string = resourceGroup().location


var fullName = '${appName}-${entity}-${env}'
var commonFullName = '${appName}-common-${env}'

var fullUniqueName = '${appName}-${entity}-${companyShortName}-${env}'
var fullUniqueStandardName = '${appName}${entity}${companyShortName}${env}'


var commonRgName = 'rg-${commonFullName}'

//Existing Log Analytics Workspace
var workspaceName = 'log-${commonFullName}'
resource workspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' existing = {
  name: workspaceName
  scope: resourceGroup(commonRgName)
}

//Existing App Service Plan
var planName = 'asp-${commonFullName}'
resource plan 'Microsoft.Web/serverfarms@2022-09-01' existing = {
  name: planName
  scope: resourceGroup(commonRgName)
}


//Application Insight
var appInsightName = 'appi-${fullName}'
module appInsight 'Common/applicationInsight.bicep' = {
  name: 'appInsight'
  params: {
    location: location
    appInsightName: appInsightName
    workspaceId: workspace.id
  }
}

//Storage Account (Function App System)
var storageAccountName = 'st${fullUniqueStandardName}'
module storageAccount 'Common/storageAccount.bicep' = {
  name: 'storageAccount'
  params: {
    location: location
    accountName: storageAccountName
  }
}

//Function App
var functionAppName = 'func-${fullUniqueName}'
module functionApp 'Common/functionApp.bicep' = {
  name: 'functionApp'
  params: {
    location: location
    appInsightConnectionString: appInsight.outputs.connectionString
    functionAppName: functionAppName
    planId: plan.id
    storageAccountName: storageAccount.outputs.name 
  }
}
