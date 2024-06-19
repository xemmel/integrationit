targetScope = 'resourceGroup'

param workflowName string
param audience string = 'https://management.azure.com/'
param location string = resourceGroup().location

resource logicApp 'Microsoft.Logic/workflows@2019-05-01' = {
  name: workflowName
  location: location
  properties: {
    definition: {
      '$schema' : 'https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#'
      contentVersion: '1.0.0.0'
      actions: {
        nameHeader: {
          inputs: '@substring(triggerOutputs()?[\'headers\']?[\'Authorization\'],0,10)'
          type: 'Compose'
          runAfter: {}
        }
        response: {
          inputs: {
            statusCode: 200
            body: 'The nameHeader is @{outputs(\'nameHeader\')}'
          }
          kind: 'Http'
          type: 'Response'
          runAfter: { 
            nameHeader: [ 'Succeeded' ]
          }
        }
      }
      triggers: {
        manual: {
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
    accessControl : {
      triggers : {
        openAuthenticationPolicies : {
          policies : {
            mortenonly : {
              type: 'AAD'
              claims: [
                {
                  name: 'iss'
                  value: 'https://sts.windows.net/551c586d-a82d-4526-b186-d061ceaa589e/'
                }
                {
                  name: 'aud'
                  value: audience
                }
              ]
            }
          }
        }
      }
    }
  }
}


output callbackUrl string = listCallbackUrl(resourceId('Microsoft.Logic/workflows/triggers', workflowName, 'manual'), '2016-06-01').value
