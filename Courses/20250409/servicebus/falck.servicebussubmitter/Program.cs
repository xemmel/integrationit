
//Client ???

using Azure.Identity;
using Azure.Messaging.ServiceBus;

string sbNamespace = "falckmlc";
string topicName = "mytopic";
string country = args[0];

var credential = new AzureCliCredential();

var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{sbNamespace}.servicebus.windows.net",
        credential: credential);


var sender = client.CreateSender(topicName);

var message = new ServiceBusMessage("Hello from the app");
message.ApplicationProperties.Add("country",country);

await sender.SendMessageAsync(message);
System.Console.WriteLine("Message sent...");

