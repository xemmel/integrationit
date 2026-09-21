TOKEN=$(az account get-access-token \
  --resource https://ai.azure.com/ \
  --query accessToken \
  -o tsv)

curl -X POST \
  "${FOUNDRY_PROJECT_ENDPOINT}/agents/simple-json-agent?api-version=v1" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  --data @simple.json


  curl -X POST \
  "${FOUNDRY_PROJECT_ENDPOINT}/agents?api-version=v1" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  --data @azure_queue.json




  curl -X POST \
  "${FOUNDRY_PROJECT_ENDPOINT}/agents/azure-function-json-agent?api-version=v1" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  --data @azure_queue.json

