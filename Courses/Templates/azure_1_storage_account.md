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
   ![Create Resource Group](/Images/ChooseAdvancedSA.png)
  - **Review + create**
  - **Create** 

