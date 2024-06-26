targetScope = 'resourceGroup'

param topicName string
param location string

resource topic 'Microsoft.EventGrid/topics@2022-06-15' = {
  name: topicName
  location: location
}

output id string = topic.id
output endpoint string = topic.properties.endpoint


