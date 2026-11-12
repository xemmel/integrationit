from argparse import ArgumentParser
import os
import re
from pathlib import Path
from uuid import uuid4


import yaml
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    CreateSkillVersionFromFilesBody,
    MicrosoftCopilotHarness,
    PromptAgentDefinition,
    SkillReference,
)

argparser = ArgumentParser()

argparser.add_argument("--list",action="store_true")
argparser.add_argument("--createagent",action="store_true")


args = argparser.parse_args()

from azure.identity import DefaultAzureCredential

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]

project_client = AIProjectClient(endpoint=project_endpoint,credential=DefaultAzureCredential())

if args.list:
    for skill in project_client.beta.skills.list():
        print(f"Skill: {skill.name}")
    exit()


if args.createagent:
    print("Creating agent agentfinalskill")
    agent = project_client.agents.create_version(
        agent_name="agentfinalskill",
        definition=PromptAgentDefinition(
            model="large",
            harness=MicrosoftCopilotHarness(),
            skills=[
                SkillReference(name="finalskills",version="5")
            ]
        ),
        headers={ "Foundry-Features" : "Skills=V1Preview,MicrosoftCopilot=V1Preview" }
    )
    print(f"Agent {agent.name} created with version: {agent.version}")
    exit()

folder = Path("./data")

files = []

for path in folder.rglob("*"):
    if path.is_file():
        files.append((path.relative_to(folder).as_posix(),path.read_bytes()))



skill = project_client.beta.skills.create_from_files(
    name="finalskills",
    content=CreateSkillVersionFromFilesBody(
        files=files,
    ),
    headers={
        "Foundry-Features": "Skills=V1Preview",
    },
)

print(f"Skill: {skill.name} created with version: {skill.version}")