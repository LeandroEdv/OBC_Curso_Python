import requests
from pymongo import MongoClient

client = MongoClient()
db = client['nobel']

for colection_name in ["prizes", "laureates"]:
    response = requests.get(f"http://api.nobelprize.org/v1/{colection_name[:-1]}.json")
    documents = response.json()[colection_name]
    db[colection_name].insert_many(documents)
    
    prizes = db["prizes"]
    laureates = db["laureates"]
    
    len_prizes =prizes.count_documents({})
    len_laureates = laureates.count_documents({})
    
    print(len_laureates)
    print(len_prizes)