import os
import re 

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient 

def main():
    try:
        project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
        with(DefaultAzureCredential() as credential, 
             AIProjectClient(endpoint=project_endpoint,credential=credential) as project_client):
            print("Connected..")
            tools_pattern = "(?<=\\().*?(?=\\))"

            user_input = input("Input: ")
            deployment = os.environ["FOUNDRY_DEPLOYMENT"]
            tools = []
            match = re.search(tools_pattern,user_input)
            if match:
                print("tools found")
                tools_array = [x.strip() for x in match.group().split(",")]
                if "web" in tools_array:
                    print("Appending web_search")
                    tools.append({ "type" : "web_search"})
                if "mini" in tools_array:
                    print("Changing to mini model")
                    deployment = os.environ["FOUNDRY_DEPLOYMENT_MINI"]
                user_input = re.sub(r"\s*\([^)]*\)\s*$", "", user_input)
                print(f"new user input: {user_input}")
            openai_client = project_client.get_openai_client()
            print(f"using deployment: {deployment}")
            response = openai_client.responses.create(model=deployment,input=user_input, tools=tools)
            print(response.output_text)
            print()
            print(f"Input tokens: {response.usage.input_tokens}")
            print(f"Output tokens: {response.usage.output_tokens}")
            print(f"Total tokens: {response.usage.total_tokens}")


    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()