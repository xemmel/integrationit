### Dotnet commands

```powershell

#### Create Solution

dotnet new sln -o simplewebapi


#### Create project (webapi) (inside solution folder)
cd simplewebapi
dotnet new webapi -o simplewebapi --use-controllers

#### Add project to solution
dotnet sln add .\simplewebapi\

#### Run the project
dotnet run --project .\simplewebapi\

### Func init (new function app project)

func init myfunctions --worker-runtime dotnet-isolated --target-framework net9.0

### Func new (new function)

func new -n mytrigger [-t HttpTrigger|QueueTrigger|TimerTrigger]

### Publish function app to azure

func azure functionapp publish **az204mimlc**

### List functions

func azure functionapp list-functions **az204mimlc** [--show-keys]
```