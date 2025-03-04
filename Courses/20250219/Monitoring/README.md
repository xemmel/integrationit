```

### View all requests within 10 m

AppRequests
| where TimeGenerated > ago(10m)
| where Name == "Calculator"
| project TimeGenerated, Success,DurationMs, OperationId
| order by TimeGenerated desc


### View custom logged properties by piechart

AppTraces
| extend prop__number_ = tostring(Properties.prop__number)
| where prop__number_ != ''
| summarize count() by prop__number_
| render piechart 

### Success/Not by piechart

AppRequests
| where TimeGenerated > ago(20m)
| where Name == "Calculator"
| summarize count() by tostring(Success)
| render piechart 

### Executions (true/false) by time-period

AppRequests
| where TimeGenerated > ago(30m)
| where Name == "Calculator"
| summarize count() by bin(TimeGenerated,2m), tostring(Success)
| render barchart 

### View traces/Exceptions by operationId (single execution)

AppTraces|AppExceptions
| where OperationId == '1111111'

```