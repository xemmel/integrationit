import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    A2AProtocolVersion,
    A2ATool,
    PromptAgentDefinition,
)
import argparse


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--deployment")
arg_parser.add_argument("--a2aconnection")
arg_parser.add_argument("--name")

args = arg_parser.parse_args()

deployment = args.deployment
a2a_connection = args.a2aconnection
agent_name = args.name


project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

# Get the Foundry connection pointing at A1
connection = project.connections.get(a2a_connection)

# Turn A1 into a tool that A2 can call
amath = A2ATool(
    a2a_version=A2AProtocolVersion.V1_0,
    project_connection_id=connection.id,
)

agent = project.agents.create_version(
    agent_name=agent_name,
    definition=PromptAgentDefinition(
        model=deployment,
    instructions="""
You are Agent A2, a manager agent.

You MUST NOT solve mathematical questions yourself.

For ANY question involving mathematics, arithmetic, numbers,
calculations, equations, or mathematical reasoning:

1. ALWAYS call the available A2A agent.
2. Send the user's mathematical question to that agent unchanged.
3. Return the answer received from that agent.
4. NEVER calculate or correct the answer yourself.

This rule applies even to extremely simple questions such as 1+1.
""",
        tools=[amath],
    ),
)

print(f"Created: {agent.name} version {agent.version}")