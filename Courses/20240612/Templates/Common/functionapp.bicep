targetScope = 'resourceGroup'

param functionAppName string
param location string
param planId string
param appInsightConnectionString string
param storageAccountName string
param keyVaultName string
param secretName string
param serviceBusConnectionAlias string
param serviceBusNamespaceName string
param alwaysOn bool = true

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
      alwaysOn: alwaysOn
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
        {
          name: '${serviceBusConnectionAlias}__fullyQualifiedNamespace'
          value: '${serviceBusNamespaceName}.servicebus.windows.net'
        }
      ]
    }
  }
}

output principalId string = functionApp.identity.principalId
