using System;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace myfirstfunctions
{
    public class mytimer2
    {
        private readonly ILogger _logger;

        public mytimer2(ILoggerFactory loggerFactory)
        {
            _logger = loggerFactory.CreateLogger<mytimer2>();
        }

        //[Function("mytimer2")]
        public void Run([TimerTrigger("0 */1 * * * *")] TimerInfo myTimer)
        {
            _logger.LogInformation($"C# Timer trigger function executed at: {DateTime.Now}");
            
            if (myTimer.ScheduleStatus is not null)
            {
                _logger.LogInformation($"Next timer schedule at: {myTimer.ScheduleStatus.Next}");
            }
        }
    }
}
