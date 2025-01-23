{endpoint}/openai/deployments/gpt-4o/chat/completions?api-version=2024-10-21

Headers:
    api-key: {apiKey}

Body
   raw-json

```json

{
 "messages": [
  {
   "role": "system",
   "content": "you are a helpful assistant, you give short precise answers"
  },
  {
   "role": "user",
   "content": "Us 10th president?"
  },
  {
      "role": "assistant",
      "content" : "The 10th President of the United States was John Tyler."
  },
  {
      "role" : "user",
      "content" : "tell me a fun fact about him and his children"
  }
 ]
}


```