using System.Net;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;

namespace myisolatedfunctions
{
    public class greeter
    {
        private readonly ILogger _logger;
        private readonly IGreetingHandler _greetingHandler;

        public greeter(ILoggerFactory loggerFactory, IGreetingHandler greetingHandler)
        {
            _logger = loggerFactory.CreateLogger<greeter>();
            _greetingHandler = greetingHandler;
        }

        [Function("greeter")]
        public async Task<HttpResponseData> RunAsync(
            [HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequestData req,
            CancellationToken cancellationToken)
        {
            _logger.LogInformation("C# HTTP trigger function processed a request.");

            var response = req.CreateResponse(HttpStatusCode.OK);
            response.Headers.Add("Content-Type", "text/plain; charset=utf-8");

            //IMessageFormatter formatter = new FunnyMessageFormatter();
            //IGreetingHandler greeter = new AngryGreetingHandler(formatter);


            string greeting = await _greetingHandler.GetGreetingAsync(cancellationToken);
            response.WriteString(greeting);

            return response;
        }
    }
}
