import argparse
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
from azure.identity import DefaultAzureCredential


def load_skills(root: Path):
    """Read each skill folder, including all supporting files."""

    if not root.is_dir():
        raise ValueError(f"Skills directory does not exist: {root}")

    packages = []
    names = set()

    for folder in sorted(p for p in root.iterdir() if p.is_dir()):
        if folder.name.startswith("."):
            continue

        document = folder / "SKILL.md"

        if not document.is_file():
            raise ValueError(f"Missing {document}")

        text = document.read_text(encoding="utf-8-sig")

        match = re.match(
            r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z",
            text,
            re.S,
        )

        if not match:
            raise ValueError(
                f"{document}: expected YAML front matter and a body"
            )

        metadata = yaml.safe_load(match.group(1))

        if not isinstance(metadata, dict):
            raise ValueError(f"{document}: front matter must be a mapping")

        name = metadata.get("name")
        description = metadata.get("description")

        if (
            not isinstance(name, str)
            or not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", name)
            or len(name) > 64
            or "--" in name
        ):
            raise ValueError(f"{document}: invalid skill name")

        if (
            not isinstance(description, str)
            or not 1 <= len(description.strip()) <= 1024
        ):
            raise ValueError(
                f"{document}: description is required (max 1024 characters)"
            )

        if not match.group(2).strip():
            raise ValueError(f"{document}: skill instructions are empty")

        if name in names:
            raise ValueError(f"Duplicate skill name: {name}")

        names.add(name)

        files = []

        for path in sorted(folder.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Symlinks are not supported: {path}")

            if path.is_file():
                files.append((
                    path.relative_to(folder).as_posix(),
                    path.read_bytes(),
                ))

        packages.append((name, files))

    if not packages:
        raise ValueError(f"No skill folders found in {root}")

    return packages


def main():
    parser = argparse.ArgumentParser(
        description="Create a Foundry agent with skills from local folders."
    )

    parser.add_argument(
        "--endpoint",
        default=os.getenv("FOUNDRY_PROJECT_ENDPOINT"),
    )
    parser.add_argument(
        "--model",
        default=os.getenv("FOUNDRY_MODEL_DEPLOYMENT_NAME", "mini5"),
    )
    parser.add_argument(
        "--agent-name",
        default=f"skills-agent-{uuid4().hex[:8]}",
    )
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=Path(__file__).parent / "skills",
    )
    parser.add_argument(
        "--prompt",
        help="Optional prompt to test the agent",
    )

    args = parser.parse_args()

    if not args.endpoint:
        parser.error("Set FOUNDRY_PROJECT_ENDPOINT or pass --endpoint")

    try:
        packages = load_skills(args.skills_dir.resolve())
    except (ValueError, OSError, yaml.YAMLError) as error:
        parser.error(str(error))

    with (
        DefaultAzureCredential() as credential,
        AIProjectClient(
            endpoint=args.endpoint,
            credential=credential,
            allow_preview=True,
        ) as project_client,
    ):
        references = []

        # Upload each skill folder as a new skill version.
        for name, files in packages:
            skill = project_client.beta.skills.create_from_files(
                name=name,
                content=CreateSkillVersionFromFilesBody(
                    files=files,
                ),
                headers={
                    "Foundry-Features": "Skills=V1Preview",
                },
            )

            references.append(
                SkillReference(
                    name=skill.name,
                    version=skill.version,
                )
            )

            print(f"Uploaded skill: {skill.name}, version: {skill.version}")

        # Attach the skills to a prompt agent using the Copilot harness.
        agent = project_client.agents.create_version(
            agent_name=args.agent_name,
            definition=PromptAgentDefinition(
                model=args.model,
                instructions="Use the relevant attached skills to help the user.",
                harness=MicrosoftCopilotHarness(),
                skills=references,
            ),
            headers={
                "Foundry-Features": (
                    "Skills=V1Preview,MicrosoftCopilot=V1Preview"
                ),
            },
        )

        print(f"Created agent: {agent.name}, version: {agent.version}")

        # Optionally test using an agent-scoped client and a conversation.
        if args.prompt:
            with project_client.get_openai_client(
                agent_name=agent.name,
            ) as client:
                conversation = client.conversations.create()

                response = client.responses.create(
                    conversation=conversation.id,
                    input=args.prompt,
                )

                print(response.output_text)

                if response.status != "completed":
                    raise RuntimeError(
                        f"Response did not complete: {response.status}"
                    )


if __name__ == "__main__":
    main()