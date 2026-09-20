import os
import json
import logging
import argparse

from common.common_file_tools import save_file, common_file_tools, get_file_content,list_files
from common.common_supportcase_tools import create_support_case, insert_support_case_text, close_support_case, common_supportcase_tools

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

total_input_tokens = 0
total_output_tokens = 0
total_cost = 0

ASTRA_INPUT_PRICE = 2.50
ASTRA_OUTPUT_PRICE = 15.00

MINI_INPUT_PRICE = 0.25
MINI_OUTPUT_PRICE = 2.00



parser = argparse.ArgumentParser()
parser.add_argument("--deployment")
args = parser.parse_args()


if args.deployment == "astra6":
    input_price = ASTRA_INPUT_PRICE
    output_price = ASTRA_OUTPUT_PRICE

if args.deployment == "mini5":
    input_price = MINI_INPUT_PRICE
    output_price = MINI_OUTPUT_PRICE


def set_tokens(input_tokens: int, output_tokens: int):
     global total_input_tokens, total_output_tokens, total_cost
     total_input_tokens += input_tokens
     total_output_tokens += output_tokens

     input_cost = input_tokens / 1_000_000 * input_price
     output_cost = output_tokens / 1_000_000 * output_price

     cost = input_cost + output_cost
     total_cost += cost
     print(f"input tokens: {input_tokens} output tokens: {output_tokens} total input tokens: {total_input_tokens} total output tokens: {total_output_tokens} total: {total_input_tokens+total_output_tokens}")
     print(f"input cost: {input_cost} output cost: {output_cost} total cost: {total_cost}")

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
    level=logging.WARN,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s"
)

    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
    deployment = args.deployment

    logger.info("deployment: %s", deployment)

    tools = [ *common_file_tools, *common_supportcase_tools, { "type" : "web_search"} ]

    print("Starting...")
    
    with (DefaultAzureCredential() as credential, AIProjectClient(endpoint=project_endpoint,credential=credential) as project_client):
        openai_client = project_client.get_openai_client()

        previous_response_id = None

        while True:
             
            user_input = input("Input (exit to exit): ")
            if user_input.lower() == "exit":
                 exit()
            request = {
                 "model" : deployment,
                 "input" : user_input,
                 "tools" : tools
            }
            if previous_response_id:
                 request["previous_response_id"] = previous_response_id
            response = openai_client.responses.create(**request)
            set_tokens(input_tokens= response.usage.input_tokens, output_tokens= response.usage.output_tokens)
            output_tokens = response.usage.output_tokens

            logger.info(json.dumps(
                    response.model_dump(),
                    indent=2
            ))

            print()
            while True:
                tools_output = []
                for item in response.output:
                    if item.type == "message":
                            print(item.content[0].text)
                    if item.type == "function_call":
                            arguments = json.loads(item.arguments)
                            print(f"Need to call function: {item.name}")
                            if item.name == "save_file":
                                fileName = arguments["fileName"]
                                content = arguments["content"]
                                logger.info(f"Save file: {fileName}")
                                output = save_file(fileName=fileName,content=content)

                            if item.name == "create_support_case":
                                 employee_id = arguments["employee_id"]
                                 output = create_support_case(employee_id=employee_id)
                            if item.name == "insert_support_case_text":
                                 case_id = arguments["case_id"]
                                 text = arguments["text"]
                                 output = insert_support_case_text(case_id=case_id,text=text)
                            if item.name == "get_file_content":
                                 file_name = arguments["fileName"]
                                 output = get_file_content(fileName=file_name)
                            if item.name == "list_files":
                                 output = json.dumps(list_files())
                            tools_output.append({
                                    "type" : "function_call_output",
                                    "call_id" : item.call_id,
                                    "output" : output
                                })
                ## Extra callback if tools_output populated
                if tools_output:
                    response = openai_client.responses.create(
                            model=deployment,
                            previous_response_id=response.id,
                            input=tools_output,
                            tools=tools)
                    set_tokens(input_tokens= response.usage.input_tokens, output_tokens= response.usage.output_tokens)
                    continue

                break
            previous_response_id = response.id
if __name__ == "__main__":
    main()
