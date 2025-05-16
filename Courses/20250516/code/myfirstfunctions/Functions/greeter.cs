using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace myfirstfunctions
{
    public class greeter
    {
        private readonly ILogger<greeter> _logger;
        private readonly IGreeter _greeter;

        public greeter(ILogger<greeter> logger, IGreeter greeter)
        {
            _logger = logger;
            _greeter = greeter;
        }

        [Function("greeter")]
        public async Task<IActionResult> RunAsync(
            [HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequest req,
             CancellationToken cancellationToken)
        {
            _logger.LogInformation("C# HTTP trigger function processed a request.");
            var greeting = await _greeter.GetGreetingAsync(cancellationToken);
            return new OkObjectResult(greeting);
        }
    }
}
