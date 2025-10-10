## Get requests

```

AppRequests
| where TimeGenerated > ago(1h)
| where Name == 'calculator'
| project TimeGenerated,Success,DurationMs,OperationId
| order by TimeGenerated desc

```

## Summarize success as piechart

```

AppRequests
| where TimeGenerated > ago(1h)
| where Name == 'calculator'
| summarize count() by tostring(Success)
| render piechart 

```

## Summarize executions by time and success

```

AppRequests
| where TimeGenerated > ago(1h)
| where Name == 'calculator'
| summarize count() by bin(TimeGenerated,5m), tostring(Success)
| render barchart 

```

## See Traces and/or Exceptions

```

AppTraces
| where OperationId == 'e29005e80c104142a6438d5c8ebe35ac'


AppExceptions
| where OperationId == 'e29005e80c104142a6438d5c8ebe35ac'

```