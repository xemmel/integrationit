targetScope = 'resourceGroup'

param vaultName string
param location string 
param adminGroupId string
param purgeProtection bool = true
param softDelete bool = true
param softDeleteDays int = 7

resource vault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: vaultName
  location: location
  properties: {
    sku: {
      family: 'A'
      name:  'standard'
    }
    tenantId: tenant().tenantId
    accessPolicies: []
    enableRbacAuthorization: true
    enableSoftDelete: softDelete
    enablePurgeProtection: purgeProtection
    softDeleteRetentionInDays: softDeleteDays
  }
}

//RBAC to admin group
var roleId = '00482a5a-887f-4fb3-b363-3b7fe8e74483'

resource role 'Microsoft.Authorization/roleDefinitions@2022-04-01' existing = {
  scope: subscription()
  name: roleId
}


resource roleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(resourceGroup().id, adminGroupId, roleId)
  scope: vault
  properties: {
    principalId: adminGroupId
    roleDefinitionId: role.id
  }
}


output id string = vault.id
output name string = vault.name
