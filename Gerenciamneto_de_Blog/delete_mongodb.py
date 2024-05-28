from pymongo import MongoClient
client = MongoClient()
mydb = client.obcblog
mycol = mydb.posts

myquery = {"category": "love"}
x = mycol.delete_one(myquery)