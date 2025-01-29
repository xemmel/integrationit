param storageAccountName string
param location string = 'germanywestcentral'
param storageAccountSKU string = 'Standard_GRS'


var storageKind = 'StorageV2'
resource userMI 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'mortensid'
  location: location
}

resource sb 'Microsoft.ServiceBus/namespaces@2024-01-01' = {
  name: 'mortenssb'
  location: location
}

resource sa 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: storageAccountSKU
  }
  kind: storageKind
}
