import os
import argparse

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential


argparser = argparse.ArgumentParser()
argparser.add_argument("--server")
args = argparser.parse_args()



MCP_SERVER = (
    args.server
)

project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

openai_client = project_client.get_openai_client()

conversation = openai_client.conversations.create()

while True:
    user_input = input("Input (exit): ")
    if user_input.lower() == "exit":
        break;
    response = openai_client.responses.create(
        model="astra6",
        input=user_input,
        conversation=conversation.id,
        tools=[
            {
                "type": "mcp",
                "server_label": "my-mcp",
                "server_url": MCP_SERVER,
                "require_approval": "never"
            }
        ]
    )
    print(response.output_text)

