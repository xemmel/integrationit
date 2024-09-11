param appName string
param env string
param location string = resourceGroup().location

//Log Analytics Workspace
var workspaceName = 'log-${appName}-${env}'
module workspace 'Common/logAnalyticsWorkspace.bicep' = {
  name: 'workspace'
  params: {
    location: location
    retention: 180
    workspaceName: workspaceName
  }
}
