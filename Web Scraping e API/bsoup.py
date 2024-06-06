from bs4 import BeautifulSoup

# 1 - Importando arquivo local
with open('pages/index.html', 'r', encoding='utf-8') as file_html:
     content = file_html.read()
    #  print(content)
     soup = BeautifulSoup(content)
     #print(soup.prettify())
     
     vagas = soup.find_all('h5')
     #print(vagas)
     for curso in vagas:
         print (curso.text)
     