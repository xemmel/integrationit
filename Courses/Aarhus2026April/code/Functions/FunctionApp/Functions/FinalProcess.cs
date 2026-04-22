using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace FunctionApp;

public class FinalProcess
{
    private readonly ILogger<FinalProcess> _logger;
    private readonly IOrderHandler _orderHandler;

    public FinalProcess(ILogger<FinalProcess> logger, IOrderHandler orderHandler)
    {
        _logger = logger;
        _orderHandler = orderHandler;
    }

    [Function(nameof(FinalProcess))]
    [ServiceBusOutput("finalqueue", Connection = "ServiceBusConnection")]
    public async Task<SalesOrder> RunAsync(
        [QueueTrigger("middlequeue", Connection = "StorageAccountConnection")] SalesOrder order, CancellationToken cancellationToken)
    {
        //_logger.LogInformation("C# Queue trigger function processed: {messageText}", message.MessageText);
        _logger.LogInformation("Received OrderId: {orderId}",order.OrderId);
        order = await _orderHandler.ProcessOrderAsync(order,cancellationToken);
        return order;
    }
}