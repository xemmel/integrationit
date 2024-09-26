using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace myisolatedfunctions
{
    public class startprocessingorders
    {
        private readonly ILogger<startprocessingorders> _logger;

        public startprocessingorders(ILogger<startprocessingorders> logger)
        {
            _logger = logger;
        }

        [Function(nameof(startprocessingorders))]
        [QueueOutput("middlequeue", Connection = "externalStorageConnection")]
        public string Run([QueueTrigger("inputorder", Connection = "externalStorageConnection")] QueueMessage message)
        {
            _logger.LogInformation($"C# Queue trigger function processed: {message.MessageText}");
            int qty = int.Parse(message.MessageText);
            string output = $"You ordered {qty} items";
            return output;
        }
    }
}
