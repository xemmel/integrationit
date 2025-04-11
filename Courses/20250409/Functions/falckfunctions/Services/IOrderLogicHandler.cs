public interface IOrderLogicHandler
{
    Task<Order> ProcessOrderAsync(Order order, CancellationToken cancellationToken = default);
}