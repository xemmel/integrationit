param identityId string
param roleName string

resource role 'Microsoft.Authorization/roleDefinitions@2022-04-01' existing = {
  scope: subscription()
  name: roleName
}

resource roleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(resourceGroup().id, identityId, role.id)
  scope: resourceGroup()
  properties: {
    principalId: identityId
    roleDefinitionId: role.id
  }
}
