import os
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
            tools = [
                {
                    "type" : "web_search"
                }
            ]
            user_input = input("Input: ")
            response = openai_client.responses.create(model=deployment,input=user_input)
            ## print(response.output_text)
            ## print(response.model_dump_json(indent=2))
            print(response.output_text)
            print(f"Usage input: {response.usage.input_tokens} output: {response.usage.output_tokens} total: {response.usage.total_tokens}")
    except Exception as ex:
        print(f"Error: {ex}")
if __name__ == "__main__":
    main()

