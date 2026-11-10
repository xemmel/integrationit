from argparse import ArgumentParser
from common import get_project_client
from azure.ai.projects.models import CreateSkillVersionFromFilesBody
from pathlib import Path

argparser = ArgumentParser()


argparser.add_argument("--list", action="store_true")
argparser.add_argument("--name")


args = argparser.parse_args()

project_client = get_project_client()
client = project_client.get_openai_client()

if args.list:
    for vector_store in client.vector_stores.list():
        print(f"Vector store: {vector_store.name} id: {vector_store.id}")
    exit()


### Create vector store

vector_store = client.vector_stores.create(
    name=args.name
)

folder = Path("./skills")

for file in folder.rglob("*"):
    if not file.is_file():
        continue
    print(f"Uploading: {file}")
    with file.open("rb") as f:
        client.vector_stores.files.upload_and_poll(vector_store_id=vector_store.id,file=f)

print(f"Vector store: {args.name} with id: {vector_store.id} created..")
