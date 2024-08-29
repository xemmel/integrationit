

dotnet new console -o servicebussubmitter

cd servicebussubmitter

dotnet add package Azure.Messaging.ServiceBus
dotnet add package Azure.Identity



```csharp

using Azure.Identity;
using Azure.Messaging.ServiceBus;

var sbNamespace = "...";
var topicName = "...";
var topicSubscriptionName = "....";




var credential = new DefaultAzureCredential();


var client = new ServiceBusClient(
        fullyQualifiedNamespace: $"{sbNamespace}.servicebus.windows.net",
        credential: credential);

var options = new ServiceBusReceiverOptions
{
    ReceiveMode = ServiceBusReceiveMode.PeekLock 
};
var receiver = client
                    .CreateReceiver(
                            topicName,
                            topicSubscriptionName,
                            options);

var messages = await receiver.ReceiveMessagesAsync(maxMessages: 10,maxWaitTime: new TimeSpan(0,0,30));

foreach(var message in messages)
{
    System.Console.WriteLine(message.Body.ToString());
}

```