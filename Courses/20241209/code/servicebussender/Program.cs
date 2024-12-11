
using Azure.Identity;
using Azure.Messaging.ServiceBus;

string topicName = "mytopic";
string nsName = "aismlcdemo";

string country = args[0];
int count = int.Parse(args[1]);




var credential = new DefaultAzureCredential();

var client = new ServiceBusClient(fullyQualifiedNamespace: $"{nsName}.servicebus.windows.net", credential: credential);

var sender = client.CreateSender(topicName);
for (int i = 1; i <= count; i++)
{
    var message = new ServiceBusMessage($"Message {i}");
    message.ApplicationProperties.Add("country", country);
    message.ApplicationProperties.Add("qty","20f");
    await sender.SendMessageAsync(message);
    System.Console.WriteLine($"Message {i} sent...");
}


//Comm with SA

