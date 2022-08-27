import requests

endpoint = 'http://127.0.0.1:8000/api/generic/1/delete/'
# data = {'title': 'Hello 3', 'price': 10.5}
get_response = requests.delete(endpoint)

print(get_response.status_code)
