using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace myfunctions;

public class Calculator
{
    private readonly ILogger<Calculator> _logger;

    public Calculator(ILogger<Calculator> logger)
    {
        _logger = logger;
    }

    [Function("Calculator")]
    public IActionResult Run([HttpTrigger(AuthorizationLevel.Function, "get")] HttpRequest req)
    {
        var numberString = req.Query["number"].ToString();
        _logger.LogWarning("The number entered is: {number}",numberString);
        int number = int.Parse(numberString);


        return new OkObjectResult($"The number: {number} squared is: {number*number}");
    }
}
