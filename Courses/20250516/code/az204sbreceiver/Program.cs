using Azure.Identity;
using Azure.Messaging.ServiceBus;

var credential = new DefaultAzureCredential();
string serviceBusNamespace = "myqueues";

string topicName = "topic1";
string subscriptionName = "getall";

int maxMessages = int.Parse(args[0]);
int maxWaitSeconds = 30;

TimeSpan maxWaitTime = new TimeSpan(0, 0, maxWaitSeconds);

var optionsc = new ServiceBusClientOptions
{
 TransportType = ServiceBusTransportType.AmqpTcp
};
var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{serviceBusNamespace}.servicebus.windows.net",
        credential: credential, options: optionsc);

var options = new ServiceBusReceiverOptions
{
    ReceiveMode = ServiceBusReceiveMode.PeekLock
};

var receiver = client.CreateReceiver(topicName, subscriptionName,options);


var messages = await receiver.ReceiveMessagesAsync(
        maxMessages: maxMessages,
        maxWaitTime: maxWaitTime);

foreach (var message in messages)
{
    try
    {
        System.Console.WriteLine(message.Body.ToString());
        //await receiver.CompleteMessageAsync(message);
    }
    catch (System.Exception)
    {

        await receiver.AbandonMessageAsync(message);
    }
    
}