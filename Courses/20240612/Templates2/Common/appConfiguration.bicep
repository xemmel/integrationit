param appConfigStoreName string
param location string
param disableLocalAuth bool = true


resource appConfigStore 'Microsoft.AppConfiguration/configurationStores@2023-03-01' = {
  name: appConfigStoreName
  location: location
  sku: {
    name: 'standard'
  }
  properties: {
    disableLocalAuth: disableLocalAuth
  }
}
