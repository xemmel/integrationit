using Azure.Identity;
using Azure.Messaging.ServiceBus;

string sbNamespace = "az204mlc";
string queueName = "mytopic";
string subscriptionName = "subscription2";
int maxMessages = int.Parse(args[0]);
TimeSpan timeToMaxWait = new TimeSpan(0, 0, 20);

var credential = new DefaultAzureCredential();

var client = new ServiceBusClient(
    fullyQualifiedNamespace: $"{sbNamespace}.servicebus.windows.net",
    credential: credential);

var options = new ServiceBusReceiverOptions
{
    ReceiveMode = ServiceBusReceiveMode.PeekLock
};
var receiver = client.CreateReceiver(
        topicName: queueName,
        subscriptionName: subscriptionName,
        options: options);


// var messages = await receiver.ReceiveMessagesAsync(maxMessages: maxMessages, maxWaitTime: timeToMaxWait);

// foreach (var message in messages)
// {
//     try
//     {
//         System.Console.WriteLine(message.Body.ToString());
//         await receiver.AbandonMessageAsync(message);
//     }
//     catch (System.Exception)
//     {

//         await receiver.AbandonMessageAsync(message);
//     }

// }

await foreach(var message in receiver.ReceiveMessagesAsync())
{
    System.Console.WriteLine(message.Body.ToString());
    await receiver.CompleteMessageAsync(message);
}