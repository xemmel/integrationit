public class DateStringFormatter : IStringFormatter
{
    public string FormatString(string input)
    {
        return $"{DateTime.Now}\t{input}";
    }
}
