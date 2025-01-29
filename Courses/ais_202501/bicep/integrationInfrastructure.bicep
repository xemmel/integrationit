param platformName string
param env string
param location string = resourceGroup().location
param storageAccountSKU string = 'Standard_GRS'


var storageKind = 'StorageV2'

//User Managed ID
var userMIName = 'id-${platformName}-${env}'
resource userManagedIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: userMIName
  location: location
}

//Log analytic Workspace
var laWorkspaceName = 'log-${platformName}-${env}'
resource logWorkspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: laWorkspaceName
  location: location
}

//Service Bus
var sbName = 'sbns-${platformName}-${env}'
resource serviceBusNamespace 'Microsoft.ServiceBus/namespaces@2024-01-01' = {
  name: sbName
  location: location
}

//Storage Account
var saName = 'sa${platformName}${env}'
resource sa 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: saName
  location: location
  sku: {
    name: storageAccountSKU
  }
  kind: storageKind
}

//Role Assignment UserMI/Blob Data Owner/SA


var userMIPrincipalId = userManagedIdentity.properties.principalId

module roleAssignmentBlobOwner 'rbacResourceGroup.bicep' = {
  name: 'roleAssignmentBlobOwner'
  params: {
    identityId: userMIPrincipalId
    roleName: 'b7e6dc6d-f1e8-4753-8033-0f276bb0955b'
  }
}


//Role Assignment UserMI/Service Bus Data Owner/SB
module roleAssignmentSBDataOwner 'rbacResourceGroup.bicep' = {
  name: 'roleAssignmentSBDataOwner'
  params: {
    identityId: userMIPrincipalId
    roleName: '090c5cfd-751d-490a-894a-3ce6f1109419'
  }
}

//Logic app (receive orders)
module laReceiveOrders 'workflow.bicep' = {
  name: 'laReceiveOrders'
  params: {
    location: location
    workflowName: 'receive-orders'
    messageType: 'Order'
    workspaceId: logWorkspace.id
  }
}

//Logic app (receive invoice)
module laReceiveInvoice 'workflow.bicep' = {
  name: 'laReceiveInvoice'
  params: {
    location: location
    workflowName: 'receive-invoice'
    messageType: 'Invoice'
    workspaceId: logWorkspace.id
  }
}

//Logic app (receive credit-note)
module laReceiveCreditNote 'workflow.bicep' = {
  name: 'laReceiveCreditNote'
  params: {
    location: location
    workflowName: 'receive-creditnote'
    messageType: 'CreditNote'
    workspaceId: logWorkspace.id
  }
}

