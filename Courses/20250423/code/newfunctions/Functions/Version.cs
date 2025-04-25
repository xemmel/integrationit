using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace newfunctions
{
    public class Version
    {
        private readonly ILogger<Version> _logger;

        public Version(ILogger<Version> logger)
        {
            _logger = logger;
        }

        [Function("Version")]
        public IActionResult Run([HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequest req)
        {
            _logger.LogInformation("C# HTTP trigger function processed a request.");
            return new OkObjectResult("Az 204!!!");
        }
    }
}
