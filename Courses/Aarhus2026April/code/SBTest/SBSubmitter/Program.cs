
using Azure.Identity;
using Azure.Messaging.ServiceBus;

var serviceBusNamespace = "az204mlcqueues";

var queueName = "topic1";


string country = args[0];
int count = int.Parse(args[1]);

var credential = new DefaultAzureCredential();

var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{serviceBusNamespace}.servicebus.windows.net",
        credential: credential);

var sender = client.CreateSender(queueName);
for (int i = 1; i <= count; i++)
{
    string messageBody = $"Message: {i}";
    var message = new ServiceBusMessage(messageBody);
    message.ApplicationProperties.Add("MessageNumber",i);
    message.ApplicationProperties.Add("country", country);
    await sender.SendMessageAsync(message);
    System.Console.WriteLine($"Message '{messageBody}' sent....");
}
