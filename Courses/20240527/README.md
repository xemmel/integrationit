## Agenda

- What is Azure
   - What is cloud computing
   - What is Microsoft Azure
   - Subscriptions/Resource Groups/Resources
   - Management plane and Data/App plane
   - Policies
   - Security
   - Regions/Locations
   - Entra (Azure AD)
   - Exercise
       - Create a Storage Account in the Azure Portal and set up Access Control


- Azure App Services / Web Apps
   - What are Azure Web Apps
   - What is an App Service Plan
   - PaaS vs IaaS
   - Scaling
   - Deployment
       - Powershell/CLI
       - Deployment slots
       - Deployment from Container Registry
   - Exercise
      - Create a Web App and deploy through Azure CLI
      - Containerize a C# Aspnet core web api, deploy it to ACR and update
        a container web app

- Azure Functions
   - What is Azure Functions
   - Consumption vs. App Service plan
   - Using Managed Identity to harden AF infrastructur
   - Using Managed Identity in AF code
   - What are Durable Functions
   - Exercise
      - Create an Azure Function App in Azure and deploy an HTTP Trigger
    and a QueueTrigger via. the Function CLI tool and harden the Function App
with Managed Identities.


- Azure Service Bus
   - Queues
   - Topics
   - PeekLock vs. ReceiveAndDelete
   - Coding with SDK's towards queues/topics
   - Exercise
     - Create a topic with multiple subscribers

- Azure Networking
   - VNET
   - Private Endpoints
   - Delegated subnets

- Monitoring and Logging
  - Diagnostics Settings
  - Monitor/Log Analytics Workspaces
  - Application Insight
  - Enable Application Insight in code
  - Kusto Queries
  - Alerts
  - Exercise
     - Examine Monitoring and Kusto queries in Azure

- Securing Applications
   - App Registrations
   - Managed Identities
   - Exercise
      - Use Managed Identity in a Function App
 - Secure a C# web api with Entra

- Existing Azure setup at Nitor Energy and best practice use case
   - Backup of data planes
   - VNET/Private endpoints
