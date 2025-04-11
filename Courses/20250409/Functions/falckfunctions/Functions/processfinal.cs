using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace falckfunctions
{
    public class processfinal
    {
        private readonly ILogger<processfinal> _logger;
        private readonly IOrderLogicHandler _orderLogicHandler;

        public processfinal(ILogger<processfinal> logger, IOrderLogicHandler orderLogicHandler)
        {
            _logger = logger;
            _orderLogicHandler = orderLogicHandler;
        }

        [Function(nameof(processfinal))]
        [QueueOutput("finalqueue", Connection = "externalstorage")]
        public async Task<Order> RunAsync(
            [QueueTrigger("outputqueue", Connection = "externalstorage")] Order order,
            CancellationToken cancellationToken = default)
        {
            _logger.LogInformation($"C# Queue trigger function processed: {order.OrderId}");
            order = await _orderLogicHandler.ProcessOrderAsync(order: order,cancellationToken: cancellationToken);
            return order;
        }
    }
}
