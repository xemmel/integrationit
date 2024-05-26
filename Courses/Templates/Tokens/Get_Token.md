- Run the following script in *Powershell* replace everything needed

```powershell

Clear-Host;

### Replace
$tenantId = "replace";
$audience = "replace";
$clientId = "replace"; ## App Client Id
$clientSecret = "replace";


$scope = "$($audience)/.default";
$url = "https://login.microsoftonline.com/$($tenantId)/oauth2/v2.0/token";

$body = "";
$body += "client_id=$clientId";
$body += "&grant_type=client_credentials";
$body += "&client_secret=$clientSecret";
$body += "&scope=$scope";



$response = $null;
$response = Invoke-WebRequest `
    -Uri $url `
    -Method Post `
    -Body $body
;

$token = $response |
    Select-Object -ExpandProperty Content |
    ConvertFrom-Json |
    Select-Object -ExpandProperty access_token;

$token |Set-Clipboard;

$token;

```