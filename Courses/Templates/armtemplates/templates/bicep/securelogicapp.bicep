param workflowName string
param location string = resourceGroup().location

param audience string = ''
param tenantId string = ''
param oid string = ''

var triggerName = 'http'
resource workflow 'Microsoft.Logic/workflows@2019-05-01' = {
  name: workflowName
  location: location
  properties: {
    definition: {
      '$schema' : 'https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#'
      contentVersion: '1.0.0.0'
      actions: {
        Response: {
          inputs: {
            statusCode: 200
            body: 'Secure message'
          }
          type: 'Response'
          kind: 'Http'
          runAfter: {}
        }

      }
      triggers: {
        '${triggerName}': {
           conditions: [
            {
              expression: '@startsWith(triggerOutputs()?[\'headers\']?[\'Authorization\'], \'Bearer\')'
            }
           ]
           inputs: {
             schema: {}
           }
           kind: 'Http'
           operationOptions: 'IncludeAuthorizationHeadersInOutputs'
           type: 'Request'
        }
      }
    }
    accessControl: {
      triggers: {
        openAuthenticationPolicies: {
          policies: {
            useronly: {
              type: 'AAD'
              claims: [
                {
                  name: 'iss'
                  value: 'https://sts.windows.net/${tenantId}/'
                }
                {
                  name: 'aud'
                  value: audience
                }
                {
                  name: 'oid'
                  value: oid
                }
              ]
            }

          }
        }
      }
    }
  }
}


output callbackUrl string = listCallbackUrl(resourceId('Microsoft.Logic/workflows/triggers', workflowName, triggerName), '2016-06-01').value
