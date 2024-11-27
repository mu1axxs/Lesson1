import requests #--get
response = requests.get("https://httpbin.org/get")
print(response.content)
print(f"Datatype - {type(response.content)}")
print(response.text)
print(f"Datatype - {type(response.text)}")