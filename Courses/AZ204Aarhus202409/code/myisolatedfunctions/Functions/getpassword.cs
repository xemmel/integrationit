using System.Net;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;

namespace myisolatedfunctions
{
    public class getpassword
    {
        private readonly ILogger _logger;

        public getpassword(ILoggerFactory loggerFactory)
        {
            _logger = loggerFactory.CreateLogger<getpassword>();
        }

        [Function("getpassword")]
        public HttpResponseData Run([HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequestData req)
        {
            _logger.LogInformation("C# HTTP trigger function processed a request.");

            var response = req.CreateResponse(HttpStatusCode.OK);
            response.Headers.Add("Content-Type", "text/plain; charset=utf-8");
            //Make a ftp call

            //Retrive ftp password
            string? password = Environment.GetEnvironmentVariable("ftppassword");
            //Make the call

            response.WriteString($"The password is: {password}");

            return response;
        }
    }
}
