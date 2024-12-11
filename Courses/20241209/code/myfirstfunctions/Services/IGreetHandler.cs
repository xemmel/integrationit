public interface IGreetHandler
{
    Task<string> GetGreetingAsync(CancellationToken cancellationToken = default);
}