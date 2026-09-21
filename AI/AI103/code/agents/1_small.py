import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import argparse

credential = DefaultAzureCredential()

project_client = AIProjectClient(endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],credential=credential)

parser = argparse.ArgumentParser()
parser.add_argument("--agent")

args = parser.parse_args()

agent_name = args.agent or "mini-agent"


openai_client = project_client.get_openai_client(agent_name=agent_name)

conversation = openai_client.conversations.create()

while True:

    user_input = input("Input: ")
    if user_input.lower() == "exit":
        exit()
    response = openai_client.responses.create(
            input=user_input,
            conversation = conversation.id)
    print(response.model_dump_json(indent=2))
    for item in response.output:
        item_type = item.type
        if item_type == "message":
            print(item.content[0].text)
        if item_type == "function_call":
            function_name = item.name
            call_id = item.call_id
            print(f"Call function: {function_name} call_id: {call_id} arg: {item.arguments}")

