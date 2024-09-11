targetScope  = 'resourceGroup'

param workspaceName string
param location string
param retention int

resource workspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: workspaceName
  location: location
  properties:  {
    retentionInDays: retention
  }
}

output id string = workspace.id
