using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace FunctionApp;

public class HttpTrigger12
{
    private readonly ILogger<HttpTrigger12> _logger;

    public HttpTrigger12(ILogger<HttpTrigger12> logger)
    {
        _logger = logger;
    }

    [Function("HttpTrigger1")]
    public IActionResult Run([HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequest req)
    {
        _logger.LogInformation("C# HTTP trigger function processed a request.");
        return new OkObjectResult("Welcome to Azure Functions!");
    }

    [Function("HttpTrigger2")]
    public IActionResult Run2([HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequest req)
    {
        _logger.LogInformation("C# HTTP trigger function processed a request.");
        return new OkObjectResult("Welcome to Azure Functions2!");
    }
}
