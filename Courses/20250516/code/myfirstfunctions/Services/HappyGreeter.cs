
public class HappyGreeter : IGreeter
{
    public async Task<string> GetGreetingAsync(CancellationToken cancellationToken = default)
    {
        return "Hello have a nice day";
    }
}
