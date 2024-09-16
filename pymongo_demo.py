import pymongo
import dotenv
import os

dotenv.load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"))

db = client.todoappdatabase

collection = db.todo_items

# Insert a record
collection.insert_one({"description": "A second pymongo document"})

#Read all records
list(collection.find())

#Insert and update a record
collection.insert_one({"description": "An updateable document", "type": "updateable"})
collection.update_one({"type": "updateable"}, {"$set": {"decription": "CHANGED!!!"}})

print(collection)