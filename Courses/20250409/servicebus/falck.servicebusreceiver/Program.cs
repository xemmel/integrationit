using Azure.Identity;
using Azure.Messaging.ServiceBus;

string sbNamespace = "falckmlc";
string topicName = "mytopic";
string subscriptionName = "getall";

int maxMessages = 3;
var maxWaitTime = new TimeSpan(0,0,20); //Special!!

string connectionString = "Endpoint=sb://falckml......";
//Service Bus Namespace / Settings / Shared Access Sig / Click on Root.... Copy the connectionString

//var credential = new AzureCliCredential();

// var client = new ServiceBusClient(
//         fullyQualifiedNamespace: $"{sbNamespace}.servicebus.windows.net",
//         credential: credential);

var client = new ServiceBusClient(connectionString);


var options = new ServiceBusReceiverOptions
{
    ReceiveMode = ServiceBusReceiveMode.ReceiveAndDelete
};

var receiver = client.CreateReceiver(
        topicName: topicName,
        subscriptionName: subscriptionName,
        options: options);

var messages = await receiver
            .ReceiveMessagesAsync(
                maxMessages: maxMessages,
                maxWaitTime: maxWaitTime);

foreach(var message in messages)
{
    System.Console.WriteLine(message.Body.ToString());
}
