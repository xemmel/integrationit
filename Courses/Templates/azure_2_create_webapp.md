- Create a *Web App/App Service* in the same process create new *Resource Group* (**rg-student-*your intitals*-webapp**)
  - Needs a unique name
  - Choose *Code*  *.NET 8 (LTS)* 
  - Choose region 
  - Choose Linux for *Operation System*
  - Under **Pricing Plans** -> **Pricing Plan** leave it as **Premium V3 P0V3**
  - **Review + create ** -> **Create**

- Make a note of your *Resource Group* and the name or the *Web App*

- Back in your *Web App* go to the *Overview* page (it might take a minute or so to load the first time)
  - Click on **Default domain** and verify that your web app is up and running


- Create a C# Web Api
  - In your root folder execute the following *dotnet command*

```powershell

dotnet new webapi -controllers -o integrationit.test.api

cd .\integrationit.test.api\

dotnet run

### Not the http://localhost:.... address

``` 

- In another powershell session run the following (replace xxxx with port)

```powershell

curl http://localhost:xxxx/weatherforecast

```

- Verify that the default *weatherforecast* api is working

- exit the running web api (CTRL+C)

- open *visual studio code* inside the folder *integrationit.test.api*

```powershell

code .

```




