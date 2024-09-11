## Web App

1. Create a WebApp
```powershell




dotnet dev-certs https -t

dotnet new webapp -o [thename]

properties->launchsettings.
 line 15       "applicationUrl": "https://localhost:xxxx;http://localhost:5267",

cd 

dotnet run

Note the port used for https

Get the https url


dotnet add package Microsoft.AspNetCore.Authentication.OpenIdConnect
dotnet add package Microsoft.Identity.Web;
dotnet add package Microsoft.Identity.Web.UI;


```
1. Create App Registration in *Entra*   (entra.microsoft.com)

Under *Redirect URI (optional)*
   - select a platform -> Web
   - url: https://localhost:xxxx/signin-oidc


Save

Get *ClientId* and *TenantId*

Authentication (in App Reg) -> Implicit -> ID Tokens



Visual Studio Code (App)

In appsettings

```json

,  "AzureAd": {
    "Instance": "https://login.microsoftonline.com/",
    "TenantId": "...",
    "ClientId": "...",
    "CallbackPath": "/signin-oidc"
  }

```
Program.cs

```csharp

using Microsoft.Identity.Web;

builder.Services.AddRazorPages();

builder
    .Services
    .AddMicrosoftIdentityWebAppAuthentication(builder.Configuration);

builder.Services.AddAuthorization(options =>
{
    // By default, all incoming requests will be authorized according to the default policy.
    options.FallbackPolicy = options.DefaultPolicy;
});


....


app.UseAuthentication(); //Insert this
app.UseAuthorization();


```

dotnet run -> Login (Existing browser NOT PROMPTED!!) -> Incagnito


In Shared/
_LoginPartial.cshtml

```razor

@using System.Security.Principal

<ul class="navbar-nav">
@if (User.Identity?.IsAuthenticated == true)
{
        <span class="navbar-text text-dark">Hello @User.Identity?.Name!</span>
        <li class="nav-item">
            <a class="nav-link text-dark" asp-area="MicrosoftIdentity" asp-controller="Account" asp-action="SignOut">Sign out</a>
        </li>
}
else
{
        <li class="nav-item">
            <a class="nav-link text-dark" asp-area="MicrosoftIdentity" asp-controller="Account" asp-action="SignIn">Sign in</a>
        </li>
}

```
Shared/_Layout.cshtml (line 28)

```html
                    </ul>
                    <partial name="_LoginPartial" />
                </div>

```

[Back to top](#table-of-content)
