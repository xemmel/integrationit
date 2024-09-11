param appName string
param entity string
param env string
param location string = resourceGroup().location



var commonRgName = 'rg-${appName}-common-${env}'

//Existing Log Analytics Workspace
var workspaceName = 'log-${appName}-${env}'
resource workspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' existing = {
  name: workspaceName
  scope: resourceGroup(commonRgName)
}

//Application Insight
var appInsightName = 'appi-${appName}-${entity}-${env}'
module appInsight 'Common/applicationInsight.bicep' = {
  name: 'appInsight'
  params: {
    location: location
    appInsightName: appInsightName
    workspaceId: workspace.id
  }
}
