using System;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace falckfunctions
{
    public class mytimertrigger
    {
        private readonly ILogger _logger;

        public mytimertrigger(ILoggerFactory loggerFactory)
        {
            _logger = loggerFactory.CreateLogger<mytimertrigger>();
        }

        //[Function("mytimertrigger")]
        public void Run([TimerTrigger("%timerschedule%")] TimerInfo myTimer)
        {
            _logger.LogInformation($"C# Timer trigger function executed at: {DateTime.Now}");
            
            if (myTimer.ScheduleStatus is not null)
            {
                _logger.LogInformation($"Next timer schedule at: {myTimer.ScheduleStatus.Next}");
                _logger.LogInformation($"Next timer schedule at: {myTimer.ScheduleStatus.Last}");

            }

            //Call API
            //Http get stuff ?from=myTimer.ScheduleStatus.Last

            //If null then get everything? Or get nothing

        }
    }
}
