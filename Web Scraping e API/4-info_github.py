import requests 

url = 'http://api.github.com/events'
response =  requests.get(url)
#print(response.json())

headers = {'x-GitHub-Api-Version': "2022-11-28"}

response3 = requests.get(url, headers=headers)

print(response3.json())