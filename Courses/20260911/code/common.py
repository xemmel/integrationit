import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

def get_project_client():
    credential = DefaultAzureCredential()
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
    project_client = AIProjectClient(endpoint=project_endpoint,credential=credential, allow_preview=True)
    return project_client
