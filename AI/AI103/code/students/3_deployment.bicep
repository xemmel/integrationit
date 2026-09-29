param appName string
param location string = resourceGroup().location
param disableLocalAuth bool = false


// Foundry Service

var foundryServiceName = 'aif-${appName}'
var foundryProjectName = '${foundryServiceName}-project'
resource foundryService 'Microsoft.CognitiveServices/accounts@2026-07-01' = {
  name: foundryServiceName
  location: location
  sku: {
    name: 'S0'
  }
  kind: 'AIServices'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    customSubDomainName: foundryServiceName
    disableLocalAuth: disableLocalAuth
    allowProjectManagement: true
    defaultProject: foundryProjectName
    associatedProjects: [
      foundryProjectName
    ]
    publicNetworkAccess: 'Enabled'
  }
}

/// Foundry Project
resource foundryProject 'Microsoft.CognitiveServices/accounts/projects@2026-07-01' = {
  parent: foundryService
  name: foundryProjectName
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    displayName: foundryProjectName
  }

}

// Deployment
resource model 'Microsoft.CognitiveServices/accounts/deployments@2025-06-01' = {
  parent: foundryService
  name: 'mini'
  sku: {
    name: 'GlobalStandard'
    capacity: 10
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: 'gpt-5-mini'
      version: '2025-08-07'
    }
    versionUpgradeOption: 'OnceCurrentVersionExpired'
  }
}
