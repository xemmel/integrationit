using System;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace myisolatedfunctions
{
    public class thetimer
    {
        private readonly ILogger _logger;

        public thetimer(ILoggerFactory loggerFactory)
        {
            _logger = loggerFactory.CreateLogger<thetimer>();
        }

        [Function("thetimer")]
        public async Task RunAsync([TimerTrigger("0 */1 * * * *")] TimerInfo myTimer,CancellationToken cancellationToken)
        {
            _logger.LogInformation($"C# Timer trigger function executed at: {DateTime.Now}");
            
            if (myTimer.ScheduleStatus is not null)
            {
                _logger.LogInformation($"Next timer schedule at: {myTimer.ScheduleStatus.Next}");
                string url = "https://enxdlxnnlwe6.x.pipedream.net/";
                var client = new HttpClient();
                var response = await client.GetAsync(url,cancellationToken);
                string responseString = await response.Content.ReadAsStringAsync(cancellationToken);    
                _logger.LogInformation($"The response was: {responseString}");
            }
        }
    }
}
