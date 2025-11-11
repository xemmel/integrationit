param appName string
param env string
param location string = resourceGroup().location


//storage account
var storageaccountname = '${appName}${env}st'

resource storageAccount 'Microsoft.Storage/storageAccounts@2025-01-01' = {
    name: storageaccountname
    location: location
    sku: {
        name: 'Standard_LRS'
    }
    kind: 'StorageV2'
}


resource blobService 'Microsoft.Storage/storageAccounts/blobServices@2025-01-01' = {
    name: 'default'
    parent: storageAccount
}

resource container 'Microsoft.Storage/storageAccounts/blobServices/containers@2025-01-01' = {
    name: 'process'
    parent: blobService
}


//Service bus namespace
var servicebusName = 'sb-${appName}-${env}'
resource serviceBus 'Microsoft.ServiceBus/namespaces@2024-01-01' = {
    name: servicebusName
    location: location
    sku: {
        name: 'Standard'
    }
}

//Process Queue

resource serviceBusProcessQueue 'Microsoft.ServiceBus/namespaces/queues@2024-01-01' = {
    name: 'process'
    parent: serviceBus
}
