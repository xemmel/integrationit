## Install

```powershell

pip install azure.identity azure.ai.projects

```

## Set Env

```powershell
$ENV:FOUNDRY_PROJECT_ENDPOINT = "https://ai103-mlc-foundry.services.ai.azure.com/api/projects/proj-default"
$ENV:FOUNDRY_DEPLOYMENT = "maxi"

```

## App code

```python

import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
deployment = os.environ["FOUNDRY_DEPLOYMENT"]

credential = DefaultAzureCredential()

project_client = AIProjectClient(endpoint=project_endpoint,credential=credential)

client = project_client.get_openai_client()

user_input = input("Input: ")

response = client.responses.create(
    model=deployment,
    input=user_input
)

print(response.output_text)


```

## Run

```powershell

python app.py

```


### Looping with response id

```python

import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
deployment = os.environ["FOUNDRY_DEPLOYMENT"]

credential = DefaultAzureCredential()

project_client = AIProjectClient(endpoint=project_endpoint,credential=credential)

client = project_client.get_openai_client()

previous_response_id = None

user_input = input("Input: ")
response = client.responses.create(
    model=deployment,
    input=user_input
)
print(response.output_text)
previous_response_id = response.id
while True:

    user_input = input("Input: ")
    if user_input.lower() == "exit":
        break

    response = client.responses.create(
        model=deployment,
        input=user_input,
        previous_response_id=previous_response_id
    )
    previous_response_id = response.id

    print(response.output_text)




```