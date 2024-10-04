param appName string
param env string
param location string = resourceGroup().location


//Create Log Analytics Workspace
var workspaceName =  'log-${appName}-${env}'
module workspace 'monitorWorkspace.bicep' = {
  name: 'workspace'
  params: {
    location: location
    workspaceName: workspaceName
  }
}

//Create App Insight
var insightName = 'appi-${appName}-${env}'
module insight 'appInsight.bicep' = {
  name: 'insight'
  params: {
    location: location
    insightName: insightName
    workspaceId: workspace.outputs.id
  }
}
