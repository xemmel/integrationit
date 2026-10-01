import os

from azure.identity import DefaultAzureCredential
from agent_framework.foundry import FoundryAgent
from agent_framework.orchestrations import SequentialBuilder
from agent_framework_foundry_hosting import ResponsesHostServer


credential = DefaultAzureCredential()
endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]

agent1_name = os.environ["AGENT1"]
agent2_name = os.environ["AGENT2"]


agent1 = FoundryAgent(
    project_endpoint=endpoint,
    agent_name=agent1_name,
    credential=credential,
)

agent2 = FoundryAgent(
    project_endpoint=endpoint,
    agent_name=agent2_name,
    credential=credential,
)


workflow = SequentialBuilder(
    participants=[
        agent1,
        agent2,
    ]
).build()


workflow_agent = workflow.as_agent(
    name="math-validator-workflow"
)


server = ResponsesHostServer(
    agent=workflow_agent,
    history_source="agent",
)


server.run()