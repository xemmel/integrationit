public class FunnyMessageFormatter : IMessageFormatter
{
    public string FormatText(string text)
    {
        return $"This is fun\t{text}";
    }
}
