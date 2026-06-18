public class ProcessOrderService : IProcessOrderService
{
    public async Task<Order> ProcessOrderAsync(Order order, CancellationToken cancellationToken = default)
    {
        order.Qty++;
        return order;
    }
}