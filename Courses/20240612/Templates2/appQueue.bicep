param appName string
param companyShortName string
param env string
param queueName string
param requiresDuplicateDetection bool
param duplicateDetectionHistoryTimeWindow string
param maxDeliveryCount int

var serviceBusNamespaceName = 'sbns-${appName}-${companyShortName}-${env}'

module queue 'Common/ServiceBus/serviceBusQueue.bicep' = {
  name: 'queue'
  params: {
    queueName: '${queueName}queue'
    serviceBusNamespace: serviceBusNamespaceName 
    requiresDuplicateDetection: requiresDuplicateDetection
    duplicateDetectionHistoryTimeWindow: duplicateDetectionHistoryTimeWindow
    maxDeliveryCount: maxDeliveryCount
  }
}
