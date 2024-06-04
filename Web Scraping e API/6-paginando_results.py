import requests
from collections import Counter
import pandas

access_token = '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'

headers = {'Authorization': 'Bearer'+ access_token,
           'x-GitHub-Api-Vesersion': '2022-11-28'}
# 2 - Mapeando Informações 
base_api = 'https://api.github.com'
owner = 'OneBitCodeBlog'
url = f'{base_api}/users/{owner}/repos'

# 3 - Organizando os Dados
repos_list = []
for page_num in range(1, 3):
    try:
        url_page = f'{url}?page={page_num}'
        response = requests.get(url_page, headers=headers)
        repos_list.append(response.json())
    except:
        repos_list.append(None)
    
#print(repos_list[0][3]['name'])

name_repos = []
for page in repos_list:
    for repo in page:
       #print(repo['name'])
       name_repos.append(repo['name'])

lang_repos = []
for page in repos_list:
    for repo in page:
        lang_repos.append(repo['language'])

#print(lang_repos)
#print(Counter(lang_repos))

dados_obc = pandas.DataFrame()
dados_obc['repo_name'] = name_repos
dados_obc['repo_lang'] = lang_repos
#print(dados_obc)

dados_obc.to_csv('dados_OBC.csv')