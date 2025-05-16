using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace myfirstfunctions
{
    public class myhttptrigger
    {
        private readonly ILogger<myhttptrigger> _logger;

        public myhttptrigger(ILogger<myhttptrigger> logger)
        {
            _logger = logger;
        }

        [Function("myhttptrigger")]
        public async Task<IActionResult> RunAsync(
            [HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequest req,
            CancellationToken cancellationToken)
        {
            _logger.LogInformation("C# HTTP trigger function processed a request.");
            return new OkObjectResult("Hello students from new FA");
        }
    }
}
