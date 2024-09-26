
using Azure.Identity;

public class BlobGreetingHandler : IGreetingHandler
{
    private readonly IMessageFormatter _messageFormatter;

    public BlobGreetingHandler(IMessageFormatter messageFormatter)
    {
        _messageFormatter = messageFormatter;
    }

    public async Task<string> GetGreetingAsync(CancellationToken cancellationToken = default)
    {
        var credential = new DefaultAzureCredential();

        var client = new Azure.Storage.Blobs.BlobServiceClient(
            serviceUri: new Uri("https://mlcaz204.blob.core.windows.net/"),
            credential: credential);
        var containerClient = client.GetBlobContainerClient("privatecontainer");
        var blobClient = containerClient.GetBlobClient("test.txt");
        var content = await blobClient.DownloadContentAsync();
        var contentString = content.Value.Content.ToString();
        
        var formattedMessage = _messageFormatter.FormatText(contentString);
        return formattedMessage;
    }
}