from db import mongo_db
import datetime
import utility.auto_increment as auto_increment

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
    # Create tag objects for each tag title
    tag_objects = []
    for tag_title in tags:
        tag_object = {
            "title": tag_title,
            "created_at": datetime.datetime.now()
        }
        tag_objects.append(tag_object)
    
    note = {
        "_id": auto_increment.get_next_sequence("Notes"),
        "title": title,
        "content": content,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
        "weight": weight,
        "status": status,
        "tags": tag_objects,  # Store tag objects directly
        "owner_id": owner_id
    }
    notes.insert_one(note)

def update_by_id(id, title=None, content=None, weight=None, status=None, tags=None):
    note = get_by_id(id)
    
    # Process tags if provided
    tag_objects = note["tags"]
    if tags is not None:
        # Create new tag objects
        tag_objects = []
        for tag_title in tags:
            tag_object = {
                "title": tag_title,
                "created_at": datetime.datetime.now()
            }
            tag_objects.append(tag_object)
    
    updated_note = {
        "title": note["title"] if title is None else title,
        "content": note["content"] if content is None else content,
        "weight": note["weight"] if weight is None else weight,
        "status": note["status"] if status is None else status,
        "tags": tag_objects,
        "updated_at": datetime.datetime.now()
    }
    notes.update_one({"_id": id}, {"$set": updated_note})
 
def delete_by_id(id):
    notes.delete_one({"_id": id})