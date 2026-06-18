using Azure.Identity;
using Azure.Messaging.ServiceBus;

var credential = new DefaultAzureCredential();

int count = int.Parse(args[0]);

string serviceBusNamespaceName = "aismlcqueues";

var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{serviceBusNamespaceName}.servicebus.windows.net",
        credential: credential);

var sender = client.CreateSender("queue1");

for (int i = 1; i <= count; i++)
{
    string messageText = $"Message: {i}";
    var message = new ServiceBusMessage(messageText);

    await sender.SendMessageAsync(message);
    System.Console.WriteLine($"Message: '{messageText}' sent..");
}


