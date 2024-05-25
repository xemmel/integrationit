- Run in *Powershell* as Administrator
### Install Chocolatey

```powershell


Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))


```

### Install Powershell Core (should be used over classic Powershell)

```powershell

### Chocolatey

choco install powershell-core -y

### winget 

winget install Microsoft.PowerShell --silent

```

### Install Azure CLI

```powershell

### Chocolatey
choco install azure-cli -y

### winget

winget install Microsoft.AzureCLI --silent

```

#### Azure CLI Login

- Use *--use-device-code* if you are logged in in *private mode* or in a non-default browser

```powershell

az login --use-device-code

```

### Install Dotnet SDK 8

```powershell

## Chocolatey (newest released)

choco install dotnet-sdk -y

## winget

winget install Microsoft.DotNet.SDK.8 --silent


```


### Install Azure Functions Core Tools

```powershell

### Chocolatey

choco install azure-functions-core-tools -y

### winget

winget install  Microsoft.Azure.FunctionsCoreTools --silent

```