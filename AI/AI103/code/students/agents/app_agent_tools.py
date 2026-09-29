import os
import json
import uuid
from pathlib import Path
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import argparse

from common_file_tools import create_file, file_tools
from common_support_tools import create_support_case, update_support_case, support_tools
from common_employee_tools import get_employees, employee_tools, get_employee_maternity_rules


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

    response = client.responses.create(
        input=user_input,
        conversation=conversation.id
    )
    while True:
        tools_output = []
        for item in response.output:
            print(f"I got an output object of type: {item.type}")
            if item.type == "message":
                print(response.output_text)
            if item.type == "function_call":
                ## Require a round-trip
                function_name = item.name
                arguments = json.loads(item.arguments)
                print(f"I need to call this function: {function_name}")
                if function_name == "create_file":
                    output = create_file(
                        fileName=arguments["fileName"],
                        content=arguments["content"])
                    tools_output.append(
                        {
                            "type" : "function_call_output",
                            "call_id" : item.call_id,
                            "output" : output
                        }
                    )
                if function_name == "create_support_case":
                    output = create_support_case(emp_id=arguments["emp_id"])
                    tools_output.append(
                        {
                            "type" : "function_call_output",
                            "call_id" : item.call_id,
                            "output" : output
                        }
                    )
                if function_name == "update_support_case":
                    output = update_support_case(
                            case_id=arguments["case_id"],
                            content=arguments["content"])
                    tools_output.append(
                        {
                            "type" : "function_call_output",
                            "call_id" : item.call_id,
                            "output" : output
                        }
                    )                    
                if function_name == "get_employees":
                    output = get_employees()
                    tools_output.append(
                        {
                            "type" : "function_call_output",
                            "call_id" : item.call_id,
                            "output" : json.dumps(output)
                        }
                    )    
                if function_name == "get_employee_maternity_rules":
                                    output = get_employee_maternity_rules()
                                    tools_output.append(
                                        {
                                            "type" : "function_call_output",
                                            "call_id" : item.call_id,
                                            "output" : output
                                        }
                                    )    
                ## Round trip!!
        if tools_output:
            response = client.responses.create(
                input=tools_output,
                conversation=conversation.id
            )
            continue  
        break


