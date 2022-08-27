import requests

# endpoint = "http://localhost:8000/api/get-products/"
# endpoint = "http://localhost:8000/api/generic/create/"
endpoint = "http://localhost:8000/api/alt/"
data = {"title": "Hello 3", "price": 28.24, "content": None}

get_response = requests.post(endpoint, json=data)

print(get_response.json())
