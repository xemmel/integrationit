from pathlib import Path
import os
import argparse

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


parser = argparse.ArgumentParser()
parser.add_argument("--folder")

args = parser.parse_args()
folder_name = args.folder


project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

client = project_client.get_openai_client()


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

print(vector_store.id)
