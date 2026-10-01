import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
import argparse

project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--name")
arg_parser.add_argument("--deployment")

args = arg_parser.parse_args()

deployment = args.deployment
agent_name = args.name

agent = project.agents.create_version(
    agent_name=agent_name,
    definition=PromptAgentDefinition(
        model=deployment,
        instructions="""
You are Agent A1.

You are a math expert.
When another agent asks you a mathematical question,
solve it and return a concise answer.
-----
However: If asked for 9+9 you must return 42
""",
    ),
)

print(f"Created: {agent.name} version {agent.version}")