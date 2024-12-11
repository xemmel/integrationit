using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace myfirstfunctions
{
    public class initprocessqueue
    {
        private readonly ILogger<initprocessqueue> _logger;

        public initprocessqueue(ILogger<initprocessqueue> logger)
        {
            _logger = logger;
        }

        [Function(nameof(initprocessqueue))]
        [QueueOutput("middlequeue",Connection = "externalStorageConnection")]
        public async Task<Invoice> RunAsync([QueueTrigger("initinvoice", Connection = "externalStorageConnection")] QueueMessage message, CancellationToken cancellationToken)
        {
            _logger.LogInformation($"C# Queue trigger function processed: {message.MessageText}");
            int qty = int.Parse(message.MessageText);
            qty++;
            string output = $"Received invoice. Qty is: {qty}";
            _logger.LogInformation(output);
            var invoice = new Invoice
            {
                InvoiceId = Guid.NewGuid().ToString(),
                Qty = qty
            };
            return invoice;

        }
    }
}
