using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace myfirstfunctions
{
    public class finalprocess
    {
        private readonly ILogger<finalprocess> _logger;

        public finalprocess(ILogger<finalprocess> logger)
        {
            _logger = logger;
        }

        [Function(nameof(finalprocess))]
        [QueueOutput("finalqueue", Connection = "storageconnection")]
        public Order Run([QueueTrigger("middlequeue", Connection = "storageconnection")]
            Order order)
        {
            order.Qty++;
            return order;
        }
    }
}
