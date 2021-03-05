from flask import Flask, jsonify, request # pip install Flask
import pymongo #pip install pymongo
import os
from dotenv import load_dotenv
import json
#pip install dnspython


app = Flask(__name__) #initialized Flask app

#loads environmental variables from env file
load_dotenv()
user = os.getenv("DBUSER")
passw= os.getenv("DBPASS")
mongoServer = os.getenv("DBSERVER")


client = pymongo.MongoClient(mongoServer) # initializes the mongodb connection
db = client["api_db"] # Database name
accounts = db["user_accounts"] # Collection name

#Main route
@app.route("/")
def home():
    return jsonify({"Home": "Hello World!"})


#Accounts route which allows user to get all player data
@app.route("/accounts", methods=["GET"])
def user_accounts():
    user = request.args.get("user")

    if(user != None):
        return jsonify(list(accounts.find({"name":user})))

    else:
        return jsonify(list(accounts.find()))


#Transactions route which allows users to get specified players game bank/wallet transactions
@app.route("/transactions", methods = ["GET"])
def find_transactions():
    user = request.args.get("user")
    
    if(user != None):
        to_return = accounts.find({"name":user})[0]["transactions"]

        if len(to_return) == 0:
            return jsonify({"Status":"No Transactions have been made."})
        else:
            return jsonify(to_return)

    else:
        return jsonify({"error":"Please enter valid arguments: user"})


#Transactions subroute which allows users to log transactions of players 
@app.route("/transactions/make", methods = ["POST"])
def make_transaction():
    receiver = request.args.get("to")
    sender = request.args.get("from")
    amount = request.args.get("amount", type = int)

    if(receiver == None or sender == None or amount == None):
        return jsonify({"error":"Please enter valid arguments: sender, receiver, and amount"})

    else:
        sent_trans = {"sender":sender, "recipient":receiver, "amount": amount, "type":"Payment"}
        recieved_trans = {"sender":sender, "recipient":receiver, "amount": amount, "type":"Received"}

        accounts.update({"name":sender}, {"$push": {"transactions":sent_trans}, "$inc": {"wallet": -amount}})
        accounts.update({"name":receiver}, {"$push": {"transactions":recieved_trans}, "$inc": {"wallet": amount}})

        return jsonify({"sender":sender, "recipient":receiver, "amount": amount, "status":"Transaction Completed"})


if __name__ == "__main__":
    app.run(debug=False, threaded = True)