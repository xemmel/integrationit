Morten la Cour
lacour@gmail.com

### Cert prep

```

customer1-free


<rate-limit calls="5" renewal-period="30" />

customer2-premium




<authentication-managed-identity resource="https://storage.azure.com/" />

validate-jwt


<validate-jwt header-name="Authorization" failed-validation-httpcode="401" failed-validation-error-message="Unauthorized. Access token is missing or invalid.">
    <openid-config url="https://login.microsoftonline.com/adminintegrationit.onmicrosoft.com/.well-known/openid-configuration" />
    <audiences>
        <audience>api://8f494144-773a-47ca-87ce-f7b2df045e5f</audience>
    </audiences>
    <required-claims>
        <claim name="roles" match="all">
            <value>nonimportantrole</value>
        </claim>
    </required-claims>
</validate-jwt>



- WebServices
- Function App
- Blob Storage
     - Access Tier
         Hot / Cool / Cold / Archive
     - Lifecycle
- CosmosDb (X)
- Containers (Container Instance)
- Authen/Auth
   - Add custom claim (ctry)  -> Groups (limit) (JWT MAX)
- Key Vault / Managed Identity!!
- API Man
- Event Grid / Event HUB (X)
-  Service Bus (MQ)
- Application Insight  (Health Probe)
    Function App
    

WEB APP

 Microsoft.ApplicationInsights.AspNetCore


builder.Services.AddApplicationInsightsTelemetry();


Azure cli

az servicebus namespaces list -o table

az group create --name fdsfd --location rrdre 



```