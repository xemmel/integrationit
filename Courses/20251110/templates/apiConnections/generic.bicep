param apiName string
param displayName string
param location string
param apiType string

resource apiConnection 'Microsoft.Web/connections@2016-06-01' = {
  name: apiName
  location: location
  kind: 'V1'
  properties: {
    displayName: displayName
    customParameterValues: {}
    api: {
      id: subscriptionResourceId('Microsoft.Web/locations/managedApis',location,apiType)
      name: apiName
      type: 'Microsoft.Web/locations/managedApis'
    }
    parameterValueSet: {
      name: 'managedIdentityAuth'
      values: {}
    }
  }
}
