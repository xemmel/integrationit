using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace myfirstfunctions
{
    public class finalInvoiceProcess
    {
        private readonly ILogger<finalInvoiceProcess> _logger;

        public finalInvoiceProcess(ILogger<finalInvoiceProcess> logger)
        {
            _logger = logger;
        }

        [Function(nameof(finalInvoiceProcess))]
        [QueueOutput("finalqueue",Connection = "externalStorageConnection")]
        public Invoice Run([QueueTrigger("middlequeue", Connection = "externalStorageConnection")] 
        Invoice invoice)
        {
            invoice.Description = "You have been processed";
            //_logger.LogInformation($"C# Queue trigger function processed: {message.MessageText}");
            return invoice;
        }
    }
}
