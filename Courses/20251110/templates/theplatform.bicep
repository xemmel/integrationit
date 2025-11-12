param appName string
param env string
param location string = resourceGroup().location


var workspaceName = 'log-${appName}-${env}'
resource workspace 'Microsoft.OperationalInsights/workspaces@2025-02-01' = {
    name: workspaceName
    location: location
}

//storage account
var storageaccountname = '${appName}${env}st'

resource storageAccount 'Microsoft.Storage/storageAccounts@2025-01-01' = {
    name: storageaccountname
    location: location
    sku: {
        name: 'Standard_LRS'
    }
    kind: 'StorageV2'
}


resource blobService 'Microsoft.Storage/storageAccounts/blobServices@2025-01-01' = {
    name: 'default'
    parent: storageAccount
}

resource container 'Microsoft.Storage/storageAccounts/blobServices/containers@2025-01-01' = {
    name: 'process'
    parent: blobService
}


//Service bus namespace
var servicebusName = 'sb-${appName}-${env}'
resource serviceBus 'Microsoft.ServiceBus/namespaces@2024-01-01' = {
    name: servicebusName
    location: location
    sku: {
        name: 'Standard'
    }
}

//Process Queue

resource serviceBusProcessQueue 'Microsoft.ServiceBus/namespaces/queues@2024-01-01' = {
    name: 'process'
    parent: serviceBus
}


//Receive HTTP Logic App
var receiveHttpLogicAppName = 'la-${appName}-${env}-rec-http'
var triggerName = 'HttpTrigger'
resource receiveHttpLogicApp 'Microsoft.Logic/workflows@2019-05-01' = {
    name: receiveHttpLogicAppName
    location: location
    identity: {
        type: 'SystemAssigned'
    }
    properties: {
        definition: {
            '$schema' : 'https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#'
            contentVersion: '1.0.0.0'
            parameters: {
                '$connections' : {
                    defaultValue: {}
                    type: 'Object'
                }
            }
            triggers: {
                '${triggerName}': {
                    type: 'Request'
                    kind: 'Http'
                    inputs: {
                        method: 'POST'
                    }
                }
            }
            actions: {
                CreateBlobName: {
                    inputs: '@guid()'
                    type: 'Compose'
                    runAfter: {}
                }
                Response: {
                    inputs: {
                        statusCode: 200
                        body: 'Message: @{outputs(\'CreateBlobName\')} submitted'
                    }
                    type: 'Response'
                    kind: 'Http'
                    runAfter: {
                        CreateBlobName: [ 'Succeeded' ]
                        
                    }
                }
            }
        }
    }
}


//Role Assignments

//Service bus data owner

var servicebusOwnerRoleName = '090c5cfd-751d-490a-894a-3ce6f1109419'
module ra_servicebusOwner 'roleassignment_rg.bicep' = {
    params: {
        identityId: receiveHttpLogicApp.identity.principalId
        roleName: servicebusOwnerRoleName
    }
}

//Service bus data owner

var blobOwnerRoleName = 'b7e6dc6d-f1e8-4753-8033-0f276bb0955b'
module ra_blobOwner 'roleassignment_rg.bicep' = {
    params: {
        identityId: receiveHttpLogicApp.identity.principalId
        roleName: blobOwnerRoleName
    }
}


///Function App



//Application Insight
var appInsightKind = 'web'
resource appInsight 'Microsoft.Insights/components@2020-02-02' = {
  name: 'appi-${appName}-${env}'
  location: location
  kind: appInsightKind
  properties: {
    Application_Type: appInsightKind
    WorkspaceResourceId: workspace.id
    DisableLocalAuth: true
  }
}

//Storage Account
resource funcstorageAccount 'Microsoft.Storage/storageAccounts@2025-01-01' = {
  name: 'func${appName}${env}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    allowSharedKeyAccess: false
    allowBlobPublicAccess: false
  }
}

//blob Service
resource funcblobService 'Microsoft.Storage/storageAccounts/blobServices@2025-01-01' = {
  name: 'default'
  parent: funcstorageAccount
}

//deployment container
resource funcdeploymentContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2025-01-01' = {
  name: 'deployment'
  parent: funcblobService
}

//Plan

resource plan 'Microsoft.Web/serverfarms@2024-11-01' = {
  name: 'plan-${appName}-${env}'
  location: location
  sku: {
    name: 'FC1'
    tier: 'FlexConsumption'
    size: 'FC1'
    family: 'FC'
    capacity: 0
  }
  kind: 'functionapp'
  properties: {
    reserved: true
  }
}

//Flex Function app
resource functionapp 'Microsoft.Web/sites@2024-11-01' = {
  name: 'func-${appName}-${env}'
  location: location
  kind: 'functionapp,linux'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    serverFarmId: plan.id
    reserved: true
    siteConfig: {
      alwaysOn: false
      appSettings: [
        {
          name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
          value: appInsight.properties.ConnectionString
        }
        {
          name: 'APPLICATIONINSIGHTS_AUTHENTICATION_STRING'
          value: 'Authorization=AAD'
        }
        {
          name: 'AzureWebJobsStorage__accountName'
          value: storageAccount.name
        }
      ]
    }
    functionAppConfig: {
      deployment: {
        storage: {
          type: 'blobContainer'
          value: '${storageAccount.properties.primaryEndpoints.blob}${funcdeploymentContainer.name}'
          authentication: {
            type: 'SystemAssignedIdentity'
          }
        }
      }
      runtime: {
        name: 'dotnet-isolated'
        version: '9.0'
      }
      scaleAndConcurrency: {
        maximumInstanceCount: 100
        instanceMemoryMB: 2048
      }
    }
  }
}

//Role assignments

var blobOwnerRoleId = 'b7e6dc6d-f1e8-4753-8033-0f276bb0955b'
module blobOwnerRBAC 'roleassignment_rg.bicep' = {
  params: {
    identityId: functionapp.identity.principalId
    roleName: blobOwnerRoleId
  }
}

//Monitoring Metrics Publisher


var monitorRoleId = '3913510d-42f4-4e42-8a64-420c390055eb'
module monitorrRBAC 'roleassignment_rg.bicep' = {
  params: {
    identityId: functionapp.identity.principalId
    roleName: monitorRoleId
  }
}


var callback = receiveHttpLogicApp.listCallbackUrl(receiveHttpLogicApp.apiVersion)
var triggerCallback = replace(callback.value,'?api','/triggers/${triggerName}/paths/invoke/api')

output receiveHttpLogicAppUrl string = triggerCallback
