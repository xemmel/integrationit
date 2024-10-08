using System;
using System.Threading.Tasks;
using Azure.Messaging.ServiceBus;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace managedidentityfunctions
{
    public class queuetrigger
    {
        private readonly ILogger<queuetrigger> _logger;

        public queuetrigger(ILogger<queuetrigger> logger)
        {
            _logger = logger;
        }

        [Function(nameof(queuetrigger))]
        public async Task Run(
            [ServiceBusTrigger("myqueue", Connection = "sbConnection")]
            ServiceBusReceivedMessage message,
            ServiceBusMessageActions messageActions)
        {
            _logger.LogInformation("Message ID: {id}", message.MessageId);
            _logger.LogInformation("Message Body: {body}", message.Body);
            _logger.LogInformation("Message Content-Type: {contentType}", message.ContentType);

            // Complete the message
            await messageActions.CompleteMessageAsync(message);
        }
    }
}
