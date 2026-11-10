import os
import json
from tools import create_file, create_support_case, update_support_case, create_file_tool, create_support_case_tool,update_support_case_tool
from argparse import ArgumentParser
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from common import get_project_client

argparser = ArgumentParser()

argparser.add_argument("--conversationid")
argparser.add_argument("--instructions")

argparser.add_argument("--agent")
argparser.add_argument("--websearch", action="store_true")
argparser.add_argument("--customtools", action="store_true")


args = argparser.parse_args()

conversationid = args.conversationid
instructions = args.instructions or "You are a normal polite chat bot"
##model = args.model or "fastcheap"
agent = args.agent
## print(instructions)




project_client = get_project_client()


client = project_client.get_openai_client(agent_name=agent)

if conversationid:
    conversation = client.conversations.retrieve(conversation_id=conversationid)
else:
    conversation = client.conversations.create()
##conversation = client.conversations.retrieve(conversation_id="conv_05e3bdea874994b800RxN9dgbo9GbHDTmh6DPIHkhEswuaNAN8")

while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        break
    current_input = user_input
    while True:
        response = client.responses.create(
                input=current_input,
                conversation=conversation.id,
                )
        
        ## breakpoint()
        tools_output = []
        function_response = None
        for item in response.output:
            item_type = item.type
            print(f"Item type: {item_type}")
            if item_type == "message":
                ## breakpoint()
                print(item.content[0].text)
            if item_type == "function_call":
                if item.status == "in_progress":
                      print("Incomplete")
                      continue
                ##breakpoint()
                function_name = item.name
                arguments = json.loads(item.arguments)
                if function_name == "create_file":
                    ## breakpoint()
                    function_response = create_file(file_name=arguments["file_name"],content=arguments["content"])
                if function_name == "create_support_case":
                                    ## breakpoint()
                                    function_response = create_support_case(employee_id=arguments["employee_id"])
                if function_name == "update_support_case":
                                    ## breakpoint()
                                    function_response = update_support_case(support_case_id=arguments["support_case_id"],content=arguments["content"])
                                    
                if function_name == "create_support":
                    print("what")   
                tools_output.append({
                                        "type" : "function_call_output",
                                        "call_id" : item.call_id,
                                        "output" : function_response
                                    })
        if tools_output:
            ## Require Round-trip
            current_input = tools_output
            continue  
        break        
   
   ##  print(response.output_text)
   ##  print(f"Input tokens: {response.usage.input_tokens}")
   ##  print(f"Output tokens: {response.usage.output_tokens}")


print(f"Conversation Id: {conversation.id}")
