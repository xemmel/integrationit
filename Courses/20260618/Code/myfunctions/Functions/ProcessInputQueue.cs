using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace myfunctions;

public class ProcessInputQueue
{
    private readonly ILogger<ProcessInputQueue> _logger;

    public ProcessInputQueue(ILogger<ProcessInputQueue> logger)
    {
        _logger = logger;
    }

    [Function(nameof(ProcessInputQueue))]
    [QueueOutput("middlequeue", Connection = "externalstorageconnection")]
    public Order Run([QueueTrigger("inputqueue", Connection = "externalstorageconnection")] QueueMessage message)
    {
        
        _logger.LogInformation("C# Queue trigger function processed: {messageText}", message.MessageText);
        int qty = int.Parse(message.MessageText);
        var order = new Order
        {
            OrderId = Guid.NewGuid().ToString(),
            Qty = qty
        };
        return order;
    }
}