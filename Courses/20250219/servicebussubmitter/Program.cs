//Submit message to a queue/topic

using Azure.Identity;
using Azure.Messaging.ServiceBus;

//string connectionString = "Endpoint=sb://mlcservicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=tzE/3gh6nU+kcoz++KwTzUlBE42lP2YEx+ASbMDlMsE=";
string topicName = "topic1";
string namespaceName = "mlcservicebus";
//Place content in a blob in Storage Account

var credential = new DefaultAzureCredential();


//Send to Service Bus
var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{namespaceName}.servicebus.windows.net",
        credential: credential);
string messageType = args[0];

var sender = client.CreateSender(topicName);
int count = int.Parse(args[1]);
for (int i = 1; i <= count; i++)
{
    var message = new ServiceBusMessage($"Message {i}");
    message.ApplicationProperties.Add("messageType", messageType);
    await sender.SendMessageAsync(message);
    System.Console.WriteLine($"Message {i} sent...");
}
