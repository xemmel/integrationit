using System.Text;
using Azure.Identity;
using Azure.Storage.Blobs;
using Microsoft.AspNetCore.Mvc;

namespace az204webapi.Controllers;

[ApiController]
[Route("[controller]")]
public class BlobController : ControllerBase
{
    private readonly ILogger<BlobController> _logger;

    public BlobController(ILogger<BlobController> logger)
    {
        _logger = logger;
    }

    [HttpPost(Name = "PostBlob")]
    public async Task<string> PostAsync([FromBody]BlobInput blobInput,CancellationToken cancellationToken)
    {
        string containerName = "container2";
        string storageAccountName = "az204mlcdemo01";
        //string connectionString = "DefaultEndpointsProtocol=https;AccountName=az204mlcdemo01;AccountKey=O6WWDMCIxOy8mDwzImrOhLEb4mMZaOAoIk0Vwwi8Enfoo1fkG3WR+BMB8Y++ozGTVRJkgkxBCQrf+ASt2yOBYA==;EndpointSuffix=core.windows.net";
        //Use Service Account


        string blobName = Guid.NewGuid().ToString();


        var credential = new DefaultAzureCredential();
        
        //var storageAccountClient = new BlobServiceClient(connectionString: connectionString);
        var storageAccountClient = new BlobServiceClient(serviceUri: new Uri($"https://{storageAccountName}.blob.core.windows.net"), 
        credential: credential);

        var containerClient = storageAccountClient.GetBlobContainerClient(containerName);

        var blobClient = containerClient.GetBlobClient(blobName);

        //String to Stream
        var bytes = Encoding.UTF8.GetBytes(blobInput.Content);

        var stream = new MemoryStream(bytes);

        await blobClient.UploadAsync(stream,cancellationToken);



        return $"The blob {blobName} was uploaded";
    }
}
