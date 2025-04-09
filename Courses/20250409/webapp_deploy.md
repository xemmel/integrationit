
$rgName = "rg-falck-mlc-demo";
$webAppName = "mlcfalck2";

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
;



Blue/green

falck-pre  (few people)

falck 

Swap


Canary

falck 

