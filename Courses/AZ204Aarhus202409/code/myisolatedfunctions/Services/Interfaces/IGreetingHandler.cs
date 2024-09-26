public interface IGreetingHandler
{
    Task<string> GetGreetingAsync(CancellationToken cancellationToken = default);
}