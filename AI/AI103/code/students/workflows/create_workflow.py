import os
import argparse
import hashlib
import zipfile
from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    CodeConfiguration,
    CodeDependencyResolution,
    HostedAgentDefinition,
    ProtocolVersionRecord,
)


parser = argparse.ArgumentParser()
parser.add_argument("--agent1", required=True)
parser.add_argument("--agent2", required=True)
args = parser.parse_args()

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]

hosted_agent_name = "math-validator-workflow"

base_dir = Path(__file__).parent
zip_path = base_dir / "workflow.zip"


# Package the code that Foundry will execute.
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(base_dir / "main.py", "main.py")
    z.write(base_dir / "requirements.txt", "requirements.txt")


code_bytes = zip_path.read_bytes()
code_sha256 = hashlib.sha256(code_bytes).hexdigest()


credential = DefaultAzureCredential()

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=credential,
)


created = project_client.agents.create_version_from_code(
    agent_name=hosted_agent_name,

    definition=HostedAgentDefinition(
        cpu="0.5",
        memory="1Gi",

        code_configuration=CodeConfiguration(
            runtime="python_3_14",
            entry_point=["python", "main.py"],
            dependency_resolution=CodeDependencyResolution.REMOTE_BUILD,
        ),

        protocol_versions=[
            ProtocolVersionRecord(
                protocol="responses",
                version="2.0.0",
            )
        ],

        environment_variables={
            "FOUNDRY_PROJECT_ENDPOINT": endpoint,
            "AGENT1": args.agent1,
            "AGENT2": args.agent2,
        },
    ),

    code=(
        zip_path.name,
        code_bytes,
        "application/zip",
    ),

    code_zip_sha256=code_sha256,

    description="Sequential Agent Framework workflow",
)


print(f"Created hosted workflow: {hosted_agent_name}")
print(f"Version: {created.version}")
print(f"Agent 1: {args.agent1}")
print(f"Agent 2: {args.agent2}")