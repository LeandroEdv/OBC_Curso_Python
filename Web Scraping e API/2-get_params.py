import requests

url = "https://jsonplaceholder.typicode.com/posts/"

# Adcionando Payload
payload = {
    "id": [1, 2, 3, 4, 5],
    "userId": 1
}

response = requests.get(url,params=payload)
#print(response.json())

response_json = response.json()
for i in response_json:
    print(i,'\n')