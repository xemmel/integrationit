- Create a new **Resource Group** in the *Azure Portal*
  - Search for *Resource Groups* in the *Search Task bar* if needed
  ![Create Resource Group](/Images/CreateResourceGroup.png)
  - Click **+ Create**
  - Choose correct *Subcription* if not already selected
  - Give the *Resource Group* a name **rg-student-*your intitals*-storageaccount**
  - Choose a *Region* (Could be *Germany West Central*)
  - **Review + create** (Note: no tags are needed, but feel free to experiment with them)
  - **Create** 

- Create new **Storage Account** (Be sure not to choose *Storage Accounts (Classic)*)
  - Choose your newly created *Resource Group*
  - Give the *Storage Account* a unique name
  - Leave all other settings on the **Basics** tab as is
  - Go to the **Advanced** tab and select *Allow enabling anonymous access on individual containers*
   ![Choose Advanced](/Images/ChooseAdvancedSA.png)
  - **Review + create**
  - **Create** 

- Create two new **Containers**
  - Go to the newly create *Storage Account* Left side menu -> **Data storage** -> **Containers**
   - 1 *Container* name: **mypubliccontainer** with **Anonymous access level** set to **Blob (ano..read acces..)**
   - 1 *Container* name: **myprivatecontainer** with **Anonymous access level** set to **Private (no an...)**

- Upload a test file to both *Containers*
  - Create a test txt-file in a local folder, make sure that it contains some text
  - For each container do the following
    - Select the *container* by clicking on it
    - Click the **Upload** icon
    - Either drag the file or *Browse for files*
    - Click **Upload** if you are overwriting an existing file/blob be sure to select *Overwrite ..*
    - Click the uploaded *blob* and copy the **URL** into clipboard
    - Do an **HTTP GET** on the *URL* this can be done in an *Internet Browser*. By using *Postman*. By using the *Rest Client* Extension for *Visual Studio Code* or powershell/bash

```powershell

curl URL

```

  - Note: you should get the blob content from the public container and an *error (not a correct error)* from the private container

  

