import os
import argparse

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential


argparser = argparse.ArgumentParser()
argparser.add_argument("--agentname")

args = argparser.parse_args()





project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

openai_client = project_client.get_openai_client(agent_name=args.agentname)

conversation = openai_client.conversations.create()

while True:
    user_input = input("Input (exit): ")
    if user_input.lower() == "exit":
        break;
    response = openai_client.responses.create(
        input=user_input,
        conversation=conversation.id,
        
    )
    print(response.output_text)

