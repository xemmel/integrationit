import os
import json
from tools import create_local_file_tool, create_support_case_tool,update_support_case_tool
from argparse import ArgumentParser
from common import get_project_client
from azure.ai.projects.models import (
    PromptAgentDefinition, 
    SkillReference, 
    MicrosoftCopilotHarness, 
    FileSearchTool,
    MCPTool
    )



argparser = ArgumentParser()

argparser.add_argument("--model")
argparser.add_argument("--list", action="store_true")
argparser.add_argument("--delete", action="store_true")
argparser.add_argument("--agent_name")
argparser.add_argument("--websearch", action="store_true")
argparser.add_argument("--instructions")
argparser.add_argument("--customtools", action="store_true")
argparser.add_argument("--skill_name")
argparser.add_argument("--skill_version")
argparser.add_argument("--vector_store_id")
argparser.add_argument("--mcp_url")



args = argparser.parse_args()

model = args.model
agent_name = args.agent_name
instuctions = args.instructions

project_client = get_project_client()

if args.delete:
    project_client.agents.delete(agent_name=agent_name,force=True)
    print(f"Agent: {agent_name} deleted..")
    exit()

if args.list:
    for agent in project_client.agents.list():
        print(f"Agent: {agent.name}")
    exit()    

tools = []
skills = []
if args.websearch:
    print("adding web_search")
    tools.append({ "type" : "web_search" })
if args.customtools:
    print("adding custom_tools")
    tools.append(create_local_file_tool)
    tools.append(create_support_case_tool)
    tools.append(update_support_case_tool)
if args.skill_name:
    print(f"adding skills {args.skill_name}")
    skills.append(SkillReference(name=args.skill_name,version=args.skill_version))

if args.vector_store_id:
    print(f"adding vector store: {args.vector_store_id}")
    tools.append(FileSearchTool(vector_store_ids=[ args.vector_store_id ]))

if args.mcp_url:
    print(f"adding mcp server: {args.mcp_url}")
    mcp_tool = MCPTool(
        server_label="my-mcp",
        server_url=args.mcp_url,
        require_approval="never"
    )
    tools.append(mcp_tool)



agent = project_client.agents.create_version(
    agent_name=agent_name,
    definition=PromptAgentDefinition(
        model=model,
        instructions=instuctions,
        tools=tools,
        ##harness=MicrosoftCopilotHarness(),
        ##skills=skills
        ))

print(f"Agent: {agent_name} created with version: {agent.version}")