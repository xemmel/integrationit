using System.Net.Http.Headers;
using Azure.Identity;
using Azure.Messaging.ServiceBus;

string topicName = "mytopic";
string subName = "getall";
string nsName = "aismlcdemo";

int maxMessages = int.Parse(args[0]);
var credential = new DefaultAzureCredential();

var client = new ServiceBusClient(fullyQualifiedNamespace:$"{nsName}.servicebus.windows.net",credential: credential);

var options = new ServiceBusReceiverOptions
{
  ReceiveMode = ServiceBusReceiveMode.PeekLock
};
var receiver = client.CreateReceiver(topicName: topicName, subscriptionName: subName,options: options);
var messages = await receiver.ReceiveMessagesAsync(maxMessages: maxMessages,maxWaitTime: new TimeSpan(0,0,10));
foreach(var message in messages)
{
    System.Console.WriteLine($"Received Message: {message.Body.ToString()}");    
}