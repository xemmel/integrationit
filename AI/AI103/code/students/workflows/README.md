## Init

```powershell

pip install agent-framework-foundry

```

### Agents in workflow

> agent-work-1

```
You give math results and always returns both q and a

4+5=9 for instance
-------------------------
when asked about 9+9 you answer "9+9=42"
```

> agent-work-2

```
You are a math validator. If the math you see as input is correct you return the result

9+9 = 18   You return: 18
-----

If wrong: 9+9=10   You return: NO NO NO

```


```powershell

pip install agent_framework.foundry
pip install agent_framework_orchestrations
pip install agent_framework_foundry_hosting


```
### Code


#### In-process

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


#### Hosted

```python

import os

from azure.identity import DefaultAzureCredential
from agent_framework.foundry import FoundryAgent
from agent_framework.orchestrations import SequentialBuilder
from agent_framework_foundry_hosting import FoundryWorkflowHost


credential = DefaultAzureCredential()
endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]


math_agent = FoundryAgent(
    project_endpoint=endpoint,
    agent_name="agent-a2a-math",
    credential=credential,
)

validator_agent = FoundryAgent(
    project_endpoint=endpoint,
    agent_name="agent-validator",
    credential=credential,
)


workflow = SequentialBuilder(
    participants=[
        math_agent,
        validator_agent,
    ]
).build()


host = FoundryWorkflowHost(
    project_endpoint=endpoint,
    credential=credential,
)


host.publish(
    workflow=workflow,
    name="math-validator-workflow",
)

```