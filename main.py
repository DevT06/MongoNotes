import shlex
import repositories as repo
import utility as utils
import os

note_repo = repo.note_repo
user_repo = repo.user_repo

display = utils.display_utils
crud = utils.crud_operations
edit_utils = utils.edit_utlis
help_utils = utils.help
user_actions = utils.user_actions

def edit(args):
    if len(args) != 2:
        print("Usage: edit [note/user] [id]")
        return
        
    collection = args[0]
    try:
        id = int(args[1])
    except ValueError:
        print(f"ID must be an integer: {args[1]}")
        return
        
    if collection == "note":
        edit_utils.edit_note(id)
    elif collection == "user":
        edit_utils.edit_user(id)
    else:
        print("Invalid collection type. Use 'note' or 'user'")

if __name__ == "__main__":
    print("Welcome to MongoNotes CLI")
    print("Type 'help' for available commands")
    
    user_actions.setup()

    is_running = True
    while is_running:
        try:
            userinput = input("\nMongoNotes> ")
            parts = shlex.split(userinput)
            
            if not parts:
                continue
                
            cmd = parts.pop(0)
            match cmd:
                case "get":
                    crud.get(parts)
                case "add":
                    crud.add(parts)
                case "edit":
                    edit(parts)
                case "delete":
                    user_actions.delete_with_admin_password(parts)
                case "exit":
                    print("Goodbye!")
                    is_running = False
                case "help":
                    help_utils.show_help()
                case _:
                    print(f"Invalid command: {cmd}")
                    print("Type 'help' for available commands")
        except Exception as e:
            print(f"Error: {e}")
            print("Type 'help' for available commands")