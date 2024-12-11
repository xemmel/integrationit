
public class AngryGreeter : IGreetHandler
{
    private readonly IStringFormatter _stringFormatter;

    public AngryGreeter(IStringFormatter stringFormatter)
    {
        _stringFormatter = stringFormatter;
    }
    public async Task<string> GetGreetingAsync(CancellationToken cancellationToken = default)
    {
        return _stringFormatter.FormatString("Have a very rotten day");
    }
}