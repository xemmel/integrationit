using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace newfunctions
{
    public class FinalProcess
    {
        private readonly ILogger<FinalProcess> _logger;

        public FinalProcess(ILogger<FinalProcess> logger)
        {
            _logger = logger;
        }

        [Function(nameof(FinalProcess))]
        [QueueOutput("erpqueue", Connection = "orderstorageaccount")]
        public Order Run([QueueTrigger("middlequeue", Connection = "orderstorageaccount")] Order order)
        {
           // _logger.LogInformation($"C# Queue trigger function processed: {message.MessageText}");
           order.Qty++;
           return order;
        }
    }
}
