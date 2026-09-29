import os
import json
import uuid
from pathlib import Path
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


def create_file(fileName: str, content: str) -> str:
    ## Implement create local file logic
    folder = Path("sandbox")
    folder.mkdir(parents=True, exist_ok=True)
    
    fullName = Path("sandbox") / fileName
    fullName.write_text(content,encoding="utf-8")
    print(f"-- create_file executed with fileName: {fileName}")
    return "success"

def create_support_case(emp_id: str) -> str:
    case_id = str(uuid.uuid4())
    print(f"-- create_support_case executed with case_id: {case_id} for emp_id: {emp_id}")    
    return case_id

def update_support_case(case_id: str, content: str) -> str:
    print(f"-- update_support_case executed with case_id: {case_id} content: '{content}'")
    return "updated"

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
deployment = os.environ["FOUNDRY_DEPLOYMENT"]

tools = [
    {
        "type" : "function",
        "name" : "create_file",
        "description" : """
            Creates a local file
            -------------------
            Outputs: status (success/failed)
        """,
        "parameters" : {
            "type" : "object",
            "properties" : {
                "fileName" : {
                    "type" : "string",
                    "description" : "The name of the file"
                },
                "content" : {
                    "type": "string",
                    "description" : "The file content"
                }
            },
            "required" : [ "fileName", "content"],
            "additionalProperties" : False
        }
    },
     {
            "type" : "function",
            "name" : "create_support_case",
            "description" : """
                Creates a support case for an employee
                -------------------
                Outputs: the newly created support case unique id
            """,
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "emp_id" : {
                            "type" : "string",
                            "description" : "The employee id. Format: [0-9]{4}"
                        }
                },
                "required" : [ "emp_id" ],
                "additionalProperties" : False
            }
        },
        {
                    "type" : "function",
                    "name" : "update_support_case",
                    "description" : """
                        Update an existing support case for an employee
                        -------------------
                        Outputs: updated as string
                    """,
                    "parameters" : {
                        "type" : "object",
                        "properties" : {
                            "case_id" : {
                                    "type" : "string",
                                    "description" : "The support case id"
                                },
                            "content" : {
                                    "type" : "string",
                                    "description" : "The content to be appended to the support text"
                                }
                        },
                        "required" : [ "case_id", "content" ],
                        "additionalProperties" : False
                    }
                }
]

credential = DefaultAzureCredential()

project_client = AIProjectClient(endpoint=project_endpoint,credential=credential)

## client = project_client.get_openai_client(agent_name="simple-agent")
client = project_client.get_openai_client()
conversation = client.conversations.create()

while True:

    user_input = input("Input: ")
    if user_input.lower() == "exit":
        break

    response = client.responses.create(
        model=deployment,
        input=user_input,
        instructions="You talk like a chat bot",
        conversation=conversation.id,
        tools=tools
    )
    while True:
        tools_output = []
        for item in response.output:
            print(f"I got an output object of type: {item.type}")
            if item.type == "message":
                print(response.output_text)
            if item.type == "function_call":
                ## Require a round-trip
                function_name = item.name
                arguments = json.loads(item.arguments)
                print(f"I need to call this function: {function_name}")
                if function_name == "create_file":
                    output = create_file(
                        fileName=arguments["fileName"],
                        content=arguments["content"])
                    tools_output.append(
                        {
                            "type" : "function_call_output",
                            "call_id" : item.call_id,
                            "output" : output
                        }
                    )
                if function_name == "create_support_case":
                    output = create_support_case(emp_id=arguments["emp_id"])
                    tools_output.append(
                        {
                            "type" : "function_call_output",
                            "call_id" : item.call_id,
                            "output" : output
                        }
                    )
                if function_name == "update_support_case":
                    output = update_support_case(
                            case_id=arguments["case_id"],
                            content=arguments["content"])
                    tools_output.append(
                        {
                            "type" : "function_call_output",
                            "call_id" : item.call_id,
                            "output" : output
                        }
                    )                    

                ## Round trip!!
        if tools_output:
            response = client.responses.create(
                model=deployment,
                input=tools_output,
                conversation=conversation.id,
                tools=tools
            )
            continue  
        break

    ## print(response.output_text)
    ## print(response.model_dump_json(indent=2))

    ## print(f"Input Tokens: {response.usage.input_tokens}")
    ## print(f"Output Tokens: {response.usage.output_tokens}")
    ## print(f"Total Tokens: {response.usage.total_tokens}")

