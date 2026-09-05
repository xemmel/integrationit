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

#### venv

```bash

python3 -m venv devenv

source devenv/bin/activate


```

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

### MCP

#### pip

```bash

pip install mcp

```


#### Server

```bash

cat<<EOF>> mcp_server.py
import sys
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("my-first-mcp")


@mcp.tool()
def say_hello(name: str) -> str:
    """Say hello to somebody."""

    print(f">>> MCP TOOL CALLED: {name}", file=sys.stderr)

    return f"Hello {name}!"


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        stateless_http=True,
        json_response=True,
    )
EOF


```

##### Run Server

```bash

python3 mcp_server.py

```

##### Container Server

###### Create files
```bash

rm -f mcp_requirements.txt
rm -f Dockerfile

cat<<EOF>> mcp_requirements.txt
mcp
EOF

cat<<EOF>> Dockerfile
FROM python:3.14-slim

WORKDIR /app

COPY mcp_requirements.txt .
RUN pip install --no-cache-dir -r mcp_requirements.txt

COPY mcp_server.py .

EXPOSE 8000

CMD ["python", "mcp_server.py"]
EOF


```

###### build image

```bash

docker buildx build --tag mcpserver:1.0 .


```

###### Run container

```bash

docker run --publish 7777:8000 --name mcpserver -d mcpserver:1.0


```

#### Client

```bash

cat<<EOF>> mcp_client_app.py
import asyncio
import json
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from mcp import Client
from mcp.types import TextContent


async def main():
    question = input("Question: ")

    # Azure Foundry / OpenAI client
    project = AIProjectClient(
        endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
        credential=DefaultAzureCredential(),
    )

    openai = project.get_openai_client()

    # LOCAL MCP server
    async with Client("http://localhost:8000/mcp") as mcp:

        # 1. Discover MCP tools
        discovered = await mcp.list_tools()

        # 2. Convert MCP tools -> OpenAI function tools
        tools = []

        for tool in discovered.tools:
            print(f"Found MCP tool: {tool.name}")

            tools.append({
                "type": "function",
                "name": tool.name,
                "description": tool.description or "",
                "parameters": tool.input_schema,
            })

        # 3. Ask the model
        response = openai.responses.create(
            model=os.environ["FOUNDRY_DEPLOYMENT"],
            input=question,
            tools=tools,
        )

        # 4. See whether the LLM requested any tool calls
        while True:

            calls = [
                item
                for item in response.output
                if item.type == "function_call"
            ]

            if not calls:
                print(response.output_text)
                return

            tool_outputs = []

            for call in calls:
                arguments = json.loads(call.arguments)

                print(
                    f">>> LLM REQUESTED MCP TOOL: "
                    f"{call.name}({arguments})"
                )

                # 5. Execute locally via MCP
                result = await mcp.call_tool(
                    call.name,
                    arguments,
                )

                # MCP result -> text for the model
                text = "\n".join(
                    block.text
                    for block in result.content
                    if isinstance(block, TextContent)
                )

                tool_outputs.append({
                    "type": "function_call_output",
                    "call_id": call.call_id,
                    "output": text,
                })

            # 6. Give results back to LLM
            response = openai.responses.create(
                model=os.environ["FOUNDRY_DEPLOYMENT"],
                previous_response_id=response.id,
                input=tool_outputs,
                tools=tools,
            )


asyncio.run(main())
EOF


```

##### Change port if container

```bash

sed 's/8000/7777/g' mcp_client_app.py -i

```

##### Run client

```bash

python3 mcp_client_app.py

```

###### Log mcp server container

```bash

docker logs mcpserver -f

```



#### Extended mcp server

```python

import sys
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("my-first-mcp")


@mcp.tool()
def save_file(content: str, fileName: str) -> str:
    """Create File"""


    with open(fileName, "w", encoding="utf-8") as f:
        f.write(content)

    print(f">>> File created '{fileName}'\nContent: {content}")

    return f"File created.."

@mcp.tool()
def create_support_case(description: str) -> str:
    """Create support case"""

    print(f">>> Support case created: '{description}'")

    return f"Support case created.."

@mcp.tool()
def say_hello(name: str) -> str:
    """Say hello to somebody."""

    print(f">>> MCP TOOL CALLED: {name}", file=sys.stderr)
    print(f">>> HELLO: {name}", file=sys.stderr)

    return f"Hello {name}!"


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        stateless_http=True,
        json_response=True,
    )

```