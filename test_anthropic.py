import json
import requests
import os

api_key = os.environ.get("ANTHROPIC_API_KEY", "")
url = "https://api.anthropic.com/v1/messages"

prompt = "Hello"
headers = {
    'x-api-key': api_key,
    'anthropic-version': '2023-06-01',
    'content-type': 'application/json'
}
req_data = {
    "model": "claude-3-haiku-20240307",
    "max_tokens": 100,
    "temperature": 0.4,
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

response = requests.post(url, headers=headers, json=req_data)
print(response.text)
