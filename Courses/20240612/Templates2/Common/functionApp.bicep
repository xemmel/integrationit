param functionAppName string
param planId string
param location string
param storageAccountName string
param appInsightConnectionString string
param appConfigurationStoreConnectionString string
param appConfigLabelName string
param alwaysOn bool = true

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
          name: 'AppConfigEndpoint'
          value: appConfigurationStoreConnectionString
        }
        {
          name: 'AppConfigLabelFilter'
          value: appConfigLabelName
        }
      ]
    }
  }
}

//RoleId: b7e6dc6d-f1e8-4753-8033-0f276bb0955b
//Storage Blob Data Owner
module rbacDataOwner 'roleAssignment.bicep' = {
  name: 'rbacDataOwner'
  params: {
    identityId: functionApp.identity.principalId
    roleId: 'b7e6dc6d-f1e8-4753-8033-0f276bb0955b'
  }
}

//RoleId: 17d1049b-9a84-46fb-8f53-869881c3d3ab
//Storage Account Contributor
module rbacStorageContributor 'roleAssignment.bicep' = {
  name: 'rbacStorageContributor'
  params: {
    identityId: functionApp.identity.principalId
    roleId: '17d1049b-9a84-46fb-8f53-869881c3d3ab'
  }
}

//RoleId: 974c5e8b-45b9-4653-ba55-5f855dd0fb88
//Storage Queue Data Contributor
module rbacStorageQueueDataContributor 'roleAssignment.bicep' = {
  name: 'rbacStorageQueueDataContributor'
  params: {
    identityId: functionApp.identity.principalId
    roleId: '974c5e8b-45b9-4653-ba55-5f855dd0fb88'
  }
}

output principalId string = functionApp.identity.principalId


