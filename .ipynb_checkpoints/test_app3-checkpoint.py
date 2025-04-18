import requests

resp = requests.get("http://127.0.0.1:5000/add", params={"a": 3.5, "b": 4.2})
assert resp.status_code == 200
print(resp.text)  # 7.7
