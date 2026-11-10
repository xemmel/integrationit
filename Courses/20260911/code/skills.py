from argparse import ArgumentParser
from common import get_project_client
from azure.ai.projects.models import CreateSkillVersionFromFilesBody
from pathlib import Path

argparser = ArgumentParser()


argparser.add_argument("--list", action="store_true")
argparser.add_argument("--name")


args = argparser.parse_args()

project_client = get_project_client()

if args.list:
    for skill in project_client.beta.skills.list():
        print(f"Skill: {skill.name} id: {skill.id} version: {skill.latest_version}")
    exit()

### Create skill

folder = Path("./skills")

files = []

for path in folder.rglob("*"):
    if path.is_file():
        files.append((path.relative_to(folder).as_posix(),
                      path.read_bytes())
                      )


skill = project_client.beta.skills.create_from_files(
    name=args.name,
    content=CreateSkillVersionFromFilesBody(files=files)
    )

print(f"Skill: {args.name} created. Id: {skill.id}  skill_id: {skill.skill_id}")