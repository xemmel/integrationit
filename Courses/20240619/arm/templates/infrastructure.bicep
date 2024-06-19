targetScope = 'resourceGroup'

param appName string 
param location string = resourceGroup().location
param sku string = 'Standard_LRS'


module workspace 'law.bicep' = {
  name: 'workspace'
  params: {
    appName: appName
    location: location
  }
}

//App Insight
module appInsight 'appInsight.bicep' = {
  name: 'appInsight'
  params: {
    appName: appName
    location: location
    workspaceId: workspace.outputs.id
  }
}


module storageAccount 'storageaccount.bicep' = {
  name: 'storageAccount'
  params: {
    appName: appName
    location: location
    sku: sku
  }
}



