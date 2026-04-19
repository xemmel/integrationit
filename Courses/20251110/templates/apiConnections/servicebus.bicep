param apiConnectionName string
param location string 
param serviceBusNamespace string

resource serviceBusConnection 'Microsoft.Web/connections@2016-06-01' = {
  name: apiConnectionName
  location: location
  properties: {
    api: {
      id: 'subscriptions/${subscription().subscriptionId}/providers/Microsoft.Web/locations/${location}/managedApis/servicebus'
    }
    parameterValueSet: {
      name: 'managedIdentityAuth'
      values: {
        namespaceEndpoint: {
          value: 'sb://${serviceBusNamespace}.servicebus.windows.net'
        }
      }
    }
  }
}
