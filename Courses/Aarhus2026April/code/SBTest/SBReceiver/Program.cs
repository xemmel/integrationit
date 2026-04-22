using Azure.Identity;
using Azure.Messaging.ServiceBus;

var serviceBusNamespace = "az204mlcqueues";

var topicName = "topic1";
var subscriptionName = "getallmessages";

int maxMessages = int.Parse(args[0]);

TimeSpan maxWaitTime = new TimeSpan(0, 0, 20);

var credential = new DefaultAzureCredential();

var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{serviceBusNamespace}.servicebus.windows.net",
        credential: credential);


var options = new ServiceBusReceiverOptions()
{
    ReceiveMode = ServiceBusReceiveMode.PeekLock
};

var receiver = client.CreateReceiver(topicName, subscriptionName, options: options);

var messages = await receiver.ReceiveMessagesAsync(
        maxMessages: maxMessages, maxWaitTime: maxWaitTime);


foreach (var message in messages)
{
    try
    {
        int messageNumber = (int)message.ApplicationProperties["MessageNumber"];
        bool acceptMessage = (messageNumber % 2) == 0;
        var content = message.Body.ToString();
        if (!acceptMessage)
        {
            await receiver.AbandonMessageAsync(message);
            System.Console.WriteLine($"Abandoned message: '{content}");
            continue;
        }

        System.Console.WriteLine($"Received message '{content}'");
        await receiver.CompleteMessageAsync(message);
        System.Console.WriteLine($"Completed message");
    }
    catch (System.Exception ex)
    {
        System.Console.WriteLine(ex.Message);
        await receiver.AbandonMessageAsync(message);
    }

}