import os
import re
import json
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
deployment = os.environ["FOUNDRY_DEPLOYMENT"]

def main():
    try:
        with(DefaultAzureCredential() as credential, AIProjectClient(endpoint=project_endpoint,credential=credential) as project_client):
            openai_client = project_client.get_openai_client()
            print("Connected...")

            ## User input and return response (web search)

            user_input = input("Input: ")


            tools = []
            tools_pattern = "(?<=\\().*?(?=\\)$)"
            match = re.search(tools_pattern,user_input)
            if match:
                print("yes")
                tools_string = match.group()
                tools_array = tools_string.split(",")
                if "web" in tools_array:
                    tools.append({ "type" : "web_search" })

            response = openai_client.responses.create(model=deployment,input=user_input, tools=tools)
            ## print(response.output_text)
            ## print(response.model_dump_json(indent=2))
            print(response.output_text)
            print(f"Usage input: {response.usage.input_tokens} output: {response.usage.output_tokens} total: {response.usage.total_tokens}")
    except Exception as ex:
        print(f"Error: {ex}")
if __name__ == "__main__":
    main()

