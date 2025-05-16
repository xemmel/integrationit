using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace myfirstfunctions
{
    public class processinputqueue
    {
        private readonly ILogger<processinputqueue> _logger;

        public processinputqueue(ILogger<processinputqueue> logger)
        {
            _logger = logger;
        }

        [Function(nameof(processinputqueue))]
        [QueueOutput("middlequeue", Connection = "storageconnection")]
        public Order Run([QueueTrigger("inputqueue", Connection = "storageconnection")] QueueMessage message)
        {
            _logger.LogInformation($"C# Queue trigger function processed: {message.MessageText}");
            int qty = int.Parse(message.MessageText);
            _logger.LogInformation("Qty ordered is: {qty}", qty);
            var order = new Order
            {
                OrderId = Guid.NewGuid().ToString(),
                Qty = qty
            };
            return order;
        }
    }
}
