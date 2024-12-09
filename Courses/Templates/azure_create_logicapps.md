- Create new *Resource Group* with your initials and ending in *-remove*
- Create a new **Logic App**
  - Choose **Consumption**
  - Click *Select*
  - Choose your *Resource Group*
  - Give the *Logic App*/*Workflow* a name (uniqueness not required but recommended)
  - Choose *Region*
  - Leave *Enable log analytics* as **No**
  - Click **Review + create**
  - Click **Create**

- Once created go to the *Logic App*
- Choose **Developer Tools/Logic app Designer**
   - Click **Add a trigger**
   - In the *Search* field type **http**
   - Do NOT choose the *HTTP* action, but scroll down to the *Request* / *When a HTTP request is received*
      - In the *Method* dropdown choose *POST*
      - Click **Save** and copy the *HTTP URL* and paste it for later use
      - *Collapse* **(>>)** the trigger
      - Click the **+** under the trigger to add an *Action*
      - Search for *response*
      - Choose *Request/Response*
      - In *Body* type *Hello from Logic App*
      - Click **Save**
- In *Postman* make a *POST* call to the *url* collected earlier, and type anything in the *request body*
   - Alternative in *Powershell*
```powershell
### Instead of ...... paste the url of the Logic app
$url = "........." 

curl $url -X POST -d "the body"

```

- Open *Logic app code view*
  - Before the **Response** action, insert a Compose action (Type: *Compose*) (inputs: "hello")
  - Alter the *runAfter* so that your compose shape is executed first and after that the Response
  - Change the **inputs/body** value in the Response action to the output of the Compose
  - Save and execute the *Logic App* again, verify that the response is now only **hello**

- Rules for *definition json*

### Action 

```json
"actionName" : {
    "inputs" : {},
    "type" : "type",
    "runAfter" : { "previousActionName" : [ "Succeeded" ] }
}
```
### Output from previous action
```json
@outputs('actionName')
@body('actionName') -> @outputs('actionName')['body']

```

### Output from trigger

```json
@triggerOutputs()
@triggerBody() -> @triggerOutputs()['body']
```

### Split on (Debatching)

```json
"triggers": {
            "mytrigger": {
                "type": "Request",
                "splitOn" : "@triggerBody()",
                "kind": "Http",
                "inputs": {
                    "method": "POST"
                }
            }
        }
```