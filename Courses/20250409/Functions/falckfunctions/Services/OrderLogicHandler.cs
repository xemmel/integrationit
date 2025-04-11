public class OrderLogicHandler : IOrderLogicHandler
{
    public async Task<Order> ProcessOrderAsync(Order order, CancellationToken cancellationToken = default)
    {
        order.Qty += 2;
        return order;
    }
} 