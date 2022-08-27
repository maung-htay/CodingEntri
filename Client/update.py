import requests

# endpoint = 'http://127.0.0.1:8000/api/generic/1/update/'
endpoint = 'http://127.0.0.1:8000/api/mixins/2/update/'
data = {'title': 'Hello 4', 'price': 10.5}
get_response = requests.put(endpoint, json=data)

print(get_response.json())
