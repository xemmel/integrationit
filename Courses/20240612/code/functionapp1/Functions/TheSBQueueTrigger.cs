using System;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Extensions.Logging;

namespace functionapp1
{
    public class TheSBQueueTrigger
    {
        [FunctionName("TheSBQueueTrigger")]
        [return: ServiceBus("myoutputqueue", Connection = "thesbconnection")]
        public string Run([ServiceBusTrigger("myqueue", Connection = "thesbconnection")]string myQueueItem, ILogger log)
        {
            log.LogInformation($"C# ServiceBus queue trigger function processed message: {myQueueItem}");
            string result = $"This message has been processed: {myQueueItem}";
            return result;
        }
    }
}
