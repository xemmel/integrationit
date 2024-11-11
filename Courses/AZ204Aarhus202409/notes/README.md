Region:

- Compliance!!!!!!!!

- Latency

- Version

- Pricing


-----------------------

Azure:

portal.azure.com

Entra:

entra.microsoft.com


portal.azure.com

az204@integration-it.com

Aa....

ASK LATER!!!!!!!

github.com/xemmel/integrationit

Courses/Templates/azure_1_storagaccount

Create new Resource Group (az204-init
--------------------------------

Resource Group:

Id SKAL være global!!! unik

ResourceId:
/SubscriptionId/ResourceGroupName


/subscriptions/9bc198aa-089c-4698-a7ef-8af058b48d90/
resourceGroups/rg-az204-mlc-demo01



Resource

ResourceId:
/subscriptionId/RGName/Type(VM,Storage,FunctionApp)/ResourceName


/subtest/rg1/vm/vm1 :-)
/subprod/rg1/vm/vm1 :-)
/subtest/rg1/disk/vm1 :-)


/subtest/rg2/vm/vm1 :-)

/subtest/rg1/vm/vm1 :-(

--------------

Blob URL:


https://mlcaz204.blob.core.windows.net/privatecontainer/test.txt
GET https://mlcaz204.blob.core.windows.net/publiccontainer/test.txt


--------------------


sv=2022-11-02&ss=b&srt=co&sp=riytfx&se=2024-09-24T17:23:02Z&st=2024-09-23T09:23:02Z&spr=https&sig=VaR0ZSt%2BJVBhfFTm7jKhZ7vO2ROyy%2BJCfvhjx2R8bm0%3D


sv=2022-11-02
&ss=b
&srt=co
&sp=riytfx
&se=2024-09-24T17:23:02Z
&st=2024-09-23T09:23:02Z
&spr=https

&sig=VaR0ZSt%2BJVBhfFTm7jKhZ7vO2ROyy%2BJCfvhjx2R8bm0%3D







Storage Account Queues
 Queue Size: TB
 Message Size: 75KB
 Protocol: At most once


Service Bus Queues
  Queue Size: GB
  Message Size: 256KB (Premium 100MB)
  Protocol: At least once
  Duplication Detection
  Sessions
  Enqueue Time
  Partitions

---------------------------------------------------

Service Account:

az204mlcserviceaccount

clientId (userName) : 77e48b87-48c0-4e26-9640-adeefdc95cba
secret (password) : B......
tenantId (domain) : 551c586d-a82d-4526-b186-d061ceaa589e


$env:AZURE_TENANT_ID = "551c586d-a82d-4526-b186-d061ceaa589e";
$env:AZURE_CLIENT_ID = "77e48b87-48c0-4e26-9640-adeefdc95cba";
$env:AZURE_CLIENT_SECRET = "B.......";



$env:AZURE_TENANT_ID = "";
$env:AZURE_CLIENT_ID = "";
$env:AZURE_CLIENT_SECRET = "";
--------------------------

az

az account show


az login --use-device-code

az group list -o table

$rgName = "rg-az204-mlc-script";

az group create --name $rgName --location "germanywestcentral";

az storage account create --resource-group $rgName --name mlc778899


az resource list -g $rgName -o table



New-AzStorageAccount -ResourceGroupName $rgName `
	-Name mlc7678899 -SkuName Standard_LRS `
  -Location germanywestcentral

---------------------

Function App Plans


Consumption:

Pay-as-you-go: 1 mio. free 0,000001 pr call
Cold starter
Auto-scale




App Service Plan:
"Fixed priced"
No restriction
Always on
Virtual Network integration




------------------------

External Storage account (Function App Queue)

mlcaz204external



------------------------------------------------


static void Main()
{
    var result = a.basync().GetAwaiter().GetResult();
}

static async Task MainAsync()
{
   var result = await a.basync();
}









Credentials:

https://management.azure.com/subscriptions/9bc198aa-089c-4698-a7ef-8af058b48d90/resourcegroups?api-version=2021-04-01




Farven på kortet:

- audience
- scopes
- resource
- resourceURI

-----------------------------
OAUTH2 / OpenIDConnect

IP (Authenticate)
Get token (audience/resource)

Call the actual API
HTTP Header
    Authorization:Bearer token




- Verify Function App Queue solution


- Function App/Environment Variables/Advanced Edit

externalStorageConnection: connectionString to the storage account 
(OLD WAY)


externalStorageConnection__queueServiceUri: https://mlcaz204external.queue.core.windows.net

- Function App/Identity -> Enable managed identity (On/Save)

SAVE / Restart (Overview)

- Application Insight
   - Failures  -> Does not have permission

External Storage Account
  -> Access Control (IAM)
   -> Add Role Assignment
   -> Storage Queue Contributor
   -> Members/Add members/function app name
   -> Review/Create * 2

4-5 min.
 Verify that message can be processed from inbound queue



$functionAppsIdentity = "651527a0-7050-427a-8487-8021d72d6965";
$scope = "/subscriptions/9bc198aa-089c-4698-a7ef-8af058b48d90/resourceGroups/rg-az204-mlc-functionapp/providers/Microsoft.Storage/storageAccounts/rgaz204mlcfunctionaa955";



Storage Account Contributor -> 17d1049b-9a84-46fb-8f53-869881c3d3ab
Storage Blob Data Owner -> b7e6dc6d-f1e8-4753-8033-0f276bb0955b
Storage Queue Data Contributor -> 974c5e8b-45b9-4653-ba55-5f855dd0fb88


az role assignment create `
  --role 17d1049b-9a84-46fb-8f53-869881c3d3ab `
  --scope $scope `
  --assignee $functionAppsIdentity
;

az role assignment create `
  --role b7e6dc6d-f1e8-4753-8033-0f276bb0955b `
  --scope $scope `
  --assignee $functionAppsIdentity
;

az role assignment create `
  --role 974c5e8b-45b9-4653-ba55-5f855dd0fb88 `
  --scope $scope `
  --assignee $functionAppsIdentity
;




@Microsoft.KeyVault(VaultName=az204mlcvault;SecretName=ftppassword)



externalStorageConnection: connectionString to the storage account 
(OLD WAY)


externalStorageConnection__queueServiceUri: https://mlcaz204external.queue.core.windows.net






AzureWebJobsStorage: connection String to the storage account

AzureWebJobsStorage__accountname: rgaz204mlcfunctionaa955




COSMOS DB:


- NoSQL (SQL) (default)

- MongoDb 
- Tables (storage account tables)
- PostGreSQL 
- Gremlin  (Graph)
- Cassandra (Key/Value)

- Event Grid

Redis Cache



API M


```xml


<validate-jwt header-name="Authorization" failed-validation-httpcode="401" failed-validation-error-message="Unauthorized. Access token is missing or invalid.">
    <openid-config url="https://login.microsoftonline.com/adminintegrationit.onmicrosoft.com/.well-known/openid-configuration" />
    <audiences>
        <audience>api://facd96d4-988f-4445-bc4e-f1b7d09912f7</audience>
    </audiences>
    <required-claims>
        <claim name="roles" match="all">
            <value>apimexecuter</value>
        </claim>
    </required-claims>
</validate-jwt>

```

Service
   Api
     Operation



Operation Before Base
API Before Base
Product Before
Service
Product Before
API After Base
Operation After Base


