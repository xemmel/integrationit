targetScope = 'resourceGroup'

param namespaceName string
param location string
param sku string = 'Standard'

resource serviceBusNamespace 'Microsoft.ServiceBus/namespaces@2021-11-01' = {
  name: namespaceName
  location: location
  sku: {
    name: sku
    tier: sku
  }
}

output id string = serviceBusNamespace.id
output name string = serviceBusNamespace.name



