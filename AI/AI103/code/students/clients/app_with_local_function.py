import os
import argparse
import json
from local_functions import query_sql, local_function_tools

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
deployment = os.environ["FOUNDRY_MODEL"]

tools = [ *local_function_tools ]

with(DefaultAzureCredential() as credential, AIProjectClient(endpoint=project_endpoint, credential=credential) as project_client):
    openai_client = project_client.get_openai_client()

    conversation = openai_client.conversations.create()
    while True:
        user_input = input("Input: ")
        if user_input.lower() == "exit":
            break

        input_data = user_input
        while True:
            response = openai_client.responses.create(
                model=deployment,
                input=input_data,
                conversation=conversation.id,
                tools=tools
            )
            output = None
            output_array = []
            for item in response.output:
                if item.type == "message":
                    print(item.content[0].text)
                if item.type == "function_call":
                    print(f"Function call: {item.name}")
                    arguments = json.loads(item.arguments)
                    if item.name == "query_sql":
                        output = query_sql(query=arguments["query"])
                    if output:
                        output_array.append({
                            "type" : "function_call_output",
                            "call_id" : item.call_id,
                            "output" : str(output)
                        })
                        input_data = output_array
            if output_array:
                input_data = output_array
                continue
            break
