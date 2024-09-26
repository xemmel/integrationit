
public class AngryGreetingHandler : IGreetingHandler
{
    private readonly IMessageFormatter _messageFormatter;

    public AngryGreetingHandler(IMessageFormatter messageFormatter)
    {
        _messageFormatter = messageFormatter;
    }

    public async Task<string> GetGreetingAsync(CancellationToken cancellationToken = default)
    {
        var orgMessage = "Have a very rotten day";
        var formattedMessage = _messageFormatter.FormatText(orgMessage);
        return formattedMessage;
    }
}