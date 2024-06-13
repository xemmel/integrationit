targetScope = 'resourceGroup'

param functionAppName string
param location string
param planId string
param appInsightConnectionString string
param storageAccountName string
param keyVaultName string
param secretName string


var passwordKeyVaultReference = '@Microsoft.KeyVault(VaultName=${keyVaultName};SecretName=${secretName})'

resource functionApp 'Microsoft.Web/sites@2023-12-01' = {
  name: functionAppName
  location: location
  kind: 'functionapp'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    serverFarmId: planId
    siteConfig: {
      alwaysOn: true
      appSettings: [
        {
          name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
          value: appInsightConnectionString
        }
        {
          name: 'AzureWebJobsStorage__accountName'
          value: storageAccountName
        }
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'FUNCTIONS_WORKER_RUNTIME'
          value: 'dotnet'
        }
        {
          name: 'password'
          value: passwordKeyVaultReference
        }
      ]
    }
  }
}

output principalId string = functionApp.identity.principalId
