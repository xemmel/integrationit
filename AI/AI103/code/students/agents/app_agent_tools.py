import os
import json
import uuid
from pathlib import Path
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import argparse

from common_file_tools import file_functions
from common_support_tools import support_functions
from common_employee_tools import employee_functions


FUNCTIONS = {
    **file_functions,
    **employee_functions,
    **support_functions
}

parser = argparse.ArgumentParser()
parser.add_argument("--agent")

args = parser.parse_args()

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
agent_name = args.agent or "standard"

credential = DefaultAzureCredential()

project_client = AIProjectClient(endpoint=project_endpoint,credential=credential)

client = project_client.get_openai_client(agent_name=agent_name)
## client = project_client.get_openai_client()
conversation = client.conversations.create()

while True:

    user_input = input("Input: ")
    if user_input.lower() == "exit":
        break


    while True:
        response = client.responses.create(
        input=user_input,
        conversation=conversation.id
        )
        tools_output = []
        for item in response.output:
            print(f"I got an output object of type: {item.type}")
            if item.type == "message":
                print(response.output_text)
            if item.type == "function_call":
              function = FUNCTIONS[item.name]
              arguments = json.loads(item.arguments)

              output = function(**arguments)
              if not isinstance(output, str):
                output = json.dumps(output)
              tools_output.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": output
                })
        if tools_output:
            user_input=tools_output
            continue  
        break


