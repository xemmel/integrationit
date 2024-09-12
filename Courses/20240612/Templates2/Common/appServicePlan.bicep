targetScope = 'resourceGroup'

param appServicePlanName string
param location string

param skuTier string = 'Premium0V3'
param skuName string = 'P0v3'
param capacity int = 1


resource plan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: skuName
    tier: skuTier
    capacity: capacity
  }
  kind: 'linux'
  properties: {
    reserved: true
  }

}

output id string = plan.id
