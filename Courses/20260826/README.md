AI-200: Develop AI cloud solutions on Azure
  Formerly Known as Az-204 Developing Solutions for Microsoft Azure ???

Morten la Cour
integration-it.com
flowgrait.io (Integration Platform in Azure -> BizTalk)


- Azure
- AI
- Integration
- C#, Python
- Containers/Docker/Kubernetes
- Security (Ethical Hacker!)

- Hvem er du?
- Hvorfor er du her?
- Azure/Azure AI/Entra(AAD)/C#, Python erfaring?
- Certificering?


Agenda (officiel):

- Containers (ACR/WebApps)
- Containers (Azure Container Apps)
- Containers (Kubernetes) (!)
- Azure Cosmos Db (VectorDb) (!)
- PostgreSQL (VectorDb) (!)
- Azure Managed Redis (Cache) (!)
- Implement backend services for AI Solutions (Service Bus (MQ), Event Grid, Azure Functions (create MCT Server)
- Manage application Secrets and configuration (Azure Keyvaults, Azure App Configuration)
- Observe and Troubleshoot (Application Insight, OpenTelemetry,Log Analytics, KQL)


- Azure fundamentals
- Azure Storage Account
- Azure Security (RBAC, Managed Identity) 
- Secure Application with Entra(AAD) (Apps/API)
- API Management
- Function App Deep
- 

portal.azure.com
    - entra !!

entra.micrsoft.com


### Azure Naming

Resource Group

Id (ResourceGroupId) (Global Unique)

/subscriptionId/ResourceGroupName


ResourceId

/subscriptionId/RGName/Type(VM, disk, storage account)/Name

/subtest/rg1/vm/vm1 :-)
/subprod/rg1/vm/vm1 :-)

/subtest/rg1/disk/vm1 :-)
/subtest/rg2/disk/vm1 :-)

/subtest/rg1/vm/vm1 :-(


## containers

HTTP protocol file system

Container = folder
Blob = file (bytes)



GET
https://teknodkmlcdemo01.blob.core.windows.net/container1/test.txt
https://teknodkmlcdemo01.blob.core.windows.net/container2/test.txt


## Student login

portal.azure.com

ai200student@integration-it.com

ThePlaceAug2026!!

GitHub.com/xemmel/integrationit

Courses/Templates/azure_1_storage_account.md   (Walkthrough)


## Azure Man Rest API

### List Resource Group

GET https://management.azure.com/subscriptions/6f45c47b-7dde-4813-967c-b3b549d73f9c/resourcegroups?api-version=2021-04-01


OAuth2/OpenIdConnect


-> Entra (login)
    -> Token (type/audience/scope)
token    <- Token


    -> API
        Header:
          Authorization: Bearer [token]


## CLI Tricks

az account show

az account set --subscription 9bc1


### Delete Resource Groups!


 az group list --subscription 9bc198aa-089c-4698-a7ef-8af058b48d90 | ConvertFrom-Json | Out-GridView -PassThru | ForEach-Object {az group delete --name $_.name --subscription 9bc198aa-089c-4698-a7ef-8af058b48d90 --no-wait --yes}


az group list  | ConvertFrom-Json | Out-GridView -PassThru | ForEach-Object {az group delete --name $_.name  --no-wait --yes}


az group list -o table


 az account get-access-token --resource https://management.azure.com/


$location="germanywestcentral"
$rgName="rg-mlc-demo02"


## create resource group
az group create `
   --location $location `
   --name $rgName


### Create Storage account

az storage account create `
  --name 44 `
  --allowff true `


### Add Role Assignment

az role assignment create `
  --role "Storage Blob Data Reader" `
  --scope "/subscriptions/6f45c47b-7dde-4813-967c-b3b549d73f9c/resourceGroups/rg-ai200-mlc-demo01/providers/Microsoft.Storage/storageAccounts/teknodkmlcdemo01" `
  --assignee "43164783-c836-4182-b77c-46936e588b27"

MQ (azure)

Storage Account queues ($)


Service Bus MQ  (MQ) ($$)
   - Duplicate Detection
   - Session
   - 
   - VNET (Premium) (600$)


Service Bus Namespace   = Azure Resource
   - Queue
   - Queue
   - Topic


Function App = WebApp = Azure Resource
   - Functions
   - Functions 


Function App   (c# project) (func init) (key)
   Function (Trigger) Timer, HTTP, Resource (MQ, Blob!!)
   Function (c# class) (func new)  (key)

System Storage Account


func init thefunctions --worker-runtime dotnet-isolated 












