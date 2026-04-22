public class SpecialSaleOrderHandler : IOrderHandler
{
    public async Task<SalesOrder> ProcessOrderAsync(SalesOrder order, CancellationToken cancellationToken = default)
    {
        order.Qty+=10;
        return order;
    }
}