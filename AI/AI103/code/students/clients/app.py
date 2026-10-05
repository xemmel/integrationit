import os
import argparse

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from azure.ai.projects import AIProjectClient


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--mode")

args = arg_parser.parse_args()

mode = args.mode
openai_client = None

if mode.lower() == "openai_key":
    api_key=os.environ["FOUNDRY_KEY"]
    openai_client = OpenAI(api_key=api_key,base_url=os.environ["OPENAI_ENDPOINT"])

if mode.lower() == "openai_entra":
    api_key = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")
    openai_client = OpenAI(api_key=api_key,base_url=os.environ["OPENAI_ENDPOINT"])


if mode.lower() == "aiproject":
    credential = DefaultAzureCredential()
    project_client = AIProjectClient(endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],credential=credential)
    openai_client = project_client.get_openai_client()

if openai_client:
    user_input = input("Input: ")
    response = openai_client.responses.create(
        model=os.environ["FOUNDRY_MODEL"],
        input=user_input
    )

    print(response.output_text)
else:
    print("openai client not set")
