```powershell

dotnet new console -o servicebussubmitter

cd servicebussubmitter

dotnet add package Azure.Messaging.ServiceBus
dotnet add package Azure.Identity



## Open visual studio code

code .

```


Program.cs


```csharp

using Azure.Identity;
using Azure.Messaging.ServiceBus;

var sbNamespace = "...";
var queueName = "...";



var credential = new DefaultAzureCredential();


var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{sbNamespace}.servicebus.windows.net",
        credential: credential);


var sender = client.CreateSender(queueName);

var message = new ServiceBusMessage("Hello from Program");

await sender.SendMessageAsync(message: message);
System.Console.WriteLine("Message sent...");

```

```powershell

dotnet run
```