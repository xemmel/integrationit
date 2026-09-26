```bash

## MCP


/mcp

docker build -t mcpserver:1.0 .
docker run --name mcp1 --publish 7777:8000 -d mcpserver:1.0



ACA_ENDPOINT=$(az containerapp show \
  --name mcpserverdemo \
  --resource-group rg-containerapp-remove \
  --query properties.configuration.ingress.fqdn \
  -o tsv)

MCP_ENDPOINT="https://${ACA_ENDPOINT}/mcp"




az containerapp create \
  --name mcpserverdemo \
  --resource-group rg-containerapp-remove \
  --environment thenewappapphello-env \
  --image acrthenewappapphello.azurecr.io/mcpserver:1.0 \
  --ingress external \
  --target-port 8000 \
  --user-assigned /subscriptions/9bc198aa-089c-4698-a7ef-8af058b48d90/resourcegroups/rg-containerapp-remove/providers/Microsoft.ManagedIdentity/userAssignedIdentities/id-thenewappapphello \
  --registry-server acrthenewappapphello.azurecr.io \
  --registry-identity /subscriptions/9bc198aa-089c-4698-a7ef-8af058b48d90/resourcegroups/rg-containerapp-remove/providers/Microsoft.ManagedIdentity/userAssignedIdentities/id-thenewappapphello

python3 list_mcp_tools.py --server $MCP_ENDPOINT


read -r -p "Version: " CONTAINER_VERSION

az acr build -t "acrthenewappapphello.azurecr.io/mcpserver:${CONTAINER_VERSION}" -r acrthenewappapphello .


az containerapp update \
  --name mcpserverdemo \
  --resource-group rg-containerapp-remove \
  --image "acrthenewappapphello.azurecr.io/mcpserver:${CONTAINER_VERSION}"
  

az containerapp update \
  --name mcpserverdemo \
  --resource-group rg-containerapp-remove \
  --image acrthenewappapphello.azurecr.io/mcpserver:1.0


### Check if ACA is running

az containerapp replica list \
  --name mcpserverdemo \
  --resource-group rg-containerapp-remove \
  -o table
  
 
  
  
python3 app_remote_mcp.py --agentname mcp-test-agent


### Create agent that uses mcp server

python3 build_agent_with_mcp.py \
  --agentname mcp-test-agent \
  --model mini5 \
  --mcpserver $MCP_ENDPOINT
  
  
### Run app with agent
  

```