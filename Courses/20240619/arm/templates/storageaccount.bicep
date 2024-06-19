targetScope = 'resourceGroup'

param appName string
param location string
param sku string


var storageAccountName = 'st${appName}'

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: sku
  }
  kind: 'StorageV2'
}
