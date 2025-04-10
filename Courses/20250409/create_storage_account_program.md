Fetch from Storage Account

 ConnectionString
 containerName (private)
 blobName 


```powershell

dotnet new console -o falck.getblob
cd falck.getblob
dotnet add package Azure.Storage.Blobs
code .

```

> overwrite Program.cs

```csharp
//Read blob

//BLOB SDK


using Azure.Storage.Blobs;

//Client

var connectionString = ".....";
var containerName = args[0];
var blobName = args[1];

var blobServiceClient = new BlobServiceClient(connectionString: connectionString);




var containerClient = blobServiceClient.GetBlobContainerClient(containerName);

var blobClient = containerClient.GetBlobClient(blobName);

var content = await blobClient.DownloadContentAsync();

System.Console.WriteLine(content.Value.Content.ToString());

```

```powershell

dotnet run containername blobname

```