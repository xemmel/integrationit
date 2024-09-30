using Azure.Core;
using Azure.Identity;
using Microsoft.AspNetCore.Mvc;

namespace aks.apis.Controllers;

[ApiController]
[Route("[controller]")]
public class TokenController : ControllerBase
{

    private readonly ILogger<TokenController> _logger;

    public TokenController(ILogger<TokenController> logger)
    {
        _logger = logger;
    }

    [HttpGet(Name = "GetToken")]
    public async Task<string> GetAsync([FromQuery]string resource, CancellationToken cancellationToken)
    {
        var credential = new DefaultAzureCredential();

        var token = await credential.GetTokenAsync(
                requestContext: 
                    new TokenRequestContext(
                            scopes: new string[] {resource}),
                            cancellationToken);
        string accessToken = token.Token;
        return accessToken;
    }
}
