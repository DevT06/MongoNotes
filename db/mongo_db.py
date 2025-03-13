from pymongo import MongoClient
import datetime

# Connect to MongoDB (default: localhost, port 27017)
client = MongoClient("mongodb://localhost:27017/")

# Create a database (it will be created when you insert a document)
db = client["MongoNotes"]

# Create a collections
notes = db["Notes"] # has Tags
users = db["Users"]

## Repository

# notes:
def add_note(title, content, weight, status, tags, owner_id):
    note = {"title": title, 
            "content": content, 
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now(),
            "weight": weight,
            "status": status,
            "tags": tags, # list of tags
            "owner_id": owner_id
            }
    notes.insert_one(note)

def get_all_notes():
    return notes.find()

def get_notes_by_title(title):
    return notes.find({"title": title})

def get_notse_by_id(id):
    return notes.find({"_id": id})

def update_note_by_id(id, title, content, weight, status, tags):
    notes.update_one({"_id": id}, 
                     {"$set": {"title": title, 
                               "content": content, 
                               "updated_at": datetime.datetime.now(),
                               "weight": weight,
                               "status": status,
                               "tags": tags
                               }
                     })
    
def delete_note_by_id(id):
    notes.delete_one({"_id": id})
