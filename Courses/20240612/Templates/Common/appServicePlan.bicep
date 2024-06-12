targetScope = 'resourceGroup'

param appServicePlanName string
param location string

param skuTier string = 'Standard'
param skuName string = 'S1'
param capacity int = 1


resource plan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: skuName
    tier: skuTier
    capacity: capacity
  }
  
}

output id string = plan.id
