Notes from course

Azure Integration Services (AIS)

Morten la Cour
integration-it.com

mlc@integration-it.com


Azure (Dev, Adm, Architect, Security, DevOps)
BizTalk
AI
Kubernetes (Containers/Docker)

Bordet rundt:
- Hvem er du?
- Hvorfor er du her?
- Azure/Entra(AAD) erfaring?
- Kode erfaring?



(Security all over the place!)
- Network

- Azure generelt
- Storage Accounts / Web Apps
- Logic Apps

- Function Apps
- Service Bus (Queues/Topics)

- Event Grid
- API Management

- Deployment
- Putting it all together


I.P. Entra
Login/Authenticate

Get token (audience/scope)

token (1 hour!!!) (IdentityId, audience)

API (azure)

HTTP
   Header
      Authorization:Bearer token


Naming

Resource Group

ResourceGroupId (unique) global!!

/subscriptionId/RGName

Resource

ResourceId (unique) global!!!

/subscriptionId/RGNAME/Type(vm,disk,storage,web app)/ResourceName

/subtest/rg1/vm/vm1 :-)
/sudprod/rg1/vm/vm1 :-)
/subtest/rg1/disk/vm1 :-)


/subscriptions/9bc198aa-089c-4698-a7ef-8af058b48d90/resourceGroups/rg-ais-mlc-demo01-remove/providers/Microsoft.Storage/storageAccounts/aismlcdemo01



Logic App (Workflows)

Consumption vs Standard

Trigger   -> HTTP, Timer, Resource Event, FTP, Queue

x number of Actions


AIS TYPES

Logic App (Workflows)

(Function App) 

(Storage Account)

Service Bus (MQ)

Event Grid (Event driven integrations)

API Management

Data Factory (Azure SSIS)

if (Test-Path .\publish.zip) {
    Get-Item .\publish.zip | Remove-Item -Recurse -Force
}
dotnet publish -c Release -o ./publish
cd .\publish
Compress-Archive -Force -Path * -DestinationPath ..\publish.zip
cd ..
az webapp deploy --resource-group rg-ais-mlc-webapp-remove --name mlcaisweb02  --src-path ./publish.zip --slot pre



az webapp deployment slot swap --slot pre --target-slot production --resource-group rg-ais-mlc-webapp-remove --name mlcaisweb02


Logic Apps

Trigger

Actions

JSON
LA Definition Language
Action
"actionName" : {
  "inputs": "morten" | {} | 17,
  "type" : "Compose|Http|Api Connection|Functions|...",
  "runAfter" : {
    "previousActionName" : [ "Succeeded" ]
  }
}

//Get data from previous actions|trigger

@outputs('actionName')
@body('actionName') -> @outputs('actionName')['body']
@{outputs('actionName')} Have a nice day

Trigger output

@triggerOutputs()
@triggerBody() -> @triggerOutputs()['body']



GET 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/' HTTP/1.1 Metadata: true


http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://sevicebus.azure.net/


MQ

Storage Account 
Queue Size: TB
Message Size: Max 75KB
At most once delivery
Exp date

Service Bus Queue (Real MQ)
Queue Size 1-4 GB
Message Size: 256 KB -> Premium Ed: 100 MB
At least once delivery
Exp date
Enqueue Time
Sessions (Ordered Delivery)
Duplicate Detection

Service Bus Namespace (Azure Resource) (Container Queue, Topics)




Function App

Consumption
   - Pay as you go
   - No VNET integration (Relay)
   - Cold starts



App Service
   - "Fixed" Place
   - VNET integration


winget install Microsoft.Azure.FunctionsCoreTools

<CONNECTION_NAME_PREFIX>: connectionString (!!!PASSWORD)

or

externalStorageConnection__queueServiceUri

https://stmlcaisfunctionexternal.queue.core.windows.net


AzureWebJobsStorage__accountname
rgaismlcfunctionapp8112


APIM Service (Container)
   - APi
   - Api

Price

- Centralizing (Gateway)
- Security
- Policies
- User control


 APIM Service
   - API ()   ->     Real API
       -Operation  (Method, posturl)

   - API      ->     REAL API









Policies

    Operation
  API
 Product
Service
  Product
    API
      Operation



<validate-jwt header-name="Authorization" failed-validation-httpcode="401" failed-validation-error-message="Unauthorized. Access token is missing or invalid.">
    <openid-config url="https://login.microsoftonline.com/adminintegrationit.onmicrosoft.com/.well-known/openid-configuration" />
    <audiences>
        <audience>https://management.azure.com/</audience>
    </audiences>
    <required-claims>
        <claim name="oid" match="all">
            <value>43164783-c836-4182-b77c-46936e588b28</value>
        </claim>
    </required-claims>
</validate-jwt>


<Order>
   <CustomerName>Morten</Cust>
</Order>

->
{
   "customerName" : "Morten"
}

<Order>
   <CustomerName>Morten</Cust>
   <Qty>17</Qty>
</Order>

->

{
   "customerName" : "Morten",
   "qty" : "17"
}


<Order>
   <CustomerName>Morten</Cust>
   <Qty>17</Qty>
      <Line nwe="array">
        <Item>55r</Item>
      </Line>
 </Order>

->

{
   "customerName" : "Morten",
   "qty" : "17",
   "line" : [
     {
        "item" : "55r"
     }
   ]
}



