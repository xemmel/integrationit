import argparse
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import (
    PromptAgentDefinition,
    MCPTool
)

argparser = argparse.ArgumentParser()
argparser.add_argument("--mcpserver")
argparser.add_argument("--agentname")
argparser.add_argument("--model")
argparser.add_argument("--instructions")


args = argparser.parse_args()

mcp_server = args.mcpserver
agent_name = args.agentname
model_name = args.model
instructions = args.instructions or "You are a normal chatbot using your mcp when needed"


mcp_tool = MCPTool(
    server_label="my-mcp",
    server_url=mcp_server,
    require_approval="never"
)

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]


with(DefaultAzureCredential() as credential, AIProjectClient(endpoint=project_endpoint,credential=credential) as project_client):
    agent = project_client.agents.create_version(
        agent_name = agent_name,
        definition = PromptAgentDefinition(
            model = model_name,
            instructions = instructions,
            tools = [ mcp_tool ]
        )
    )
    print (f"agent {agent_name} created...")
