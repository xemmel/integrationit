using System.Text;
using Azure.Identity;
using Azure.Storage.Blobs;

string containerName = "container2";
string blobName = Guid.NewGuid().ToString();

string storageAccountName = "az204mlc01";
string content = "Test";

var serviceUri = new Uri($"https://{storageAccountName}.blob.core.windows.net");

var credential = new DefaultAzureCredential();


//2 Storage account
var serviceClient = 
    new BlobServiceClient(serviceUri: serviceUri,credential: credential);



var containerClient =   serviceClient.GetBlobContainerClient(containerName);

var blobClient =  containerClient.GetBlobClient(blobName);

var encoding = Encoding.UTF8;
var bytes = encoding.GetBytes(content);
var stream = new MemoryStream(bytes);

await blobClient.UploadAsync(stream);

System.Console.WriteLine($"Blob: {blobName} uploaded");


//Submit MQ

//Key Vault


