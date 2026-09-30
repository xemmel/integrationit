from pathlib import Path
import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

client = project_client.get_openai_client()


def create_vector_store(client, folder_name: str) -> str:

    vector_store = client.vector_stores.create(
        name=Path(folder_name).name
    )

    folder = Path(folder_name)

    for file_path in folder.rglob("*"):

        if not file_path.is_file():
            continue

        print(f"Uploading: {file_path}")

        with file_path.open("rb") as f:
            client.vector_stores.files.upload_and_poll(
                vector_store_id=vector_store.id,
                file=f
            )

    return vector_store.id