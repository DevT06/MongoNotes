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
    for tag_input in tags:
        # Check if the tag has a description specification
        if ":d=" in tag_input:
            # Split the tag input into title and description
            tag_parts = tag_input.split(":d=", 1)
            tag_title = tag_parts[0].strip()
            
            # Extract description, handling quoted text properly
            description = tag_parts[1].strip()
            if description.startswith('"') and description.endswith('"'):
                description = description[1:-1]  # Remove surrounding quotes
            
            tag_object = {
                "title": tag_title,
                "description": description,
                "created_at": datetime.datetime.now()
            }
        else:
            # Regular tag without description
            tag_object = {
                "title": tag_input,
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
        
        # Track tag titles that will be updated to avoid duplicates
        tag_titles_to_update = set()
        
        # First pass: identify tags to be removed or replaced
        for tag_input in tags:
            if tag_input.startswith("rm:"):
                tag_to_remove = tag_input[3:]  # Remove "rm:" prefix
                tag_titles_to_update.add(tag_to_remove)
            else:
                tag_title = tag_input.split(":d=")[0].strip() if ":d=" in tag_input else tag_input
                tag_titles_to_update.add(tag_title)
        
        # Filter out existing tags that will be replaced
        existing_tags = [tag for tag in existing_tags if tag["title"] not in tag_titles_to_update]
        
        # Second pass: add new tags
        for tag_input in tags:
            if not tag_input.startswith("rm:"):
                # Check if the tag has a description specification
                if ":d=" in tag_input:
                    # Split the tag input into title and description
                    tag_parts = tag_input.split(":d=", 1)
                    tag_title = tag_parts[0].strip()
                    
                    # Extract description, handling quoted text properly
                    description = tag_parts[1].strip()
                    if description.startswith('"') and description.endswith('"'):
                        description = description[1:-1]  # Remove surrounding quotes
                    
                    updated_tags.append({
                        "title": tag_title,
                        "description": description,
                        "created_at": datetime.datetime.now()
                    })
                else:
                    # Regular tag without description
                    updated_tags.append({
                        "title": tag_input,
                        "created_at": datetime.datetime.now()
                    })
        
        # Combine existing (filtered) and new tags
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