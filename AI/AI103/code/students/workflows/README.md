## Init

```powershell

pip install agent-framework-foundry

```

### Code

```python

import os

from azure.identity import DefaultAzureCredential
from agent_framework.foundry import FoundryAgent
from agent_framework.orchestrations import SequentialBuilder
from agent_framework_foundry_hosting import ResponsesHostServer


def create_workflow_agent():

    credential = DefaultAzureCredential()
    endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]

    # Existing Foundry Prompt Agent.
    # Model, instructions, hosted tools, MCP, RAG etc.
    # remain configured on the existing Foundry agent.
    math_agent = FoundryAgent(
        project_endpoint=endpoint,
        agent_name="agent-a2a-math",
        credential=credential,
    )

    # Existing Foundry Prompt Agent.
    validator_agent = FoundryAgent(
        project_endpoint=endpoint,
        agent_name="agent-validator",
        credential=credential,
    )

    # Deterministic:
    #
    # input -> math -> validator -> result
    workflow = SequentialBuilder(
        participants=[
            math_agent,
            validator_agent,
        ]
    ).build()

    # Expose the entire workflow as one agent.
    return workflow.as_agent(
        name="math-validator-workflow"
    )


server = ResponsesHostServer(
    agent=create_workflow_agent
)

server.run()

```