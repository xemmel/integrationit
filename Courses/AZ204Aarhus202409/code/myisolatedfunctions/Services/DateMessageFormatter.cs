public class DateMessageFormatter : IMessageFormatter
{


    public string FormatText(string text)
    {
        return $"{DateTime.UtcNow}\t{text}";
    }
}
