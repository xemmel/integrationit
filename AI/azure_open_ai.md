## Azure OpenAI

```bash

SUBSCRIPTIONID="....."
RGNAME="rg-ai-ai-ai"
OPENAINAME="flowgraitai"
LOCATION="swedencentral"


az group create \
  --name $RGNAME \
  --location $LOCATION \
  --subscription $SUBSCRIPTIONID


AZUREOPENAI=$(az cognitiveservices account create \
	--kind "OpenAI" \
	--resource-group $RGNAME \
	--name $OPENAINAME \
	--subscription $SUBSCRIPTIONID \
	--sku "S0" \
	--custom-domain $OPENAINAME \
	--location $LOCATION
)


### List models

 	
	
az cognitiveservices model list \
	--location $LOCATION | 
	jq . | less
	
	


### List deployments

az cognitiveservices account deployment list \
  --resource-group $RGNAME \
  --name $OPENAINAME \
  --subscription $SUBSCRIPTIONID
  
  
### Create deployment

DEPLOYMENTNAME="main"
MODELNAME="gpt-5";
MODELFORMAT="OpenAI"
MODELVERSION="2025-08-07"
MODELSKU="GlobalStandard"
CAPACITY="150"

az cognitiveservices account deployment create \
   --subscription $SUBSCRIPTIONID \
   --resource-group $RGNAME \
   --name $OPENAINAME \
   --deployment-name $DEPLOYMENTNAME \
   --model-name $MODELNAME \
   --model-version $MODELVERSION \
   --model-format $MODELFORMAT \
   --capacity $CAPACITY \
   --sku $MODELSKU

   
   
### Call

AZUREOPENAIENDPOINT=$(echo $AZUREOPENAI | jq .properties.endpoint -r)
AZUREOPENAIKEY=$(
az cognitiveservices account keys list \
  --subscription $SUBSCRIPTIONID \
  --resource-group $RGNAME \
  --name $OPENAINAME |
  jq .key1 -r
)  
   
   
BODY=$(cat <<EOF
{
    "messages" : [
	   {
	      "role": "user",
		  "content" : "Who was the first us president"
	   }
	]
}
EOF
)
   
   
curl "${AZUREOPENAIENDPOINT}openai/deployments/$DEPLOYMENTNAME/chat/completions?api-version=2024-10-21" \
  -X POST \
  -d "$BODY" \
  -H "Authorization: Bearer $AZUREOPENAIKEY" \
  -H "Content-Type:application/json" -s |
  jq .choices[0].message.content

   

az group delete --name $RGNAME --subscription $SUBSCRIPTIONID --yes

az cognitiveservices account purge \
  --subscription $SUBSCRIPTIONID \
  --resource-group $RGNAME \
  --name $OPENAINAME \
  --location $LOCATION



```