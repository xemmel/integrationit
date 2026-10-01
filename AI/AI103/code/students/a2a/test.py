import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

openai_client = project_client.get_openai_client()

response = openai_client.responses.create(
    input="What is 9+9?",
    extra_body={
        "agent_reference": {
            "name": "agent-a2a-manager",
            "type": "agent_reference"
        }
    }
)

print(response.output_text)