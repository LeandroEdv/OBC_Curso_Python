import urllib.request
import json

url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=e547e17d4e91f3e62a571655cd1ccaff'

resposta = urllib.request.urlopen(url)

dados = resposta.read()

dados_json = json.loads(dados)

