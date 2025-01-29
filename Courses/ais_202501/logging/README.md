### Last requests

```
AppRequests
| where TimeGenerated > ago(1h)
| where Name == 'Calculator'
| project TimeGenerated, Success, OperationId
| order by TimeGenerated desc

```

### Piechart true/false

```
AppRequests
| where TimeGenerated > ago(1h)
| where Name == 'Calculator'
| summarize count() by tostring(Success)
| render piechart 

```

### Bar chart pr. hours

```

AppRequests
| where TimeGenerated > ago(1h)
| where Name == 'Calculator'
| summarize count() by bin(TimeGenerated,1m), tostring(Success)
| render barchart 

```

