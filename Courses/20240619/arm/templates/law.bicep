targetScope = 'resourceGroup'

param appName string
param location string

var workspaceName = 'log-${appName}'
resource laWorkspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: workspaceName
  location: location
}

output id string = laWorkspace.id
