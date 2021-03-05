import pymongo #pip install pymongo
import os
from dotenv import load_dotenv
import json
#pip install dnspython


load_dotenv()
user = os.getenv("DBUSER")
passw= os.getenv("DBPASS")
mongoServer = os.getenv("DBSERVER")

client = pymongo.MongoClient(mongoServer) # initializes the mongodb connection
db = client["api_db"] # Database name
accounts = db["user_accounts"] # Collection name


new_users = [
    {
        "_id":1,
        "name":"Person1",
        "role":"Manager",
        "rank_points":1500,
        "wallet":500,
        "bank": 3000
    },
    {
        "_id":2,
        "name":"Person2",
        "role":"Customer",
        "rank_points":1400,
        "wallet":300,
        "bank": 1500
    },
    {
        "_id":3,
        "name":"Person3",
        "role":"Waiter",
        "rank_points":1650,
        "wallet":500,
        "bank": 2000
    }
]

accounts.insert_many(new_users)
