using System.Text.Json;
using Azure.Identity;
using Azure.Storage.Blobs;

public class ProcessChristOrderService : IProcessOrderService
{
    public async Task<Order> ProcessOrderAsync(Order order, CancellationToken cancellationToken = default)
    {
        var credential = new DefaultAzureCredential();
        string storageAccount = "aismlcdemo01";
        string containerName = "container2";

        var serviceClient = new BlobServiceClient(
        serviceUri: new Uri($"https://{storageAccount}.blob.core.windows.net/"),
        credential: credential);

        var containerClient = serviceClient.GetBlobContainerClient(containerName);
        var blobClient = containerClient.GetBlobClient(Guid.NewGuid().ToString());

        order.Qty += 2;
       var binaryData = BinaryData.FromObjectAsJson<Order>(order);
        
        await blobClient.UploadAsync(binaryData);

        return order;
    }
}