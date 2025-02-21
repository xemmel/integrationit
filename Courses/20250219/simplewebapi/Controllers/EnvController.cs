using Microsoft.AspNetCore.Mvc;

namespace simplewebapi.Controllers;

[ApiController]
[Route("[controller]")]
public class EnvController : ControllerBase
{

    private readonly ILogger<EnvController> _logger;

    public EnvController(ILogger<EnvController> logger)
    {
        _logger = logger;
    }

    [HttpGet(Name = "GetEnv")]
    public string? Get([FromQuery]string env)
    {
        var value = Environment.GetEnvironmentVariable(env);
        return value;
    }
}
