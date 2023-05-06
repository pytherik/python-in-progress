import json
import requests


api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
j = response.json()
print(j)
res = response.status_code
print(res)
headers = {"Content-Type": "application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
print(response.json())
