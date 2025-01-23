```powershell

winget install postman

```

POST {endpoint}/language/:analyze-text?api-version=2024-11-01

HEADERS
   Ocp-Apim-Subscription-Key: {apiKey}


BODY
   Raw-json

```json

{
    "kind": "LanguageDetection",
    "parameters": {
        "modelVersion": "latest"
    },
    "analysisInput": {
    "documents": [
      {
        "id": "1",
        "text": "Je suis Morten"
      }
    ]
    }
}

```