- Create a *Web App/App Service* and *App Service Plan* in the same process create new *Resource Group* (**rg-student-*your intitals*-webapp**)
  - Needs a unique name
  - Choose *Code*  *.NET 8 (LTS)* 
  - Choose region 
  - Choose Windows for *Operation System*
  - Under **Pricing Plans** -> **Pricing Plan** select  **Premium V3 P0V3**
  - **Review + create ** -> **Create**

- Make a note of your *Resource Group* and the name or the *Web App*

- Back in your *Web App* go to the *Overview* page (it might take a minute or so to load the first time)
  - Click on **Default domain** and verify that your web app is up and running

- Goto *Developer Tools/App Service Editor*
  - Click *Open Editor*
  - In the left pane under *hostingstart.html* right click and choose **New File**
  - Write some *HTML* stuff <h1>Welcome</h1> etc.
  - This will be auto-saved

- Go back to the web page and refresh. Your newly created *HTML* should now appear.