import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
deployment = os.environ["FOUNDRY_DEPLOYMENT"]

def main():
    try:
        with(DefaultAzureCredential() as credential, AIProjectClient(endpoint=project_endpoint,credential=credential) as project_client):
            openai_client = project_client.get_openai_client()
            print("Connected...")
    except Exception as ex:
        print(f"Error: {ex}")
if __name__ == "__main__":
    main()

