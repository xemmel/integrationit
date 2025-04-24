## First code snippet

### Add storage blob nuget package

```powershell

dotnet add package Azure.Storage.Blobs

```

### Replace Program.cs with code (and get your own ConnectionString)
> Note: container and blobName might also be different

```csharp

using Azure.Storage.Blobs;

System.Console.WriteLine("Fetching blob...");

string connectionString = "DefaultEndpointsP.....";
string containerName = "container2";
string blobName = "test.txt";

var client = new BlobServiceClient(connectionString: connectionString);

var containerClient = client.GetBlobContainerClient(containerName);
var blobClient = containerClient.GetBlobClient(blobName);
var content = await blobClient.DownloadContentAsync();
System.Console.WriteLine(content.Value.Content);



```


### Change to DefaultAzureCredential

```csharp

using Azure.Identity;
using Azure.Storage.Blobs;

System.Console.WriteLine("Fetching blob...");

string accountName = "vjbdkcustapptest";
string containerName = "container2";
string blobName = "test.txt";

var credential = new DefaultAzureCredential();

var client = new BlobServiceClient(
        serviceUri: new Uri($"https://{accountName}.blob.core.windows.net"),
        credential: credential);

var containerClient = client.GetBlobContainerClient(containerName);
var blobClient = containerClient.GetBlobClient(blobName);
var content = await blobClient.DownloadContentAsync();
System.Console.WriteLine(content.Value.Content);


```

> Run -> Azure CLI -> Not allowed -> Role Assignment on Storage Account  (blob data owner)
   -> Storage Account -> Access Control -> Add Role Assignment  (Storage Blob Data Owner)  
   -> Your self (az204student)
   -> Review/Create * 2

5-6 min

dotnet run -> OK


#### Create Service Account
> You will need to take note of:
  - Name
  - ClientId
  - ClientSecret
  - TenantId

- entra.microsoft.com
  -> Applications / App Registrations
     -> + New registration (give it a name and take note of it)
  -> Take note of ClientId and TenantId
  -> Manage/Certificates & secrets
      -> + New Client Secret (give it a name and period not importannt)
      -> Take note of the **VALUE**


#### Use the Service Account in the Program

```powershell

$ENV:AZURE_TENANT_ID = "551c586d-a82d-4526-b186-d061ceaa589e";
$ENV:AZURE_CLIENT_ID = "....";
$ENV:AZURE_CLIENT_SECRET = "....";

```