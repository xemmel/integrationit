using Microsoft.AspNetCore.Mvc;

namespace aks.apis.Controllers;

[ApiController]
[Route("[controller]")]
public class VersionController : ControllerBase
{

    private readonly ILogger<VersionController> _logger;

    public VersionController(ILogger<VersionController> logger)
    {
        _logger = logger;
    }

    [HttpGet(Name = "GetVersion")]
    public string Get()
    {
        return "1.1";
    }
}
