using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace myfirstfunctions
{
    public class myfirstfunction
    {
        private readonly IGreetHandler _greetHandler;
        private readonly ILogger<myfirstfunction> _logger;

        public myfirstfunction(ILogger<myfirstfunction> logger, IGreetHandler greetHandler)
        {
            _greetHandler = greetHandler;
            _logger = logger;
        }

        [Function("myfirstfunction")]
        public async Task<IActionResult> RunAsync(
            [HttpTrigger(AuthorizationLevel.Function, "get")] HttpRequest req, CancellationToken cancellationToken)
        {
            
            _logger.LogInformation("C# HTTP trigger function processed a request.");
            var greeting = await _greetHandler.GetGreetingAsync(cancellationToken);
            return new OkObjectResult(greeting);
        }
    }
}
