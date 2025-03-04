### Validate JWT (Secure inbound with Entra)

```xml

        <validate-jwt header-name="Authorization" failed-validation-httpcode="401" failed-validation-error-message="Unauthorized. Access token is missing or invalid.">
            <openid-config url="https://login.microsoftonline.com/adminintegrationit.onmicrosoft.com/.well-known/openid-configuration" />
            <audiences>
                <audience>api://329a5b9d-cdb7-4a33-bf01-16295137d404</audience>
            </audiences>
            <required-claims>
                <claim name="roles" match="all">
                    <value>executer</value>
                </claim>
            </required-claims>
        </validate-jwt>

```

### Use Managed identity for out traffic

```xml

<authentication-managed-identity resource="api://329a5b9d-cdb7-4a33-bf01-16295137d404" />

```