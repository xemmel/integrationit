
public class HappyGreetingHandler : IGreetingHandler
{
    public async Task<string> GetGreetingAsync(CancellationToken cancellationToken = default)
    {
        return "Have a very nice day";
    }
}