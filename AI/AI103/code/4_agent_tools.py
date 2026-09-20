import os
import json
import argparse
from common.common_file_tools import save_file,common_file_tools
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]

def main():
    try:
        
        parser = argparse.ArgumentParser()
        parser.add_argument("--mode")
        parser.add_argument("--instructions")
        parser.add_argument("--agent")
        parser.add_argument("--deployment")
        args = parser.parse_args()

        tools = [ *common_file_tools ]

        with(DefaultAzureCredential() as credential, AIProjectClient(endpoint=project_endpoint,credential=credential) as project_client):
            
            print("Connected...")
            agent_name = args.agent


            
            if args.mode.lower() == "delete_agent":
                project_client.agents.delete(agent_name=agent_name)
                print(f"Agent: {agent_name} deleted..")
                exit()

            if args.mode.lower() == "create_agent":
                print(f"Creating agent: {agent_name}")
                instructions = args.instructions
                deployment=args.deployment
                agent = project_client.agents.create_version(
                    agent_name=agent_name,
                    definition=PromptAgentDefinition(
                        model=deployment,
                        instructions=instructions,
                        tools=tools
                    )

                )
                print(f"Agent created..")

                exit()

            if args.mode.lower() == "list_agents":
                print("agents:")
                print()
                for agent in project_client.agents.list():
                    print(f"agent: {agent.name} id: {agent.id}")
                    for version in project_client.agents.list_versions(agent_name=agent.name):
                        print(f"\tVersion: {version.versionc}")
                exit()


    except Exception as ex:
        print(f"Error: {ex}")
if __name__ == "__main__":
    main()

