import requests

endpoint = 'http://127.0.0.1:8000/api/generic/1/'
data = {'title': 'Hello my friend', 'price': 10.5}
get_response = requests.get(endpoint)

print(get_response.json())
