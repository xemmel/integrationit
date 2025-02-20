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



```