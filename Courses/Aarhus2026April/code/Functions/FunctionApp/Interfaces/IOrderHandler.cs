public interface IOrderHandler
{
    Task<SalesOrder> ProcessOrderAsync(SalesOrder order, CancellationToken cancellationToken = default);
}