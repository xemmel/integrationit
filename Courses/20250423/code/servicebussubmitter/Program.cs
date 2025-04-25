
using Azure.Identity;
using Azure.Messaging.ServiceBus;

string sbNamespace = "az204mlc";
string queueName = "mytopic";

string country = args[0];
int messageCount = int.Parse(args[1]);

var credential = new DefaultAzureCredential();

var client = new ServiceBusClient(
    fullyQualifiedNamespace: $"{sbNamespace}.servicebus.windows.net",
    credential: credential);


var sender = client.CreateSender(queueName);


for (int i = 1; i <= messageCount; i++)
{
    var message = new ServiceBusMessage($"Message {i}");
    message.ApplicationProperties.Add("country", country);

    await sender.SendMessageAsync(message);
    System.Console.WriteLine($"Message {i} sent...");
}

