using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace falckfunctions
{
    public class myqueuetrigger
    {
        private readonly ILogger<myqueuetrigger> _logger;

        public myqueuetrigger(ILogger<myqueuetrigger> logger)
        {
            _logger = logger;
        }

        [Function(nameof(myqueuetrigger))]
        [QueueOutput("outputqueue", Connection = "externalstorage")]
        public Order Run([QueueTrigger("inputqueue", Connection = "externalstorage")] QueueMessage message)
        {
            _logger.LogInformation($"C# Queue trigger function processed: {message.MessageText}");
            string orderId = message.MessageText.Split('/')[0];
            int qty = int.Parse(message.MessageText.Split('/')[1]);

            var order = new Order
            {
                OrderId = orderId,
                Qty = qty
            };
            return order;
        }
    }
}
