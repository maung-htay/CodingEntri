import requests

# endpoint = "http://localhost:8000/api/get-products/"
# endpoint = "http://localhost:8000/api/generic/1"
endpoint = "http://localhost:8000/api/alt/11"

get_response = requests.get(endpoint)

print(get_response.json())

