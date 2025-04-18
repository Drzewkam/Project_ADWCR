import requests

# Przykład 1
resp = requests.get("http://127.0.0.1:5000/compare", params={"x": 5, "y": 3})
print(resp.json())
# → {"x": 5.0, "y": 3.0, "decision": "x jest większe od y"}

# Przykład 2
resp = requests.get("http://127.0.0.1:5000/compare", params={"x": 2, "y": 7})
print(resp.json())
# → {"x": 2.0, "y": 7.0, "decision": "y jest większe od x"}
