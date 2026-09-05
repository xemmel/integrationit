## MCP Servers

### Init

```bash

export FOUNDRY_NAME="integration-it"
export FOUNDRY_RG="rg-ai-integration-it"
export FOUNDRY_PROJECT_NAME="integration-it-project"
export FOUNDRY_AGENT_NAME="standard-agent"
export FOUNDRY_DEPLOYMENT="common"


```

#### List projects

```bash
az cognitiveservices account project list \
  --name $FOUNDRY_NAME \
  --resource-group $FOUNDRY_RG

export FOUNDRY_PROJECT_ENDPOINT=$(az cognitiveservices account project list   --name $FOUNDRY_NAME   --resource-group $FOUNDRY_RG | jq '.[0].properties.endpoints.["AI Foundry API"]' -r)

```

#### List Agents

```bash

az cognitiveservices agent list \
  --account-name $FOUNDRY_NAME \
  --project-name $FOUNDRY_PROJECT_NAME |
    jq .[0].name -r

```

#### List models

```bash

az cognitiveservices account deployment list \
  --name $FOUNDRY_NAME \
  --resource-group $FOUNDRY_RG |
  jq .[].name 



```

### Code

#### Simple completion

##### pip

```bash

pip install azure-ai-projects azure-identity openai

```

##### App

```bash

cat<<EOF>> app.py
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential


question = input("Question: ")

project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

with project.get_openai_client() as client:
    response = client.responses.create(
        model=os.environ["FOUNDRY_DEPLOYMENT"],
        input=question,
    )

    print(response.output_text)
EOF

```

##### Run 

```bash

python3 app.py

```

### With Agent

#### Code

```bash

cat<<EOF>> app_agent.py
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

question = input("Question: ")

project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

openai = project.get_openai_client()

response = openai.responses.create(
    input=question,
    extra_body={
        "agent_reference": {
            "name": os.environ["FOUNDRY_AGENT_NAME"],
            "type": "agent_reference",
        }
    },
)

print(response.output_text)
EOF

```

#### Run

```bash

python3 app_agent.py

```