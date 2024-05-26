- Run the following script in *Powershell* replace everything needed

```powershell

Clear-Host;

### Replace
$tenantId = "551c586d-a82d-4526-b186-d061ceaa589e";
$audience = "api://198feb13-f899-4138-988a-e2724fd4555e";
$clientId = "056f00c8-5203-407d-9abf-a6cf9218017e";
$clientSecret = "tYH8Q~QE9cG5eFiLol0EMOlZUGZXKZg1FynLidCm";


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