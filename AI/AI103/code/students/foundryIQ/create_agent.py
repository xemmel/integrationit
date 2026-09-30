import os 
import argparse

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition, MCPTool, FileSearchTool

from common_file_tools import  file_tools
from common_support_tools import support_tools
from common_employee_tools import employee_tools


parser = argparse.ArgumentParser()

parser.add_argument("--name")
parser.add_argument("--deployment")
parser.add_argument("--instructions")
parser.add_argument("--mcpserver")
parser.add_argument("--vectorid")


args = parser.parse_args()

agent_name = args.name
deployment = args.deployment
instructions = args.instructions or "You are a chatbot"
mcp_server = args.mcpserver or None 
vector_id = args.vectorid or None 


web_search_tool = { "type" : "web_search"}
tools = [ *file_tools, *support_tools, *employee_tools ]
tools.append(web_search_tool)
if mcp_server:
    mcp_tool = MCPTool(
            server_label="test-mcp",
            server_url=mcp_server,
            require_approval="never")
    
    tools.append(mcp_tool)

if vector_id:
    file_search = FileSearchTool(
       vector_store_ids=[vector_id]
    )
    tools.append(file_search)

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
print(project_endpoint)
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

