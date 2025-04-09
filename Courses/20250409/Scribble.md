Cert:

Multi-choose


Choose one

Choose all  

Drag-drop   use cli to create a resource group

Case

group questions
 
fd fdfdfd fdfd and you also remem..
do you meet the requirement

yes/no

az group create --name rg-ffff --location westeurope



azure cli / Azure powershell




### Storage

LRS -> Local  (1 random DC  -> 3 disks)

GRS -> GEO  (1 random DC -> 3 disks) -> async backup (Region Pair) (1 disk)

ZRS -> Zone (all "3" DC -> 1 disk in each)

GZRS -> Combo



Storage Account --- 0$


1 TB 100$

1 SA 1 TB


2 SA 1/2 TB


----------------------

4 resources in 1

Container/Blob Storage (Default) (HTTP based file system)
(Folder/File)

http://ffdffd/image.jpg

<img src="https://fdfffd/image.jpg" />



Disk Storage
Queue Storage
Table Storage

----------------------

Blob!!!

Hot (default)   
Cool
Cold
Archive


          MB        Pr trans (read/write)
Hot       $$$            $
Cool       $$            $$
Cold        $/4          $$$ online (cost for asking for it)
Arch     $/10         offline (request 1 hour) cost for bringing back




Containers:

maps
schemas
del-lifedata



Sub
    RG (Choose Region/Location) -> Activity Log
       Resources (Almost every)(Choose Region/Location)



Region/Location -> The location of the datacenter that the resource will....


     RG (Australia)
         Res1 (Eu)
         Res2 (Us)

Region:

    - Compliance (West Europe)
    - Latency
    - FailOver (Manual)
    - Versioning (AI)
    - Pricing

Region Pairs
    - Region1  <-> Region2

Avalibilty Zones
   Denmark East
     3 DC

--------------------

NAMING!!!

Resource Group
ID: Globally unique
/SubscriptionId/ResourceGroupName

/Sub1/rgname1
/Sub2/rgname1


Resources

ID: Glob unique

/SubId/RgName/Type(Vm,disk,webapp,logicapp)/ResourceName

test,prod

/subtest/appx/vm/vm1 :-)
/subtest/appx/disk/vm1 :-)

/subtest/appx/vm/vm1 :-(

/subprod/appx/vm/vm1 :-)




falckdkappx :-)   (TEST)


falckdkappx :-(

/subtest/appy/vm/vm1 :-)



             ENTRA (AAD) (Identity Provider) MS (SaaS)
                  (Authentication)  (Who are you, prove)
                  (Tenant) -> Domain (falck.dk)


- Azure knows Entra, Entra has no knowledge of Azure!

    AZURE
    SUBSCRIPTION (Trusts single Entra Tenant)
     - Sub1
     - Sub2
     (Authorization    RBAC / Role Assignments (DB) -> entraId )
 

              O365 (SaaS)   DEVOPS    APP

- Management Group (Policy, Security)
   - Azure Subscriptions
       - Resource Groups (File Folder!!) -> Cannot be nested
           - Resources ($) (VM, Function App, Logic App, Db) <- Resources

Policy (Allowed Region, HTTPS, no HTTP TLS1.2)
   - Informative, Enforce

       Existing Resource will NOT be affected even with Enforsive


       - AppX (Delete)
           - WebApp
           - Storage Account

           - template deployment <-> 

       - RG1 
           - Resource11
           - Resource12
           - Morten!!!

       - RG2
           - Resource21
           - Morten

150 resource

     RG
        150



     150 RG -> 1 resource in each



AZURE!!!


- Microsoft
- Cloud (Public) *
   - Multi tenant
   - MANAGEMENT part is access. through the Internet

- Microsoft's Public Cloud Offering for IaaS (VM) and PaaS (WebApps/Man Db) products/services
   - Compute (+- Software)
   - Storage (Db)
   - Networking
   - AI (Marketing)


  - Entra (AAD)
  - OD365
  - Azure DevOps (Microsoft DevOps)
  - Azure





