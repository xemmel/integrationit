
using Azure.Identity;
using Azure.Messaging.ServiceBus;

var sbNamespace = "dktvmlc";
var queueName = "myqueue";



var credential = new DefaultAzureCredential();


var  client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{sbNamespace}.servicebus.windows.net",
        credential: credential);


var sender = client.CreateSender(queueName);

var message = new ServiceBusMessage("Hello");

await sender.SendMessageAsync(message);

System.Console.WriteLine("Message sent");




