import os
import json
from tools import create_file, create_support_case, update_support_case, create_file_tool, create_support_case_tool,update_support_case_tool
from argparse import ArgumentParser
from common import get_project_client
from azure.ai.projects.models import PromptAgentDefinition



argparser = ArgumentParser()

argparser.add_argument("--model")
argparser.add_argument("--agent_name")
argparser.add_argument("--websearch", action="store_true")
argparser.add_argument("--instructions")
argparser.add_argument("--customtools", action="store_true")


args = argparser.parse_args()

model = args.model
agent_name = args.agent_name
instuctions = args.instructions

tools = []

if (args.websearch):
    print("adding web_search")
    tools.append({ "type" : "web_search" })
if (args.customtools):
    print("adding custom_tools")
    tools.append(create_file_tool)
    tools.append(create_support_case_tool)
    tools.append(update_support_case_tool)


project_client = get_project_client()

agent = project_client.agents.create_version(
    agent_name=agent_name,
    definition=PromptAgentDefinition(
        model=model,
        instructions=instuctions,
        tools=tools))

print(f"Agent: {agent_name} created with version: {agent.version}")