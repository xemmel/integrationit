## Init

```powershell

cd c:\code\integration

git pull 

cd c:\code\integrationit\AI\AI103\code\students\foundryIQ

python .\create_vector_db.py --folder datafolder

## Get the vector id

python .\create_agent.py --name main-agent --deployment medium --mcpserver "https://ai103mcpserver.calmflower-<>.germanywestcentral.azurecontainerapps.io/mcp" --vectorid "<>"

python app_agent_tools.py --agent main-agent

```


## In client/agent

```python

from azure.ai.projects.models import (
    PromptAgentDefinition,
    FileSearchTool
)

file_search = FileSearchTool(
    vector_store_ids=[vector_store.id]
)

```


