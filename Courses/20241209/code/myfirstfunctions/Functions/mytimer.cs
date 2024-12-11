using System;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace myfirstfunctions
{
    public class mytimer
    {
        private readonly ILogger _logger;

        public mytimer(ILoggerFactory loggerFactory)
        {
            _logger = loggerFactory.CreateLogger<mytimer>();
        }

        //[Function("mytimer")]
        public async Task RunAsync([TimerTrigger("0 */1 * * * *")] TimerInfo myTimer, CancellationToken cancellationToken)
        {
            _logger.LogInformation($"C# Timer trigger function executed at: {DateTime.Now}");
            HttpClient client = new HttpClient();
            var response = await client.GetStringAsync("https://webhook.site/7111d749-ede7-4331-a14b-b505c85bd830",cancellationToken);
            
            if (myTimer.ScheduleStatus is not null)
            {
                _logger.LogInformation($"Next timer schedule at: {myTimer.ScheduleStatus.Next}");
            }
        }
    }
}
