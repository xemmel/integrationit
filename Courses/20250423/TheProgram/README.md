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