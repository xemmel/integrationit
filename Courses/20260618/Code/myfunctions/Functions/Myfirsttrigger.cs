using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace myfunctions;

public class Myfirsttrigger
{
    private readonly ILogger<Myfirsttrigger> _logger;

    public Myfirsttrigger(ILogger<Myfirsttrigger> logger)
    {
        _logger = logger;
    }

    [Function("Myfirsttrigger")]
    public async Task<IActionResult> RunAsync([HttpTrigger(AuthorizationLevel.Function, "get")] HttpRequest req, CancellationToken cancellationToken)
    {
        _logger.LogInformation("C# HTTP trigger function processed a request.");
        return new OkObjectResult("Welcome to Azure Functions!");
    }
}
