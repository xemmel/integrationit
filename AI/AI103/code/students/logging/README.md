### Kusto Query for remote tool execution

```

AppDependencies
| extend gen_ai_agent_name_ = tostring(Properties.["gen_ai.agent.name"])
| where gen_ai_agent_name_ != ''
| project TimeGenerated, gen_ai_agent_name_, PerformanceBucket, OperationId
| order by TimeGenerated desc 

AppDependencies
| extend gen_ai_agent_name_ = tostring(Properties.["gen_ai.agent.name"])
| where gen_ai_agent_name_ != ''
| project TimeGenerated, gen_ai_agent_name_, PerformanceBucket
| summarize count() by PerformanceBucket
| render piechart 

| order by TimeGenerated desc 


AppDependencies
| where Data == "execute_tool"
| extend ToolName = tostring(Properties["gen_ai.tool.name"])
| extend ToolArguments = tostring(Properties["gen_ai.tool.call.arguments"])
| project TimeGenerated, ToolName, ToolArguments, OperationId
| order by TimeGenerated desc

```