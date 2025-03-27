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
        # Extract the base tag title before any modifiers
        base_tag = tag_input.split(":", 1)[0].strip() if ":" in tag_input else tag_input
        
        # Initialize tag object with basic properties
        tag_object = {
            "title": base_tag,
            "created_at": datetime.datetime.now()
        }
        
        # Check for description specification (:d=)
        if ":d=" in tag_input:
            # Find the description part
            desc_start = tag_input.find(":d=") + 3
            
            # Find the end of the description (next colon or end of string)
            desc_end = tag_input.find(":", desc_start) if ":" in tag_input[desc_start:] else len(tag_input)
            
            description = tag_input[desc_start:desc_end].strip()
            # Remove surrounding quotes if present
            if description.startswith('"') and description.endswith('"'):
                description = description[1:-1]
                
            tag_object["description"] = description
        
        # Check for color specification (:c=)
        if ":c=" in tag_input:
            # Find the color part
            color_start = tag_input.find(":c=") + 3
            
            # Find the end of the color (next colon or end of string)
            color_end = tag_input.find(":", color_start) if ":" in tag_input[color_start:] else len(tag_input)
            
            color = tag_input[color_start:color_end].strip()
            # Remove surrounding quotes if present
            if color.startswith('"') and color.endswith('"'):
                color = color[1:-1]
                
            tag_object["color"] = color
        
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
                # Get the base tag title before any modifiers
                base_tag = tag_input.split(":", 1)[0].strip() if ":" in tag_input else tag_input
                tag_titles_to_update.add(base_tag)
        
        # Filter out existing tags that will be replaced
        existing_tags = [tag for tag in existing_tags if tag["title"] not in tag_titles_to_update]
        
        # Second pass: add new tags
        for tag_input in tags:
            if not tag_input.startswith("rm:"):
                # Extract the base tag title before any modifiers
                base_tag = tag_input.split(":", 1)[0].strip() if ":" in tag_input else tag_input
                
                # Initialize tag object with basic properties
                tag_object = {
                    "title": base_tag,
                    "created_at": datetime.datetime.now()
                }
                
                # Check for description specification (:d=)
                if ":d=" in tag_input:
                    # Find the description part
                    desc_start = tag_input.find(":d=") + 3
                    
                    # Find the end of the description (next colon or end of string)
                    desc_end = tag_input.find(":", desc_start) if ":" in tag_input[desc_start:] else len(tag_input)
                    
                    description = tag_input[desc_start:desc_end].strip()
                    # Remove surrounding quotes if present
                    if description.startswith('"') and description.endswith('"'):
                        description = description[1:-1]
                        
                    tag_object["description"] = description
                
                # Check for color specification (:c=)
                if ":c=" in tag_input:
                    # Find the color part
                    color_start = tag_input.find(":c=") + 3
                    
                    # Find the end of the color (next colon or end of string)
                    color_end = tag_input.find(":", color_start) if ":" in tag_input[color_start:] else len(tag_input)
                    
                    color = tag_input[color_start:color_end].strip()
                    # Remove surrounding quotes if present
                    if color.startswith('"') and color.endswith('"'):
                        color = color[1:-1]
                        
                    tag_object["color"] = color
                
                updated_tags.append(tag_object)
        
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

def delete_by_user_id(user_id):
    notes.delete_many({"owner_id": user_id})