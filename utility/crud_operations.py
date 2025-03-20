from bson import ObjectId
import repositories as repo
import utility as utils

note_repo = repo.note_repo
user_repo = repo.user_repo
display = utils.display_utils

def get(args):
    if len(args) == 1:
        match args[0]:
            case "notes":
                notes = note_repo.get_all()
                for note in notes:
                    display.format_note(note)
            case "users":
                users = user_repo.get_all()
                for user in users:
                    display.format_user(user)
            case _:
                print("Invalid arguments")
                return
    elif len(args) > 1:
        collection = args[0]
        query = {}
        for arg in args[1:]:
            key, value = arg.split(":", 1)
            match key == "ca":
                case "ca":
                    key = "created_at"
                case "ua":
                    key = "updated_at"
            query[key] = value

        match collection:
            case "notes":
                notes = note_repo.get_by_search(query)
                for note in notes:
                    print(display.format_note(note))
            case "users":
                users = user_repo.get_by_search(query)
                for user in users:
                    print(display.format_user(user))
            case _:
                print("Invalid collection")

def delete(args):
    try:
        object_id = ObjectId(args[1])  # Convert the string ID to ObjectId
    except Exception as e:
        print(f"Invalid ID format: {e}")
        return

    if args[0] == "note":
        note_repo.delete_by_id(object_id)
    elif args[0] == "user":
        user_repo.delete_by_id(object_id)
    else:
        print("Invalid collection type")