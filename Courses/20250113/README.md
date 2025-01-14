```powershell

dotnet nuget add source https://api.nuget.org/v3/index.json -n nuget.org

dotnet new console -o TextAI
cd TextAI

dotnet add package Azure.AI.Translation.Text

dotnet run da "Today is Tuesday"

```


```csharp

using Azure;
using Azure.AI.Translation.Text;

string targetLanguage = args[0];
string sourceText = args[1];

var key = "....";
var endpoint = "https://----.cognitiveservices.azure.com/";

AzureKeyCredential credential = new AzureKeyCredential(key);
var client = new TextTranslationClient(
    credential: credential,
    endpoint: new Uri(endpoint));

var result = await client.TranslateAsync(
        targetLanguage: targetLanguage,
        text:sourceText);

System.Console.WriteLine(result?.Value?.FirstOrDefault()?.Translations?.FirstOrDefault()?.Text);



```