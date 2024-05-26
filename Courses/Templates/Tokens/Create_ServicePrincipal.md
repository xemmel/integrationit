- Create a **Service Principal**/**App Registration** in *Entra* (entra.microsoft.com)
  - In *entra* goto *Applications/App Registrations*
  - Click **+ New registration** give it a name (course[init]sp)
  - Click **Register**
  - Note the *Tenant ID* and *Client ID*
  - Goto **Certificates & secrets**
    - **+ New client secret** Give the secret a name and select 3 months, click **Add**
    - Copy the **Value** (not the **Secret ID**) to somewhere save (local notepad), this value must never be exposed
  - Make sure your have
    - Tenant Id
    - Client Id
    - Client Secret
  - With these 3 parameters and an *audience* you will be able to get an access token [Get Token](/Courses/Templates/Tokens/Get_Token.md)


