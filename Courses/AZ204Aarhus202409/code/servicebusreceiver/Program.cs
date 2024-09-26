using Azure.Identity;
using Azure.Messaging.ServiceBus;

string topicName = "mytopic";
string namespaceName = "az204mlc";
string subscriptionName = "logall";

var credential = new DefaultAzureCredential();

var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{namespaceName}.servicebus.windows.net",
        credential: credential);

var options = new ServiceBusReceiverOptions
{
ReceiveMode = ServiceBusReceiveMode.PeekLock
};

var receiver = client.CreateReceiver(topicName,subscriptionName,options);

var messages = await receiver.ReceiveMessagesAsync(maxMessages:10,maxWaitTime: new TimeSpan(0,0,40));

foreach(var message in messages)
{
    System.Console.WriteLine(message.Body.ToString());
}
