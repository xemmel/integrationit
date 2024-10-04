param accountName string
param location string = resourceGroup().location
param sku string = 'Standard_ZRS'


var kind = 'StorageV2'

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: accountName
  location: location
  sku: {
    name: sku
  }
  kind: kind
}
