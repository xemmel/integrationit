public interface IGreeter
{
    Task<string> GetGreetingAsync(CancellationToken cancellationToken = default);
}