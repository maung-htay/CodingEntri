import requests

# endpoint = "http://localhost:8000/api/get-products/"
endpoint = "http://localhost:8000/api/generic/"
data = [{"title": "Hello 3", "price": 28.24, "content": None}]

get_response = requests.get(endpoint)

print(get_response.json())
