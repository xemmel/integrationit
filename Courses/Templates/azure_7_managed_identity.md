- Create a new *Function App* in a new *Resource Group* (Choose **Flex**)
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
        string? responseMessage = null;
        try
        {
            string audience = "https://storage.azure.com/";

            var credential = new DefaultAzureCredential();
            var url = req.Query["url"].ToString();

            var token = await credential
                .GetTokenAsync(
                    requestContext: new TokenRequestContext(scopes: new string[] { audience }));
            var tokenString = token.Token;
            _logger.LogInformation("Got the token: {token}", tokenString);
            _logger.LogInformation("Calling url: {url}", url);

            var httpClient = new HttpClient();
            httpClient.DefaultRequestHeaders.Authorization
                = new AuthenticationHeaderValue(scheme: "Bearer", parameter: tokenString);
            httpClient.DefaultRequestHeaders.Add("x-ms-version", "2023-08-03");
            var response = await httpClient.GetStringAsync(requestUri: url, cancellationToken: cancellationToken);


            _logger.LogInformation(response);
            responseMessage = response;
        }
        catch (System.Exception ex)
        {

            responseMessage = ex.Message;
        }

        return new OkObjectResult(responseMessage);
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
  - In Overview of the Function App click on the function *TestFunction*
  - Click on *Get Function URL*
  - Copy the *default (Function key)*

- Call the url 

> append **&url=thebloburl** to the function url copied earlier


```powershell

curl https://functionurl............/apis/TestFunction?code=334.........&url=thebloburl

```

- This will fail because the Function app does not

```

ManagedIdentityCredential authentication failed: [Managed Identity] Authentication unavailable.

```

- Enable Managed Identity on your function app
  - Settings / Identity
    - Under *System assigned* set *Status* to *On* and click **SAVE** and choose **Yes**

- Call the function again (If you still receive a *Managed Identity* error, you may have to *Restart* the Function App, under *Overview* **Restart** )

- You should now get this error when calling the function

```
Response status code does not indicate success: 403 (This request is not authorized to perform this operation using this permission.).

```

- Go to your external *Storage Account* and grant the *Function App* a *Blob Owner Role*
  - *Access Control (IAM)*
     - Add / Add Role Assignment
     - Choose **Storage Blob Data Owner** Role. Click *Next*
     - Choose **+ Select members**
       - Search for your *Function App* name
       - Click on your *Function App* *Managed Identity* and choose **Select**
       - Click **Review + assign**
       - Click **Review + assign**

- You might have to wait a couple of minutes

- Call the function again

- You should now see the content of the blob
