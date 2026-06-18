using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace myfunctions;

public class GetPassword
{
    private readonly ILogger<GetPassword> _logger;

    public GetPassword(ILogger<GetPassword> logger)
    {
        _logger = logger;
    }

    [Function("GetPassword")]
    public IActionResult Run([HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequest req)
    {
        _logger.LogInformation("C# HTTP trigger function processed a request.");
        var ftppassword = Environment.GetEnvironmentVariable("password");
        return new OkObjectResult($"The password: {ftppassword}");
    }
}
