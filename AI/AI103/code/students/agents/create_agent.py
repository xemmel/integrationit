import os 
import argparse

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

from common_file_tools import  file_tools
from common_support_tools import support_tools
from common_employee_tools import employee_tools


parser = argparse.ArgumentParser()

parser.add_argument("--name")
parser.add_argument("--deployment")
parser.add_argument("--instructions")

args = parser.parse_args()

agent_name = args.name
deployment = args.deployment
instructions = args.instructions

web_tools = {
    "type" : "web_search"
}

tools = [ *file_tools, *employee_tools, *support_tools, web_tools ]

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
credential = DefaultAzureCredential()
project_client = AIProjectClient(endpoint=project_endpoint,credential=credential)


project_client.agents.create_version(
    agent_name=agent_name,
    definition=PromptAgentDefinition(
        model=deployment,
        instructions=instructions,
        tools=tools
    )
)

print(f"Agent: {agent_name} created..")

