- Create a new **C# web api** and add the required *nuget packages*
```powershell

dotnet new webapi -controllers -o integrationit.securetest.api


cd .\integrationit.securetest.api\

dotnet add package Microsoft.Identity.Web

```

- Open in *Visual Studio Code*

- Make *https* possible locally

```powershell

dotnet dev-certs https -t

```

  - Inside *Properties/launchSettings.json*
    - Overwrite line 17 with the content of line 27

```json

  "profiles": {
    "http": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "launchUrl": "swagger",
      "applicationUrl": "https://localhost:7039;http://localhost:5173",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    },
    "https": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "launchUrl": "swagger",
      "applicationUrl": "https://localhost:7039;http://localhost:5173",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    },

``` 

  - run again and verify that https works now

```powershell

curl https://localhost:7039/weatherforecast

```

- Create *App Registrations* in *Entra ID* (entra.microsoft.com)
  - Under *Applications/App Registrations* click **+ New registration**
    - set the name to *course[yourinitials]api*
    - Click **Register**
    - Get the *Tenant ID* and the *Client ID* (this Client ID will be referenced as *Api Client Id*)
    - Goto *Manage/Expose an API*
      - Next to **Application ID URL** click *Add*
      - Leave the default suggested value and make a note of it (will be refered to as *audience*) and **Save**
    - Goto *Manage/App roles*
      - Create two roles *reader* and *writer*
 ![Create API Roles](/Images/entra_create_api_role.png)
    - Goto *Owners*
      - Click *Add owners* and add the user you are currently using in *Entra*
  
  - Secure the api code with the *Api App Registration* just created
    - Replace *Program.cs* with the following code
```csharp

using Microsoft.Identity.Web;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder
    .Services
    .AddMicrosoftIdentityWebApiAuthentication(builder.Configuration);

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthentication();
app.UseAuthorization();

app.MapControllers();

app.Run();


```
    - Replace *appsettings.Development.json* with the following (use your own *tenant Id* and *Api Client Id*)
```json

{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AzureAd" : {
    "ClientId" : "1234replaceme",
    "TenantId" : "1234replaceme",
    "Instance": "https://login.microsoftonline.com/"
  }
}


```

    - Decorate your *WeatherController* with an *[Authorize]* attribute, note that a new *using* is needed

```csharp

using Microsoft.AspNetCore.Authorization; //New line
using Microsoft.AspNetCore.Mvc;

namespace integrationit.securetest.api.Controllers;

[ApiController]
[Authorize] //New Line
[Route("[controller]")]
public class WeatherForecastController : ControllerBase

```
  - Run the dotnet Api again (note if already running, you need to stop it *CTRL+C* and start again *dotnet run*)
  - Call the api again this time it will not work, use *-v* after your curl command to see the *401 Unauthorized*


   - Back in *entra* Under *Applications/App Registrations* click **+ New registration**
    - set the name to *course[yourinitials]app*
    - Click **Register**
    - Make a note of the *Client ID* this will be refered to as *App Client Id*
    - Goto **Certificates & secrets**
      - **+ New client secret** Give the secret a name and select 3 months, click **Add**
      - Copy the **Value** (not the **Secret ID**) to somewhere save (local notepad), this value must never be exposed
  - Get a token into the *powershell variable* **$token** (see [Get Token](/Courses/Templates/Tokens/Get_Token.md) )
  - Now run the curl command this time supplying the token
```powershell

curl https://localhost:7039/weatherforecast -H "Authorization: Bearer $token"

```
  - Notice that you still get *401*
  - Decode your token, See [Decode Token](/Courses/Templates/Tokens/Decode_Token.md) 
    - Notice that no *scopes* nor *roles* are set
  
  - Add a reader role to the *App App Registration*
    - Goto the *App App Registration* (course[init]app)
      - Under *API Permissions* select **+ Add a permission**
      - Choose *My APIs* tab and select your *API registration*
      - Select *reader* and **Add permissions**
      - Select **Grant admin consent for Default Directory** (Note: at your own company, you might not be able to do this)
  - Get new token and decode it (it might take a minute or two before the role is present in the token claims)
  - Once the token contains the role *reader* call the api again, this time it should work

  - Decorate *weatherforecast* so that only token with *writer* role can access it

```csharp

[ApiController]
[Authorize(Roles = "writer")]
[Route("[controller]")]

```
  - Run the api again
  - Once again *401* since the token do not hold the correct *Role claim*
  - In *Entra* give the app *App Registration* the writer role, get new token, verify that it now has two roles *reader* and *writer* and call again, now it should work
    