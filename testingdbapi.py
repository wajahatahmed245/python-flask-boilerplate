import requests,json

r = requests.get('http://127.0.0.1:5000/')

print(r.json()[1])


