import shlex
import os
from repositories import note_repo, user_repo
from utility import display_utils, crud_operations, edit_utils, help, user_actions
import os



def edit(args, user_id):
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
        edit_utils.edit_user(id, user_id)
    else:
        print("Invalid collection type. Use 'note' or 'user'")

if __name__ == "__main__":
    print("Welcome to MongoNotes CLI")
    print("Type 'help' for available commands")
    user_id = None
    is_initial_setup = True
    while not user_id:
        user_actions.setup(is_initial_setup)
        is_initial_setup = False
        # login later
        user_id = user_actions.login()

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
                    crud_operations.get(parts)
                case "add":
                    crud_operations.add(parts, user_id)
                case "edit":
                    edit(parts, user_id)
                case "delete":
                    user_actions.delete_with_admin_password(parts, user_id)
                case "exit":
                    print("Goodbye!")
                    is_running = False
                case "help":
                    help.show_help()
                case _:
                    print(f"Invalid command: {cmd}")
                    print("Type 'help' for available commands")
        except Exception as e:
            print(f"Error: {e}")
            print("Type 'help' for available commands")