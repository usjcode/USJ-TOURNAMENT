import requests

endpoint = "http://127.0.0.1/tournement/create"
response = requests.post(endpoint, json = {'date_inscription':'1-5-2023','date_debut':'2-5-2023'} )
print(response.json())
print(response.status_code)