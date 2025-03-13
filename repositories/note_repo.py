from db import mongo_db
import datetime

notes = mongo_db.notes

def get_all():
    return notes.find()

def get_by_title(title):
    return notes.find({"title": title})

def get_by_id(id):
    return notes.find_one({"_id": id})

def get_by_search_index(search):
    return notes.find({"$text": {"$search": search}})

def get_by_search(searchQuery):
    return notes.find(searchQuery)

def add(title, content, weight, status, tags, owner_id):
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

def update_by_id(id, title, content, weight, status, tags):
    note = get_by_id(id)
    
    # update the tag logic later

    updated_note = {
        "title": title if title != note["title"] else note["title"],
        "content": content if content != note["content"] else note["content"],
        "updated_at": datetime.datetime.now(),
        "weight": weight if weight != note["weight"] else note["weight"],
        "status": status if status != note["status"] else note["status"],
        "tags": tags if tags != note["tags"] else note["tags"]
    }

    notes.update_one({"_id": id}, {"$set": updated_note})
    
def delete_by_id(id):
    notes.delete_one({"_id": id})
