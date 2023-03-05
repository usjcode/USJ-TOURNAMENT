import requests

endpoint = "http://127.0.0.1:8000/staff/create/"
response = requests.post(endpoint, json = {'email':'toto@gmail.com', 'role':'D'})
print(response.json())
print(response.status_code)