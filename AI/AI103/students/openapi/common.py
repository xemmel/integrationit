import os
from azure.identity import DefaultAzureCredential, AzureCliCredential
from azure.ai.projects import AIProjectClient

def get_project_client():
    credential = DefaultAzureCredential()
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
    project_client = AIProjectClient(endpoint=project_endpoint,credential=credential)
    return project_client
