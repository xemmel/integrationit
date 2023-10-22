



## Durable functions


### Create .NET 7 Isolated Durable Function App Project

```powershell

### Create project

func init durabletest --worker-runtime dotnet-isolated --target-framework net7.0

### Create new Durable Function

func new -t DurableFunctionsOrchestration -n firstdurablefunction


```


#### Replace code

```csharp

     outputs.Add(await context.CallActivityAsync<string>(nameof(SayHelloAsync), "Tokyo"));
            outputs.Add(await context.CallActivityAsync<string>(nameof(SayHelloAsync), "Seattle"));
            outputs.Add(await context.CallActivityAsync<string>(nameof(SayHelloAsync), "London"));



     [Function(nameof(SayHelloAsync))]
        public static async Task<string> SayHelloAsync(
            [ActivityTrigger] string name, 
            FunctionContext executionContext,
            CancellationToken cancellationToken = default)
        {
            ILogger logger = executionContext.GetLogger("SayHello");
            await Task.Delay(5000,cancellationToken);
            logger.LogInformation("Saying hello to {name}.", name);
            return $"Hello {name}!";
        }


```