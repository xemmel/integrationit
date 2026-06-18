using Azure.Identity;
using Azure.Storage.Blobs;

string containerName = "container2";
string targetContainerName = "targetcontainer";
string blobName = "test.txt";
string targetBlobName = Guid.NewGuid().ToString();

string sourceStorageAccount = "aismlcdemo01";
string targetStorageAccount = "aismlcdemo02";


Console.WriteLine("Connecting....");


var credential = new DefaultAzureCredential();

var serviceClient = new BlobServiceClient(
        serviceUri: new Uri($"https://{sourceStorageAccount}.blob.core.windows.net/"),
        credential: credential);


var containerClient = serviceClient.GetBlobContainerClient(containerName);
var blobClient = containerClient.GetBlobClient(blobName);

var content = await blobClient.DownloadContentAsync();
var contentBinary = content.Value.Content;
System.Console.WriteLine(contentBinary);

// Upload a blob to target SA with content
var targetServiceClient = new BlobServiceClient(
        serviceUri: new Uri($"https://{targetStorageAccount}.blob.core.windows.net/"),
        credential: credential);
var targetContainerClient = targetServiceClient.GetBlobContainerClient(targetContainerName);
var targetBlobClient = targetContainerClient.GetBlobClient(targetBlobName);

await targetBlobClient.UploadAsync(contentBinary);
System.Console.WriteLine($"Blob: {targetBlobName} uploaded...");