param baseName string
param env string
param location string = resourceGroup().location
param sku string = 'Standard'


var serviceBusNamespaceName = '${baseName}-${env}'
resource serviceBusNamespace 'Microsoft.ServiceBus/namespaces@2024-01-01' = {
  name: serviceBusNamespaceName
  location: location
  sku: {
    name: sku
    tier: sku
  }
}
