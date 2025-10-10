```powershell

$rgName = "rg-az204-containerapp";
$location = "swedencentral";


## Create Resource Group

az group create --name $rgName --location $location;


## Create Environment

az containerapp env create `
    --name mlccontainerenv `
    --resource-group $rgName `
    --location $location


## Create Container App with image from ACR

az containerapp create `
    --name app77 `
    --resource-group $rgName `
    --environment mlccontainerenv `
--registry-server mlcaz204ac.azurecr.io `
    --image mlcaz204ac.azurecr.io/theapi:1.4 `
    --target-port 80 `
    --ingress 'external' `
    --system-assigned `
    --registry-identity 'system' `
    --query properties.configuration.ingress.fqdn


## Update Container App Image

az containerapp update -n app77 -g $rgName -i mlcaz204ac.azurecr.io/theapi:1.5



### Build container image in ACR

az acr build `
  --registry mlcaz204ac `
  --image mlcaz204ac.azurecr.io/theapi:1.5 .

```

## Dockerfile sample .net

```dockerfile

FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /source


COPY *.csproj .
RUN dotnet restore


COPY . .
RUN dotnet publish -c release -o /app

FROM mcr.microsoft.com/dotnet/aspnet:9.0
WORKDIR /app
COPY --from=build /app ./
ENV ASPNETCORE_HTTP_PORTS=80
ENTRYPOINT ["dotnet", "theapi.dll"]

```