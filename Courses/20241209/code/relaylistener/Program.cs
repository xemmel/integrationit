using System.Text.Json;
using Azure.Core;
using Microsoft.Azure.Relay;

await MainASync(args);
        
        static async void SomebodyCalled(RelayedHttpListenerContext context)
        {
            //StreamReader sr = new StreamReader(context.Request.InputStream);
            Request req = await JsonSerializer
                        .DeserializeAsync<Request>(
                            utf8Json: context.Request.InputStream,
                            options: new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
            Console.WriteLine($"Somebody called, with the following command: {req.Command}\tFilePath is : {req.FilePath}");
            context.Response.Close();
            return;
            var files = Directory.GetFiles(req.FilePath);
            List<object> resultList = new List<object>();
            foreach (string file in files)
            {
                resultList.Add(new { file = file });
            }

            var resultObject = resultList.ToArray();

            var json =  JsonSerializer
                        .Serialize(value: resultObject, options: new JsonSerializerOptions { WriteIndented = true });
            context.Response.Headers.Add("content-type", "application/json");
            using (var sw = new StreamWriter(context.Response.OutputStream))
            {
                await sw.WriteLineAsync(json);
            }

            context.Response.Close();
        }

        static async Task MainASync(string[] args)
        {
            var listener = GetListener();
            listener.Connecting += (o, e) => { Console.WriteLine("Connecting.."); };
            listener.Online += (o, e) => { Console.WriteLine("Online"); };

            listener.RequestHandler = SomebodyCalled;

            await listener.OpenAsync();

            await Console.In.ReadLineAsync();
        }

        static HybridConnectionListener GetListener()
        {
            string ns = "aismlcrelay.servicebus.windows.net";
            string hc = "myconnection";

            var listener = new HybridConnectionListener
                (new Uri(String.Format("sb://{0}/{1}", ns, hc)),
                GetTokenProvider());
            return listener;
        }

        static TokenProvider GetTokenProvider()
        {
            string kn = "Listener";
            string k = "...";
            var result = TokenProvider.CreateSharedAccessSignatureTokenProvider(kn, k);
            return result;
        }

        public class Request
    {
        public string Command { get; set; }
        public string FilePath { get; set; }

    }