## MCP Servers

### Init

```bash

export FOUNDRY_NAME="integration-it"
export FOUNDRY_RG="rg-ai-integration-it"
export FOUNDRY_PROJECT_NAME="integration-it-project"
export FOUNDRY_AGENT_NAME="standard-agent"

```

#### List projects

```bash
az cognitiveservices account project list \
  --name $FOUNDRY_NAME \
  --resource-group $FOUNDRY_RG

```

#### List Agents

```bash

az cognitiveservices agent list \
  --account-name $FOUNDRY_NAME \
  --project-name $FOUNDRY_PROJECT_NAME |
    jq .[0].name -r

```

### Optional Init