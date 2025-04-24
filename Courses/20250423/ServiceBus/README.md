```powershell

dotnet new console -o servicebussubmitter
cd servicebussubmitter
dotnet add package Azure.Messaging.ServiceBus
dotnet add package Azure.Identity

```

```csharp

using Azure.Identity;
using Azure.Messaging.ServiceBus;

string sbNamespace = "az204mlc";
string queueName = "mytopic";

string country = args[0];
var credential = new DefaultAzureCredential();

var client = new ServiceBusClient(
    fullyQualifiedNamespace: $"{sbNamespace}.servicebus.windows.net",
    credential : credential);


var sender = client.CreateSender(queueName);

var message = new ServiceBusMessage("Hello from app");
message.ApplicationProperties.Add("country",country);

await sender.SendMessageAsync(message);
System.Console.WriteLine("Message sent...");

```