param workflowName string
param location string

param messageType string


resource workflow 'Microsoft.Logic/workflows@2019-05-01' = {
  name: workflowName
  location: location
  properties: {
    state: 'Enabled'
    definition: {
      '$schema' : 'https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#'
      contentVersion: '1.0.0.0'
      triggers: {
        httpTrigger: {
          type: 'Request'
          kind: 'Http'
          inputs: {
            method: 'Post'
          }
        }
      }
      actions: {
        GetMessageType : {
          type: 'Compose'
          runAfter: {}
          inputs: messageType
        }
      }
    }
  }
}
