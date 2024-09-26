
using Azure.Identity;
using Azure.Messaging.ServiceBus;

string queueName = "mytopic";
string namespaceName = "az204mlc";

var credential = new DefaultAzureCredential();

var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{namespaceName}.servicebus.windows.net",
        credential: credential);

var sender = client.CreateSender(queueName);

string country = args[0];
int count = int.Parse(args[1]);



for (int i = 1; i <= count; i++)
{
    var message = new ServiceBusMessage($"Message: {i}");

    message.ApplicationProperties.Add("country", country);
    await sender.SendMessageAsync(message);
    System.Console.WriteLine($"Message {i} sent...");
}

