param (
    [string]$appName,
    [string]$env,
    [string]$location,
    [string]$companyShortName,
    [string]$queueName,
    [bool]$requiresDuplicateDetection = $false,
    [string]$duplicateDetectionHistoryTimeWindow = 'P1D',
    [int]$maxDeliveryCount = 10
)

$rgName = "rg-${appName}-common-${env}";


az deployment group create `
   --resource-group $rgName `
   --template-file .\appQueue.bicep `
   --parameters appName=$appName `
   --parameters env=$env `
   --parameters companyShortName=$companyShortName `
   --parameters queueName=$queueName `
   --parameters requiresDuplicateDetection=$requiresDuplicateDetection `
   --parameters duplicateDetectionHistoryTimeWindow=$duplicateDetectionHistoryTimeWindow `
   --parameters maxDeliveryCount=$maxDeliveryCount
;


