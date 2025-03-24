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
        #"content": content,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
        #"weight": weight,
        #"status": status,
        #"tags": tag_objects,  # Store tag objects directly
        "owner_id": owner_id
    }

    if content:
        note["content"] = content
    if weight is not None:
        note["weight"] = weight
    if status:
        note["status"] = status
    if len(tag_objects) > 0:
        note["tags"] = tag_objects

    notes.insert_one(note)

def update_by_id(id, title=None, content=None, weight=None, status=None, tags=None):
    note = get_by_id(id)
    if not note:
        raise ValueError(f"Note with id {id} not found")

    # Build the $set and $unset dictionaries
    set_fields = {"updated_at": datetime.datetime.now()}
    unset_fields = {}

    if title:
        set_fields["title"] = title
    else:
        set_fields["title"] = note.get("title")

    # Use existing value if content is None or empty
    if content == "-":
        unset_fields["content"] = ""
    elif content:
        set_fields["content"] = content
    else:
        set_fields["content"] = note.get("content")

    # Use existing value if weight is None
    if weight == "-":
        unset_fields["weight"] = ""
    elif weight is not None:
        set_fields["weight"] = weight
    else:
        set_fields["weight"] = note.get("weight")

    # Use existing value if status is None or empty
    if status == "-":
        unset_fields["status"] = ""
    elif status:
        set_fields["status"] = status
    else:
        set_fields["status"] = note.get("status")


    if tags == "-":
        unset_fields["tags"] = ""
    elif tags is not None:
        existing_tags = note.get("tags", [])
        updated_tags = []

        # Remove tags with "rm:" prefix and add new tags
        for tag_title in tags:
            if tag_title.startswith("rm:"):
                tag_to_remove = tag_title[3:]  # Remove "rm:" prefix
                existing_tags = [
                    tag for tag in existing_tags if tag["title"] != tag_to_remove
                ]
            else:
                updated_tags.append(
                    {"title": tag_title, "created_at": datetime.datetime.now()}
                )

        # Append new tags to the existing ones
        existing_tags.extend(updated_tags)
        set_fields["tags"] = existing_tags

    # Perform the update with $set and $unset
    update_query = {}
    if set_fields:
        update_query["$set"] = set_fields
    if unset_fields:
        update_query["$unset"] = unset_fields

    notes.update_one({"_id": id}, update_query)
 
def delete_by_id(id):
    notes.delete_one({"_id": id})