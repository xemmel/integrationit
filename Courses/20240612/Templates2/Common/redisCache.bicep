param cacheName string
param location string
param sku string = 'Standard'

resource cache 'Microsoft.Cache/redis@2023-08-01' = {
  name: cacheName
  location: location
  properties: {
    sku: {
      name: sku
      capacity: 1
      family: 'C'
    }
  }
}


