import requests

resp = requests.get("http://127.0.0.1:5000/")
assert resp.status_code == 200
print(resp.text)  # powinno wydrukować: Witaj w moim API!
