## Queries

```

### Get Requests

AppRequests
| where TimeGenerated > ago(1h)
| where Name == 'calculator'
| project TimeGenerated, Success, OperationId


### Success in piechart

AppRequests
| where TimeGenerated > ago(1h)
| where Name == 'calculator'
| summarize count() by tostring(Success)
| render piechart 

### Executings/Success by timeframe

AppRequests
| where TimeGenerated > ago(1h)
| where Name == 'calculator'
| summarize count() by bin(TimeGenerated,2m), tostring(Success)
| render barchart 


### trace single request

AppExceptions
| where OperationId == 'd57837bbccadae78198e533b9407178b'

AppTraces
| where OperationId == 'd57837bbccadae78198e533b9407178b'


```