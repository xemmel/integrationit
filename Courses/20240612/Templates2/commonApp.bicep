param appName string
param companyShortName string
param env string
param location string = resourceGroup().location

var fullName = '${appName}-common-${env}'
var shortFullName = '${appName}common${env}'

var fullUniqueName = '${appName}-${companyShortName}-${env}'
var fullUniqueStandardName = '${appName}${companyShortName}${env}'


//Log Analytics Workspace
var workspaceName = 'log-${fullName}'
module workspace 'Common/logAnalyticsWorkspace.bicep' = {
  name: 'workspace'
  params: {
    location: location
    retention: 180
    workspaceName: workspaceName
  }
}

//App Service Plan
var planName = 'asp-${fullName}'
module plan 'Common/appServicePlan.bicep' = {
  name: 'plan'
  params: {
    location: location
    appServicePlanName: planName
  }
}
