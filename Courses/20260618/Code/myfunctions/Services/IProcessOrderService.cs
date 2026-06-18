public interface IProcessOrderService
{
    Task<Order> ProcessOrderAsync(Order order, CancellationToken cancellationToken = default);
}