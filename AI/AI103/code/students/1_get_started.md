## Windows

### Install prerequisites 

```powershell

winget install Python.Python.3.14

winget install Microsoft.AzureCLI


### If needed

winget install Microsoft.VisualStudioCode

winget install Git.Git

```

### Clone the MS labs

```powershell

cd c:\code
git clone https://github.com/MicrosoftLearning/mslearn-ai-agents.git

```

### Login to Azure CLI

```powershell

az login --use-device-code

```

### Create a python virtual environment

```powershell

mkdir code
cd code

mkdir python
cd python

python -m venv devenv

.\devenv\Scripts\Activate.ps1


```

### Clone the labs

```powershell

git clone https://github.com/MicrosoftLearning/mslearn-ai-agents.git

```

### Install the Azure Foundry packages

```powershell

pip install openai azure.identity azure.ai.projects

```

### Create first app

```powershell

$ENV:FOUNDRY_PROJECT_ENDPOINT="https://integration-it.services.ai.azure.com/api/projects/integration-it-project"
$ENV:FOUNDRY_DEPLOYMENT="mini"

mkdir firstapp
cd firstapp
code .

```

#### Chat completion

- Create new file called app_completion.py

```python

import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
deployment = os.environ["FOUNDRY_DEPLOYMENT"]

credential = DefaultAzureCredential()

project_client = AIProjectClient(endpoint=project_endpoint,credential=credential)

openai_client = project_client.get_openai_client()

user_input = input("Input: ")
response = openai_client.chat.completions.create(
        model=deployment,
        messages=[
            {
                "role" : "user",
                "content" : user_input
            }
        ])
print(response.choices[0].message.content)


```

##### Test

```powershell

python .\app_complete.py

```

#### Response

- Create a file called app_response.py

```python

import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
deployment = os.environ["FOUNDRY_DEPLOYMENT"]

credential = DefaultAzureCredential()

project_client = AIProjectClient(endpoint=project_endpoint,credential=credential)

openai_client = project_client.get_openai_client()

user_input = input("Input: ")
response = openai_client.responses.create(model=deployment,input=user_input)
print(response.output_text)


``` 
