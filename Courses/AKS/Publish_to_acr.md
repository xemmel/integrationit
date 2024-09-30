### Publish

```powershell

### You need to be in the folder with the DockerFile

$imageName = "aksapis";
$version = "1.1";


$version = Read-Host("version");
az acr build `
  --registry "acr${appName}${yourinit}" `
  --image  "acr${appName}${yourinit}.azurecr.io/${imageName}:${version}" `
  --subscription $subscriptionId .


```


### deployment

```powershell

## integrationit\Courses\AKS>

$namespace = $imageName;

kubectl create namespace $namespace;
kubectl config set-context --current --namespace $namespace;



kubectl apply --filename .\templates\aksapis\deployment.yaml

```

### Test curl pod (removed)

```powershell

kubectl run tester-pod --image curlimages/curl --rm -it /bin/sh

### For alias

k run tester-pod --image curlimages/curl --rm -it /bin/sh

```