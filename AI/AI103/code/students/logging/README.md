### Kusto Query for remote tool execution

```

AppDependencies
| where Data == "execute_tool"
| extend ToolName = tostring(Properties["gen_ai.tool.name"])
| extend ToolArguments = tostring(Properties["gen_ai.tool.call.arguments"])
| project TimeGenerated, ToolName, ToolArguments
| order by TimeGenerated desc

```