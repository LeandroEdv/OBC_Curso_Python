from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

post1 = {
    "title": "Web namoro",
    "category": "love",
    "author": {
        "name": "Desconhecido",
        "email": "desconhecido@mail"
    },
}

result = mycol.insert_one(post1)