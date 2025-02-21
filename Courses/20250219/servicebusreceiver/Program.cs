using Azure.Identity;
using Azure.Messaging.ServiceBus;

//string connectionString = "Endpoint=sb://mlcservicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=tzE/3gh6nU+kcoz++KwTzUlBE42lP2YEx+ASbMDlMsE=";
string topicName = "topic1";
string subscription = "getall";
string namespaceName = "mlcservicebus";

int maxMessages = int.Parse(args[0]);
TimeSpan maxWaitTime = new TimeSpan(0,0,40); 

//Place content in a blob in Storage Account

var credential = new ClientSecretCredential(
        tenantId: "551c586d-a82d-4526-b186-d061ceaa589e",
        clientId: "f5b4ef94-1fa5-4896-adc7-a0a0ddd56f63",
        clientSecret: "OWo8Q~zrHK72iahzmIr2NZ2V-34nm9_tjgXv3bi-");

//Send to Service Bus
var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{namespaceName}.servicebus.windows.net",
        credential: credential);
var options = new ServiceBusReceiverOptions
{
    ReceiveMode = ServiceBusReceiveMode.PeekLock
};
var receiver = client.CreateReceiver(
        topicName: topicName,
        subscriptionName: subscription,
        options: options);


var messages = await receiver.ReceiveMessagesAsync(maxMessages: maxMessages,maxWaitTime: maxWaitTime);
foreach(var message in messages)
{
    System.Console.WriteLine(message.Body.ToString());
}