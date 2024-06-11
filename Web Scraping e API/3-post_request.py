import requests 

new_data = {
    "userId": 1,
    "id": 1,
    "title": "Aprendendo Python",
    "body": "Manipulando Informaçoes da API com requests"
}

url = "https://jsonplaceholder.typicode.com/posts/"

#ENVIO DE DADOS
post_response = requests.post(
    url,
    json= new_data
)
#print(post_response.status_code)

#4 - LISTAR INFORMAÇÃO
post_response_json = post_response.json()
print(post_response_json)