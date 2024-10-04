param insightName string
param location string
param workspaceId string

var kind = 'web'

resource appInsight 'Microsoft.Insights/components@2020-02-02' = {
  name: insightName
  location: location
  kind: kind
  properties: {
    Application_Type: kind
    WorkspaceResourceId: workspaceId
  }
}
