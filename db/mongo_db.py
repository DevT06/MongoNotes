from pymongo import MongoClient



# Connect to MongoDB (default: localhost, port 27017)
client = MongoClient("mongodb://localhost:27017/")

# Create a database (it will be created when you insert a document)
db = client["my_database"]

# Create a collection
collection = db["my_collection"]

# Insert a sample document
sample_data = {"name": "Alice", "age": 25, "city": "New York"}
collection.insert_one(sample_data)

print("Database initialized successfully!")