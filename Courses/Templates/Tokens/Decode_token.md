- Run the following in *Powershell* be sure that $token is set

```powershell

Clear-Host;

function UnixDate()
{
    [datetime]$origin = '1970-01-01 00:00:00'
    $origin.AddSeconds($args[0]).ToLocalTime()

}
Clear-Host;

$p = $token.Split('.');
$parts = $p[1];
if (($parts.Length % 4) -ne 0) {
    if (($parts.Length % 4) -eq 1) {
        $parts += "===";
    }
        if (($parts.Length % 4) -eq 2) {
        $parts += "==";
    }
            if (($parts.Length % 4) -eq 3) {
        $parts += "=";
    }
}

$body = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($parts)) | ConvertFrom-Json | ConvertTo-Json;
$body;

$claims = $body | ConvertFrom-Json;
$expClaims = $claims.exp;
Write-Host "Expire: $(UnixDate($expClaims))"
$isaClaims = $claims.iat;
Write-Host "Issued: $(UnixDate($isaClaims))"
;

```