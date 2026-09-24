import os
import json
import argparse
from common.common_file_tools import save_file,common_file_tools
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]

def main():
    try:
        
        parser = argparse.ArgumentParser()
        parser.add_argument("--agent")
        args = parser.parse_args()

        with(DefaultAzureCredential() as credential, AIProjectClient(endpoint=project_endpoint,credential=credential) as project_client):
            print("Connected...")
            agent_name = args.agent

            openai_client = project_client.get_openai_client(agent_name=agent_name)
            
         
            conversation = openai_client.conversations.create()
            while True:
                ### New User interaction
                user_input = input("Input (exit): ")
                if user_input.lower() == "exit":
                    exit()
                response = openai_client.responses.create(
                    conversation=conversation.id,
                    input=user_input
                )
                while True:
                    tools_output = []
                    for item in response.output:
                        print(item.type)
                        if item.type == "message":
                            print(item.content[0].text)
                        if item.type == "function_call":
                            function_name = item.name
                            print(f"I should call the local function: {function_name}")
                            arguments = json.loads(item.arguments)
                            if function_name == "save_file":
                                output = save_file(
                                        fileName=arguments["fileName"],
                                        content=arguments["content"])
                                
                            tools_output.append({
                                "type" : "function_call_output",
                                "call_id" : item.call_id,
                                "output" : output
                            })
                    if tools_output:
                        user_input = tools_output
                        continue   
                    break
                
                

    except Exception as ex:
        print(f"Error: {ex}")
if __name__ == "__main__":
    main()

