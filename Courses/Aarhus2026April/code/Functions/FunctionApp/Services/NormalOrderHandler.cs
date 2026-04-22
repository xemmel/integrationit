public class NormalOrderHandler : IOrderHandler
{
    public async Task<SalesOrder> ProcessOrderAsync(SalesOrder order, CancellationToken cancellationToken = default)
    {
        order.Qty++;
        return order;
    }
}