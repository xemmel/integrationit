### All Requests

```

AppRequests
| where TimeGenerated > ago(2h)
| where Success == false
| project TimeGenerated, Name, Success, DurationMs, PerformanceBucket, OperationId
| order by TimeGenerated desc

```

### Traces

```
AppTraces
| where OperationId  == 'operationid'
| project TimeGenerated, Message, SeverityLevel
| order by TimeGenerated asc

```

### Exceptions

```

AppExceptions
| where OperationId  == 'operationid'
| project TimeGenerated, OuterMessage, InnermostMessage
| order by TimeGenerated asc

```


### Success (Piechart)

```

AppRequests
| where TimeGenerated > ago(2h)
| summarize count() by tostring(Success)
| render piechart 

```

### Executions by time (and success)

```

AppRequests
| where TimeGenerated > ago(2h)
| summarize count() by bin(TimeGenerated, 5m), tostring(Success)
| render barchart 


```
