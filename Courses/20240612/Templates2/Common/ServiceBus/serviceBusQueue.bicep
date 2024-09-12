targetScope = 'resourceGroup'

param serviceBusNamespace string
param queueName string
param requiresDuplicateDetection bool = false
param duplicateDetectionHistoryTimeWindow string = 'P1D'
param maxDeliveryCount int = 10

resource servicebus 'Microsoft.ServiceBus/namespaces@2021-11-01' existing = {
  name: serviceBusNamespace
}

resource queue 'Microsoft.ServiceBus/namespaces/queues@2021-11-01' = {
  name: queueName
  parent: servicebus
  properties: {
    requiresDuplicateDetection: requiresDuplicateDetection
    duplicateDetectionHistoryTimeWindow: duplicateDetectionHistoryTimeWindow
    maxDeliveryCount: maxDeliveryCount
  }
}


