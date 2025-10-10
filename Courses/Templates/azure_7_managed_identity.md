- Create a new *Function App* in a new *Resource Group*
- Create an external *Storage Account* in the same *Resoure Group*


- Create a new *Function App Project* and an **HTTP Trigger** *Function*

> .NET version may differ

```powershell

func init mifunctions --worker-runtime dotnet-isolated --target-framework net9.0

cd mifunctions

func new -n TestFunction -t httptrigger


```

- Add Reference to *Azure.Identity* 

```powershell

dotnet add package Azure.Identity

```

- Open project in Visual Studio (Code)

- Change the content of *TestFunction.cs* to the following

```csharp

using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Azure.Identity;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using Azure.Core;

namespace mifunctions;

public class TestFunction
{
    private readonly ILogger<TestFunction> _logger;

    public TestFunction(ILogger<TestFunction> logger)
    {
        _logger = logger;
    }

    [Function("TestFunction")]
    public async Task<IActionResult> Run(
        [HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequest req,
        CancellationToken cancellationToken)
    {
        string audience = "https://storage.azure.com/";
        
        var credential = new DefaultAzureCredential();
        var url = req.Query["url"].ToString();

        var token = await credential
            .GetTokenAsync(
                requestContext: new TokenRequestContext(scopes: new string[] { audience }));
        var tokenString = token.Token;
        _logger.LogInformation("Got the token: {token}", tokenString);
        _logger.LogInformation("Calling url: {url}",url);

        var httpClient = new HttpClient();
        httpClient.DefaultRequestHeaders.Authorization
            = new AuthenticationHeaderValue(scheme: "Bearer", parameter: tokenString);
        httpClient.DefaultRequestHeaders.Add("x-ms-version", "2023-08-03");
        var response = await httpClient.GetStringAsync(requestUri: url, cancellationToken: cancellationToken);


        _logger.LogInformation(response);
        return new OkObjectResult("Welcome to Azure Functions!");
    }
}


```

- Publish the function app to *Azure*

> functionappname will differ

```powershell

func azure functionapp publish functionappname

```

- Create a container in your external storage account
- Upload a blob with some text in it to the container
- Get the blob Url and store it for later

- Get the *Invoke Url* for the function in the portal

- Call the url 

```powershell

curl https://functionurl............/apis/TestFunction?code=334.........&url=thebloburl

```

- This will fail because the Function app does not

