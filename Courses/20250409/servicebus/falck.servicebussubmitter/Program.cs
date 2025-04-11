
//Client ???

using Azure.Identity;
using Azure.Messaging.ServiceBus;

string sbNamespace = "falckmlc";
string topicName = "mytopic";
string country = args[0];
int numberOfMessages = int.Parse(args[1]);



var credential = new AzureCliCredential();

var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{sbNamespace}.servicebus.windows.net",
        credential: credential);

for (int i = 1; i <= numberOfMessages; i++)
{
    var sender = client.CreateSender(topicName);
    string messageContent = $"Message {i}";
    var message = new ServiceBusMessage(messageContent);
    message.ApplicationProperties.Add("country", country);

    await sender.SendMessageAsync(message);
    System.Console.WriteLine($"Message {messageContent} sent...");

}

