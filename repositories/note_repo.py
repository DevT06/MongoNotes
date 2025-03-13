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
            "tags": tags,  # list of tags
            "owner_id": owner_id
            }
    notes.insert_one(note)

def update_by_id(id, title=None, content=None, weight=None, status=None, tags=None):
    note = get_note_by_id(id)
    updated_note = {
        "title": note["title"] if title is None else title,
        "content": note["content"] if content is None else content,
        "weight": note["weight"] if weight is None else weight,
        "status": note["status"] if status is None else status,
        "tags": note["tags"] if tags is None else tags,
        "updated_at": datetime.datetime.now()
    }
    notes.update_one({"_id": id}, {"$set": updated_note})
    # update the tag logic later
 
def delete_by_id(id):
    notes.delete_one({"_id": id})