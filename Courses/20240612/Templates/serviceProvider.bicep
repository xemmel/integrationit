targetScope = 'resourceGroup'

param appName string
param env string
param retention int = 93
param vaultIdentity string
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


//Key Vault 
var vaultName = 'kv-${appName}-${env}'
module vault 'Common/keyVault.bicep' = {
  name: 'vault'
  params: {
    location: location
    vaultName: vaultName
    adminGroupId: vaultIdentity
    purgeProtection: true
    softDelete: false
  }
}




//Service Bus
var serviceBusNamespaceName = 'sbns-${appName}-${env}'
module serviceBus 'Common/serviceBusNamespace.bicep' = {
  name: 'serviceBus'
  params: {
    location: location
    namespaceName: serviceBusNamespaceName
  }
}

//myqueue Queue
module myqueueQueue 'Common/serviceBusQueue.bicep' = {
  name: 'myqueueQueue'
  params: {
    queueName: 'myqueue'
    serviceBusNamespace: serviceBus.outputs.name
  }
}

//myoutputqueue Queue
module myoutputqueueQueue 'Common/serviceBusQueue.bicep' = {
  name: 'myoutputqueueQueue'
  params: {
    queueName: 'myoutputqueue'
    serviceBusNamespace: serviceBus.outputs.name
  }
}







//Sub-Domain function app (morten)
module subDomainMortenJobFunctionApp 'Common/functionAppWithAux.bicep' = {
  name: 'subDomainMortenJobFunctionApp'
  params: {
    appName: appName
    env: env
    location: location 
    subDomainName: 'morten'
  }
}

//Sub-Domain function app (morten2)
module subDomainMorten2JobFunctionApp 'Common/functionAppWithAux.bicep' = {
  name: 'subDomainMorten2JobFunctionApp'
  params: {
    appName: appName
    env: env
    location: location 
    subDomainName: 'morten2'
  }
}



