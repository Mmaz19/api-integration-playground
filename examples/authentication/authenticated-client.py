import requests

TOKEN = "your_access_token"

API_URL = "https://jsonplaceholder.typicode.com/users"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(API_URL, headers=headers)

print(response.status_code)

if response.ok:
    print(response.json())