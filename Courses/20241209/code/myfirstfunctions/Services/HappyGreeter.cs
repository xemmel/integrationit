
public class HappyGreeter : IGreetHandler
{
    private readonly IStringFormatter _stringFormatter;

    public HappyGreeter(IStringFormatter stringFormatter)
    {
        _stringFormatter = stringFormatter;
    }
    public async Task<string> GetGreetingAsync(CancellationToken cancellationToken = default)
    {
        return _stringFormatter.FormatString("Have a very nice day");
    }
}