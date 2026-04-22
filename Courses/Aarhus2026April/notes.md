## Notes

### Create dotnet solution and project

```powershell

dotnet new sln -o storagetest
cd storagetest
dotnet sln add storagetest
dotnet new console -o storagetest
cd storagetest
dotnet add package Azure.Storage.Blobs
cd ..
code .

```

### Regions and Storage Account

```

Region/location


West Europe
Denmark East




Region Pair


West Europe <-> North Europe

Availability Zones  (3+ Data Centre)

LRS -> Local    (1 data centre, 3 disks)
GRS -> Geo      (1 data centra, 3 disks) -> 1 disk "region pair"
ZRS -> Zone    (3 data centre, 1 disk each)




Blobs (Files)

- Hot
- Cool
- Cold
- Archieved

```

### Install Azure Cli

```powershell

winget install Microsoft.Powershell

- close existing PowerShell
- Open terminal
- Settings -> Default Profile -> Black Powershell -> Save
- Close/Open Terminal
- Open (7.6.0)

## Install Azure CLI

winget install Microsoft.AzureCLI

az login --use-device-code

az group list -o table

```

### Azure CLI


```powershell

az group create --name rg-bla-bla

Azure Powershell  (PS Native)

new-azresourcegroup -name rg-bla-bla


### Create new Resource Group

$location = "germanywestcentral"

az group create `
  --name rg-az204-mlc-demo02 `
  --location $location

```

### Deploy Web app from code

```powershell

$rgName = "rg-az204-demo01-web"
$webAppName = "az204mlc2"

Write-Host("Removing existing published files");

if (Test-Path .\publish\) {
    Get-Item .\publish\ | Remove-Item -Recurse -Force
}

if (Test-Path .\publish.zip) {
    Get-Item .\publish.zip | Remove-Item -Recurse -Force
}


Write-Host("Build/Publish .NET code");

dotnet publish -c Release -o ./publish

Write-Host("Zip..");

cd .\publish
Compress-Archive -Force -Path * -DestinationPath ..\publish.zip
cd ..

 az webapp deploy `
        --resource-group $rgName `
        --name $webAppName `
        --src-path ./publish.zip `
        --slot pre

```

### OAuth2 token notes

```

HTTP Azure 
   -> HTTP Entra
        -> Please give me a token  (Login password MFA)
token        <- Token (user token)

   -> HTTP Azure
        HTTP Header
           Authorization: Bearer token


HTTP GET /
https://management.azure.com/subscriptions/
9bc198aa-089c-4698-a7ef-8af058b48d90/resourcegroups?api-version=2021-04-01

az account get-access-token --resource https://management.azure.com/

- storage account

https://storage.azure.com/

- service bus

https://servicebus.azure.net/

```

### Use EnvironmentCredential in Powershell

```powershell

$ENV:AZURE_TENANT_ID = "551...";
$ENV:AZURE_CLIENT_ID = "684...";
$ENV:AZURE_CLIENT_SECRET = "VEt....";

```


### Function app notes

```

Service Bus Namespace (MQ) $$
    - Queue
    - Queue
    - Topic


Storage Account Queues -> $


Azure Function App -> Azure Resource  -> Web App    
     ->Internal System Storage Account


   - Function  (TimerTrigger)  -> Code C#, python, PS
   - Function  (HttpTrigger)
   - Function  (QueueTrigger)
   - DbTrigger
   - BlobTrigger (


Function App = C# Project .csproj
   Function -> C# Class .cs


func init FunctionApp --worker-runtime dotnet-isolated  --target-framework net10.0

```



## WSL

```powershell



wsl --install Ubuntu-24.04

password cannot be "admin"

```

### WSL Install Kali

```powershell

wsl --install kali-linux

sudo apt install kali-linux-default -y


```

### Setup docker and multipass

```bash

### Make passwordless sudo

sudo visudo

%sudo   ALL=(ALL:ALL) ALL
->
%sudo   ALL=(ALL:ALL) NOPASSWD:ALL

CRTL+X
Y

sudo apt update
sudo apt upgrade -y

sudo apt install docker.io -y
sudo usermod -aG docker $USER
newgrp docker


sudo snap install multipass

```

### Create Multipass server

```bash

sudo iptables -P FORWARD ACCEPT

multipass launch --name server1 --memory 4GB --cpus 2 --disk 20GB devel

multipass shell server1

sudo apt update && sudo apt upgrade -y

```

### Install dotnet SDK Ubuntu

```bash

sudo apt-get update && \
  sudo apt-get install -y dotnet-sdk-10.0

```

### Install Azure CLI Ubuntu

```bash

curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

```

### Delete all unwanted Resource Group

```powershell

 az group list -o json | ConvertFrom-Json | Out-GridView -PassThru | ForEach-Object {az group delete --name $_.name --yes --no-wait}

```

### Managed Indentity in Function App Configuration

```
"ServiceBusConnection__fullyQualifiedNamespace" : "az204mlcqueues.servicebus.windows.net"
```