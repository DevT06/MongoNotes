from bson import ObjectId
import repositories as repo
import utility as utils

note_repo = repo.note_repo
user_repo = repo.user_repo
display = utils.display_utils

def get(args):
    if len(args) == 0:
        print("Please specify a collection (notes/users)")
        return
        
    if len(args) == 1:
        match args[0]:
            case "notes":
                notes = note_repo.get_all()
                for note in notes:
                    print(display.format_note(note))
            case "users":
                users = user_repo.get_all()
                for user in users:
                    print(display.format_user(user))
            case _:
                print("Invalid collection. Use 'notes' or 'users'")
                return
    elif len(args) > 1:
        collection = args[0]
        query = {}
        for arg in args[1:]:
            if ":" not in arg:
                print(f"Invalid query format: {arg}. Use key:value")
                continue
                
            key, value = arg.split(":", 1)
            # Convert special keys
            match key:
                case "ca":
                    key = "created_at"
                case "ua":
                    key = "updated_at"
                case "id":
                    key = "_id"
                    try:
                        value = int(value)
                    except ValueError:
                        print(f"ID must be an integer: {value}")
                        return
                case "tag":
                    # Search for notes with a specific tag title
                    key = "tags.title"
                case "tag.ca":
                    # Search for notes with a specific tag created_at date
                    key = "tags.created_at"
                case "owner":
                    # Search for notes with a specific owner ID
                    key = "owner_id"
                    try:
                        value = int(value)
                    except ValueError:
                        print(f"Owner ID must be an integer: {value}")
                        return
                case "admin":
                    # Search for users with admin status
                    key = "is_admin"
                    value = bool(value) # doesnt work properly

            if isinstance(value, str):
                query[key] = {"$regex": f".*{value}.*", "$options": "i"}  # Case-insensitive regex
            elif isinstance(value, bool):
                query[key] = value
            else:
                query[key] = value

        match collection:
            case "notes":
                notes = note_repo.get_by_search(query)
                for note in notes:
                    print(display.format_note(note))
                if notes is None:
                    print("No notes found")
            case "users":
                users = user_repo.get_by_search(query)
                for user in users:
                    print(display.format_user(user))
                if users is None:
                    print("No users found")
            case _:
                print("Invalid collection. Use 'notes' or 'users'")

def add(args):
    if len(args) < 1:
        print("Specify what to add: 'note' or 'user'")
        return
        
    collection = args[0]
    
    if collection == "user":
        name = input("Enter user name: ")
        password = input("Enter password: ")
        is_admin = input("Is admin (y/n): ").lower() == 'y'
        
        try:
            user_repo.add(name, password, is_admin)
            print(f"User '{name}' added successfully")
        except Exception as e:
            print(f"Error adding user: {e}")
            
    elif collection == "note":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        weight = int(input("Enter note weight (1-5): "))
        status = input("Enter note status (draft/active/archived): ")
        tags_input = input("Enter tags (comma separated): ")
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        owner_id = int(input("Enter owner ID: "))
        
        try:
            note_repo.add(title, content, weight, status, tags, owner_id)
            print(f"Note '{title}' added successfully")
            print(f"Added {len(tags)} tags to the note")
        except Exception as e:
            print(f"Error adding note: {e}")
    else:
        print("Invalid collection. Use 'note' or 'user'")

def delete(args):
    if len(args) < 2:
        print("Usage: delete [note/user] [id]")
        return
        
    collection = args[0]
    try:
        id = int(args[1])
    except ValueError:
        print(f"ID must be an integer: {args[1]}")
        return

    if collection == "note":
        if note_repo.get_by_id(id):
            note_repo.delete_by_id(id)
            print(f"Note {id} deleted successfully")
        else:
            print(f"Note with ID {id} not found")
    elif collection == "user":
        if user_repo.get_by_id(id):
            user_repo.delete_by_id(id)
            print(f"User {id} deleted successfully")
        else:
            print(f"User with ID {id} not found")
    else:
        print("Invalid collection type. Use 'note' or 'user'")