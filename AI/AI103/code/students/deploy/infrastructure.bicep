param appName string
param env string

param location string = resourceGroup().location

//Log Analytics Workspace
var workspaceName = 'log-${appName}-${env}'
resource workspace 'Microsoft.OperationalInsights/workspaces@2026-03-01' = {
  name: workspaceName
  location: location
}

//App Insight
var appInsightName = 'appi-${appName}-${env}'
var appInsightKind = 'web'
resource appInsight 'Microsoft.Insights/components@2020-02-02' = {
  name: appInsightName
  location: location
  kind: appInsightKind
  properties: {
    Application_Type: appInsightKind
    WorkspaceResourceId: workspace.id
  }
}


var foundryServiceName = 'aif-${appName}-${env}'
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
    disableLocalAuth: true
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
