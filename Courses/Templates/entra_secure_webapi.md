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
      - Leave the default suggested value and **Save**
    - Goto *Manage/App roles*
      - Create two roles *reader* and *writer*
 ![Create API Roles](/Images/entra_create_api_role.png)

