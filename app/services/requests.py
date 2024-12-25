import services.requests as requests, json

# request = requests.get("http://127.0.0.1:8000/data")
# print(request.json())

request = requests.post("http://127.0.0.1:8000/data", data=json.dumps({"name": "test", "score": 100}))
print(request.json())