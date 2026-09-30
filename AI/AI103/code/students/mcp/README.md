## Create agent

```powershell

cd c:\code\integration

git pull 

cd c:\code\integrationit\AI\AI103\code\students\mcp

python .\create_agent.py `
    --name main-agent `
    --deployment <deployment_name> `
     --mcpserver "https://ai103mcpserver.calmflower-<code>.germanywestcentral.azurecontainerapps.io/mcp"

python app_agent_tools.py --agent main-agent

```