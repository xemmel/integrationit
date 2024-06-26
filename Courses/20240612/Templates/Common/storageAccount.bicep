targetScope = 'resourceGroup'

param accountName string
param location string
param allowedSharedKeyAccess bool = false

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: accountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    allowSharedKeyAccess: allowedSharedKeyAccess
  }
}

output id string = storageAccount.id

//var storageConnectionString = 'DefaultEndpointsProtocol=https;AccountName=${storageAccount.name};EndpointSuffix=${environment().suffixes.storage};AccountKey=${listKeys(storageAccount.id, storageAccount.apiVersion).keys[0].value}'
//output connectionString string = storageConnectionString

output name string = storageAccount.name
