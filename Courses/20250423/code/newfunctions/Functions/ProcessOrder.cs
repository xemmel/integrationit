using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace newfunctions
{
    public class ProcessOrder
    {
        private readonly ILogger<ProcessOrder> _logger;

        public ProcessOrder(ILogger<ProcessOrder> logger)
        {
            _logger = logger;
        }

        [Function(nameof(ProcessOrder))]
        [QueueOutput("middlequeue", Connection = "orderstorageaccount")]
        public Order Run([QueueTrigger("orderqueue", Connection = "orderstorageaccount")] QueueMessage message)
        {
            int qty = int.Parse(message.MessageText);
            _logger.LogInformation($"C# Queue trigger function processed: {message.MessageText}");
            
            var order = new Order();
            order.OrderId = Guid.NewGuid().ToString();
            order.Qty = qty;
            return order;
        }
    }
}
