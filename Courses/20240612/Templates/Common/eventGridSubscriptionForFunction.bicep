targetScope = 'resourceGroup'

param subscriptionName string
param topicName string
param functionAppName string
param functionName string


resource topic 'Microsoft.EventGrid/topics@2022-06-15' existing = {
  name: topicName
  scope: resourceGroup()
}

resource functionApp 'Microsoft.Web/sites@2023-12-01' existing = {
  name: functionAppName
}


var functionResourceId = '${functionApp.id}/functions/${functionName}'

resource subscription 'Microsoft.EventGrid/topics/eventSubscriptions@2022-06-15' = {
  name: subscriptionName
  parent: topic
  properties: {
    destination: {
      endpointType: 'AzureFunction'
      properties: {
        resourceId: functionResourceId
        maxEventsPerBatch: 1

      }
    }
  }
}
