from pymongo import MongoClient

# Connect to MongoDB (default: localhost, port 27017)
client = MongoClient("mongodb://localhost:27017/")

# Create a database (it will be created when you insert a document)
db = client["MongoNotes"]

# Create a collections
notes = db["Notes"] # has Tags
users = db["Users"]