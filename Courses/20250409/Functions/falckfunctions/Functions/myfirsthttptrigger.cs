using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace falckfunctions
{
    public class myfirsthttptrigger
    {
        private readonly ILogger<myfirsthttptrigger> _logger;

        public myfirsthttptrigger(ILogger<myfirsthttptrigger> logger)
        {
            _logger = logger;
        }

        [Function("myfirsthttptrigger")]
        public async Task<IActionResult> RunAsync(
            [HttpTrigger(AuthorizationLevel.Function, "get")] HttpRequest req,
            CancellationToken cancellationToken = default)
        {
            _logger.LogInformation("C# HTTP trigger function processed a request.");
            return new OkObjectResult("Hello Falck!!");
        }
    }
}
