- Create a new *Container Registry*
  - Unique name, note the name
  - Pricing tier: Standard
- Once created goto **Settings/Access Keys** and enable *Admin user* (Note: When using *Managed Identities* and *RBAC* this feature should be disabled)
  - Note the *password* and the *username*

- Create a *web api* or use an existing from before. You should have a /version Method
- Inside the project folder create a *.dockerignore* file with the following content

```

bin
obj
publish
publish.zip

``` 

- And a *Dockerfile* containing (replace *nameofproject*)

```

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /source

# copy csproj and restore as distinct layers
COPY *.csproj .
RUN dotnet restore

# copy everything else and build app
COPY . .
WORKDIR /source
RUN dotnet publish -c release -o /app --no-restore

# final stage/image
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
ENV ASPNETCORE_HTTP_PORTS=80
COPY --from=build /app ./
ENTRYPOINT ["dotnet", "nameofproject.dll"]

```

- Now run the following command to build a *container image* and push it to your *ACR* (**Azure Container Registry**) (replace *registryname*)
  - Note: You do **not** need Docker etc. locally to do this, since we are using *ACR* to build the image. Make sure you are logged in in *Azure CLI* and that it is pointing at the correct *Azure Subscription*



```powershell

 az acr build -t mytestapi:1.0 . -r registryname

```
