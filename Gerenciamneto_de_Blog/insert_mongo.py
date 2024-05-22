from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

post1 = {
    "title": "Web Scraping",
    "category": "Automação",
    "author": {
        "name": "meu nome",
        "email": "fulano@mail"
    },
}

result = mycol.insert_one(post1)