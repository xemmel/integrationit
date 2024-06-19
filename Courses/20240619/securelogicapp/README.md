### All APIM policies


#### Assign an API Role to a Managed Identity

```powershell

New-MgServicePrincipalAppRoleAssignment `
    -ServicePrincipalId $serverServicePrincipalObjectId `
    -PrincipalId $managedIdentityObjectId `
    -ResourceId $serverServicePrincipalObjectId `
    -AppRoleId $appRoleId

```

#### API

```xml

<!--
    - Policies are applied in the order they appear.
    - Position <base/> inside a section to inherit policies from the outer scope.
    - Comments within policies are not preserved.
-->
<!-- Add policies as children to the <inbound>, <outbound>, <backend>, and <on-error> elements -->
<policies>
    <!-- Throttle, authorize, validate, cache, or transform the requests -->
    <inbound>
        <base />
        <validate-jwt header-name="Authorization" failed-validation-httpcode="401" failed-validation-error-message="Unauthorized. Access token is missing or invalid.">
            <openid-config url="https://login.microsoftonline.com/adminintegrationit.onmicrosoft.com/.well-known/openid-configuration" />
            <audiences>
                <audience>api://9debe2e4-3adc-4a2e-bd46-e829888bdf91</audience>
            </audiences>
            <required-claims>
                <claim name="roles" match="all">
                    <value>apimexecuter</value>
                </claim>
            </required-claims>
        </validate-jwt>
        <set-header name="test" exists-action="override">
            <value>123</value>
        </set-header>
        <set-header name="invixo-key" exists-action="delete" />
    </inbound>
    <!-- Control if and how the requests are forwarded to services  -->
    <backend>
        <base />
    </backend>
    <!-- Customize the responses -->
    <outbound>
        <base />
    </outbound>
    <!-- Handle exceptions and customize error responses  -->
    <on-error>
        <base />
    </on-error>
</policies>

```


#### Operation


```xml

<!--
    - Policies are applied in the order they appear.
    - Position <base/> inside a section to inherit policies from the outer scope.
    - Comments within policies are not preserved.
-->
<!-- Add policies as children to the <inbound>, <outbound>, <backend>, and <on-error> elements -->
<policies>
    <!-- Throttle, authorize, validate, cache, or transform the requests -->
    <inbound>
        <base />
        <authentication-managed-identity resource="api://e1393207-30df-4e39-b3d4-755ced91f5e7" />
        <set-backend-service base-url="https://prod2-18.germanywestcentral.logic.azure.com:443/workflows/710f0e4c605e48fc944cfb21efabd466/triggers/manual/paths/invoke?api-version=2016-10-01" />
        
    </inbound>
    <!-- Control if and how the requests are forwarded to services  -->
    <backend>
        <base />
    </backend>
    <!-- Customize the responses -->
    <outbound>
        <base />
    </outbound>
    <!-- Handle exceptions and customize error responses  -->
    <on-error>
        <base />
    </on-error>
</policies>

```