using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Text.Json;

namespace aisplatformfunctions;

public class Transform
{
    private readonly ILogger<Transform> _logger;

    public Transform(ILogger<Transform> logger)
    {
        _logger = logger;
    }

    [Function("Transform")]
    public async Task<IActionResult> RunAsync([HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequest req, CancellationToken cancellationToken)
    {
        //coop-1234;
        //salling-4444;
        _logger.LogWarning("helloo");

        var request = await JsonSerializer.DeserializeAsync<TransformRequest>(
                    utf8Json: req.Body,
                    options: new JsonSerializerOptions { PropertyNameCaseInsensitive = true});

        _logger.LogInformation("blobName: {blobName}",request!.BlobName);


        // _logger.LogInformation("blobName: {blobName}",req!.BlobName);
        var senderId = request.BlobName.Split("-")[0];
        var response = new TransformResponse
        {
            BlobName = request.BlobName,
            SenderId = senderId
        };
        return new OkObjectResult(response);
    }
}
