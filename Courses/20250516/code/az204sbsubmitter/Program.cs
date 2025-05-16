using Azure.Identity;
using Azure.Messaging.ServiceBus;

var credential = new DefaultAzureCredential();
string serviceBusNamespace = "myqueues";

string topicName = "topic1";
string country = args[0];
int count = int.Parse(args[1]);


var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{serviceBusNamespace}.servicebus.windows.net",
        credential: credential);

var sender = client.CreateSender(topicName);
for (int i = 1; i <= count; i++)
{
    string messageContent = $"Message: {i}";
    var message = new ServiceBusMessage(messageContent);
    message.ApplicationProperties.Add("country", country);

    await sender.SendMessageAsync(message);
    System.Console.WriteLine($"Message {messageContent} sent");
}



