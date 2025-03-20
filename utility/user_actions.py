import repositories as repo
import utility as utils

note_repo = repo.note_repo
user_repo = repo.user_repo

display = utils.display_utils
crud = utils.crud_operations
edit_utils = utils.edit_utlis
help_utils = utils.help


def setup():
    # Check if user with ID 1 exists
    user_1 = user_repo.get_by_id(1)
    if not user_1:
        print("No regular user found with ID 1.")
        print("Please create a new regular user.")
        name = input("Enter user name: ")
        password = input("Enter password: ")
        user_repo.add(name, password, is_admin=False)
        print(f"User '{name}' created successfully with ID 1.")

    # Check if admin password for user with ID 2 is set
    admin_user = user_repo.get_by_id(2)
    if admin_user and not admin_user.get("password"):
        print("Admin password for user with ID 2 is not set.")
        password = input("Set admin password: ")
        user_repo.update_user_by_id(2, password=password)
        print("Admin password set successfully.")

def delete_with_admin_password(args):
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
        admin_password = input("Enter admin password: ")
        admin_user = user_repo.get_by_id(2)
        if admin_user and admin_user.get("password") == admin_password:
            if note_repo.get_by_id(id):
                note_repo.delete_by_id(id)
                print(f"Note {id} deleted successfully")
            else:
                print(f"Note with ID {id} not found")
        else:
            print("Invalid admin password.")
    elif collection == "user":
        if user_repo.get_by_id(id):
            user_repo.delete_by_id(id)
            print(f"User {id} deleted successfully")
        else:
            print(f"User with ID {id} not found")
    else:
        print("Invalid collection type. Use 'note' or 'user'")