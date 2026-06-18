using Azure.Identity;
using Azure.Messaging.ServiceBus;

var credential = new DefaultAzureCredential();
int maxMessages = int.Parse(args[0]);
TimeSpan timeToWait = new TimeSpan(0,0,20);

string serviceBusNamespaceName = "aismlcqueues";

var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{serviceBusNamespaceName}.servicebus.windows.net",
        credential: credential);


var options = new ServiceBusReceiverOptions
{
    ReceiveMode = ServiceBusReceiveMode.PeekLock
};

var receiver = client.CreateReceiver("queue1",options);

//TODO
var messages = await receiver.ReceiveMessagesAsync(maxMessages: maxMessages,maxWaitTime: timeToWait);
foreach(var message in messages)
{   try
{
    System.Console.WriteLine($"Message received: {message.Body}");
    //await receiver.CompleteMessageAsync(message);

}
catch (System.Exception)
{
    
    await receiver.AbandonMessageAsync(message);
}
    
}
