targetScope = 'resourceGroup'

param serviceBusNamespace string
param queueName string

resource servicebus 'Microsoft.ServiceBus/namespaces@2021-11-01' existing = {
  name: serviceBusNamespace
}

resource queue 'Microsoft.ServiceBus/namespaces/queues@2021-11-01' = {
  name: queueName
  parent: servicebus
  properties: {
    deadLetteringOnMessageExpiration: true
  }
}


