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


//Receive HTTP Logic App
var receiveHttpLogicAppName = 'la-${appName}-${env}-rec-http'

resource receiveHttpLogicApp 'Microsoft.Logic/workflows@2019-05-01' = {
    name: receiveHttpLogicAppName
    location: location
    properties: {
        definition: {
            '$schema' : 'https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#'
            contentVersion: '1.0.0.0'
            parameters: {
                '$connections' : {
                    defaultValue: {}
                    type: 'Object'
                }
            }
            triggers: {
                HttpTrigger: {
                    type: 'Request'
                    kind: 'Http'
                    inputs: {
                        method: 'POST'
                    }
                }
            }
            actions: {
                CreateBlobName: {
                    inputs: '@guid()'
                    type: 'Compose'
                    runAfter: {}
                }
            }
        }
    }
}
