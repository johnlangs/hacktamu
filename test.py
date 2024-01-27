import requests 

url = "http://localhost:4000/"

print(requests.api.get(url + "flights?date=2022-11-01").json())
