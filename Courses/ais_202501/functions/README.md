
## Create new Function App Project

```powershell

func init myisolatedproject --worker-runtime dotnet-isolated  --target-framework net9.0 

func init myinprocessproject --worker-runtime dotnet --target-framework net8.0 

```

### Create new Function (inside the Function App folder)

```powershell

## Choose trigger type manually

func new -n MyHttpTrigger

func new -n MyHttpTrigger -t HttpTrigger

### VS COde

code .
```


### Publish function app to Azure

> *** = name of function app
```powershell

func azure functionapp publish ****


```

### List function with keys

```powershell

func azure functionapp list-functions ******** --show-keys

```

### Call with function key in Header

```powershell

curl "https://*****.azurewebsites.net/api/myhttptrigger" -H "x-functions-key:******"

```