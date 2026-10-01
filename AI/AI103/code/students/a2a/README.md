## Init

```powershell

cd c:\code\integration

git pull 

cd c:\code\integrationit\AI\AI103\code\students\a2a


winget install Microsoft.Azd
azd config set auth.useAzCliAuth true


```

### Create Agent math

```powershell

$agentName = "the-goofy-math-agent"
$orchestratorAgentName = "the-org-agent"
python create_agent_math.py --name $agentname --deployment maxi 

```

### Create connection to Agent math

```powershell

#### Get a token for doing manual HTTP Calls 

$token = az account get-access-token `
    --resource https://ai.azure.com `
    --query accessToken `
    -o tsv


### Create agent card for the math agent

$body = @{
    agent_card = @{
        description = "A math specialist agent"
        version = "1.0"
        skills = @(
            @{
                id = "math"
                name = "Math"
                description = "Solves mathematical problems"
            }
        )
    }
    agent_endpoint = @{
        protocol_configuration = @{
            responses = @{}
            a2a = @{}
        }
    }
} | ConvertTo-Json -Depth 10

Invoke-RestMethod `
    -Method Patch `
    -Uri "$env:FOUNDRY_PROJECT_ENDPOINT/agents/$agentName`?api-version=v1" `
    -Headers @{ Authorization = "Bearer $token" } `
    -ContentType "application/json" `
    -Body $body

Invoke-RestMethod `
    -Uri "$env:FOUNDRY_PROJECT_ENDPOINT/agents/$agentName/endpoint/protocols/a2a/agentCard/v1.0" `
    -Headers @{ Authorization = "Bearer $token" } |
    ConvertTo-Json -Depth 10


### Create a connection to the math agent

azd ai project set $env:FOUNDRY_PROJECT_ENDPOINT

$target = "$env:FOUNDRY_PROJECT_ENDPOINT/agents/$agentName/endpoint/protocols/a2a"

azd ai connection create "a2a-$agentname" `
    --kind remote-a2a `
    --target $target `
    --auth-type user-entra-token `
    --audience https://ai.azure.com


### Verify the connection

azd ai connection show "a2a-$agentname"

```

### Create main agent using math

```powershell

python create_agent_main.py --name $orchestratorAgentName --a2aconnection "a2a-$agentname"  --deployment medium

```

- Try in *playground*  (9+9 and other math problems)
- Examine the *Log Analytics Workspace* to see the *A2A* calls

- Change your math agent (make it answer 44 instead of 42) and save the new version in the *Foundry Portal*
- Notice that the changes reflects immediately