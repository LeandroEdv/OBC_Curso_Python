import requests

headers = {'x-GitHub-Api-Vesersion': '2022-11-28'}
base_api = 'https://api.github.com'
user = 'OneBitCodeBlog'

url = f'{base_api}/users/{user}/repos'

response = requests.get(url, headers=headers)
print(response.json())