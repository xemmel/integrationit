using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace FunctionApp;

public class ProcessInput
{
    private readonly ILogger<ProcessInput> _logger;

    public ProcessInput(ILogger<ProcessInput> logger)
    {
        _logger = logger;
    }

    [Function(nameof(ProcessInput))]
    [QueueOutput("middlequeue", Connection = "StorageAccountConnection")]
    public SalesOrder Run([QueueTrigger("inputqueue", Connection = "StorageAccountConnection")] QueueMessage message)
    {
        int qty = int.Parse(message.MessageText);
        
        _logger.LogInformation("Quantity ordered: {qty}",qty);
        var order = new SalesOrder();
        order.Qty = qty;
        order.OrderId = Guid.NewGuid().ToString();

        return order;
    }
}