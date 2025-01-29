param platformName string
param env string
param location string = 'germanywestcentral'
param storageAccountSKU string = 'Standard_GRS'


var storageKind = 'StorageV2'


var userMIName = 'id-${platformName}-${env}'
resource userManagedIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: userMIName
  location: location
}

var sbName = 'sbns-${platformName}-${env}'
resource serviceBusNamespace 'Microsoft.ServiceBus/namespaces@2024-01-01' = {
  name: sbName
  location: location
}

var saName = 'sa${platformName}${env}'
resource sa 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: saName
  location: location
  sku: {
    name: storageAccountSKU
  }
  kind: storageKind
}
