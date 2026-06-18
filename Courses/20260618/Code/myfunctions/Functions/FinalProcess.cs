using System;
using Azure.Storage.Queues.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace myfunctions;

public class FinalProcess
{
    private readonly ILogger<FinalProcess> _logger;
    private readonly IProcessOrderService _processOrderService;

    public FinalProcess(ILogger<FinalProcess> logger, IProcessOrderService processOrderService)
    {
        _logger = logger;
        _processOrderService = processOrderService;
    }

    [Function(nameof(FinalProcess))]
    [QueueOutput("finalqueue", Connection = "externalstorageconnection")]
    public async Task<Order> RunAsync(
        [QueueTrigger("middlequeue", Connection = "externalstorageconnection")] Order order,
        CancellationToken cancellationToken)
    {
        order = await _processOrderService.ProcessOrderAsync(order,cancellationToken);
        return order;

    }
}