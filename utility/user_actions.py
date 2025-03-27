from repositories import note_repo, user_repo
from utility import display_utils, crud_operations, edit_utils, help
import utility as utils

def setup(is_initial_setup):
    # Check if user with ID 1 exists
    # user_1 = user_repo.get_by_id(1)
    # user = user_repo.get_by_search({"is_admin": False}, {"is_admin": {"$exists": False}})
    # if not user_1:
    #     print("No regular user found with ID")
    #     print("Please create a new regular user.")
    #     name = input("Enter user name: ")
    #     password = input("Enter password: ")
    #     user_repo.add(name, password, is_admin=False)
    #     print(f"User '{name}' created successfully.")

    # Find all non-admin users
    all_users = list(user_repo.get_by_search({"_id": {"$ne": 2}}))
    
    user_id = None
    if is_initial_setup == False:
        return

    if all_users:
        print("\nExisting regular users:")
        for user in all_users:
            print(f"ID: {user.get('_id')}, Name: {user.get('name')}, Admin: {user.get('is_admin', False)}")
        # user_id = non_admin_users[0].get("_id")
    else:
        print("\nNo regular users found.")
        print("Please create a new regular user.")
        name = input("Enter regular username: ")
        password = input("Enter password: ")
        user_id = user_repo.add(name, password, is_admin=False)
        print(f"Regular user '{name}' created successfully with ID {user_id}.")

    # Check if admin password for user with ID 2 is set
    admin_user = user_repo.get_by_id_with_password(2)
    if admin_user and not admin_user.get("password"):
        print("Root admin password for user with ID 2 is not set.")
        password = input("Set admin password: ")
        user_repo.update_user_by_id(2, password=password)
        print("Root admin password set successfully.")

def login():
    #name = input("Enter user name: ")
    user_id_str = input("Enter user ID: ")
    try:
        user_id = int(user_id_str)
    except ValueError:
        print(f"User ID must be an integer: {user_id_str}")
        return

    password = input("Enter password: ")
    user = user_repo.get_by_id_with_password(user_id)
    if user and user.get("password") == password:
        print(f"Welcome, {user.get('name')}, ID: {user.get('_id')}!")
        return user.get("_id")
    else:
        print("Invalid credentials.")
        return None

def delete_with_admin_password(args, current_user_id):
    if len(args) < 2:
        print("Usage: delete [note/user] [id]")
        return

    collection = args[0]
    try:
        id = int(args[1])
    except ValueError:
        print(f"ID must be an integer: {args[1]}")
        return

    # Get current user to check admin status
    current_user = user_repo.get_by_id(current_user_id)
    if not current_user:
        print("Current user not found. Please log in again.")
        return
    
    # Check if current user is an admin
    is_admin = current_user.get("is_admin", False)
    
    # Prevent users from deleting themselves
    if collection == "user" and id == current_user_id:
        print("Error: You cannot delete your own account while logged in")
        print("Please have another user (preferably an admin) delete your account")
        return
    
    # If trying to delete the admin user with ID 2, prevent it regardless of who's trying
    if collection == "user" and id == 2:
        print("Error: Cannot delete the root admin user (ID 2)")
        return
    
    # If current user is admin, allow deletion without password
    if is_admin:
        if collection == "note":
            note = note_repo.get_by_id(id)
            if note:
                note_repo.delete_by_id(id)
                print(f"Note {id} deleted successfully")
            else:
                print(f"Note with ID {id} not found")
        elif collection == "user":
            user = user_repo.get_by_id(id)
            if user:
                # Delete all notes associated with this user using the optimized method
                note_repo.delete_by_user_id(id)
                
                # Delete the user
                user_repo.delete_by_id(id)
                print(f"User {id} deleted successfully")
                print(f"All notes owned by user {id} have been deleted")
            else:
                print(f"User with ID {id} not found")
        else:
            print("Invalid collection type. Use 'note' or 'user'")
        return
    
    # Not an admin, so require admin password
    # Get admin user for authentication
    admin_user = user_repo.get_by_id_with_password(2)
    if not admin_user:
        print("Root admin user not found. Please run setup first.")
        return

    # Admin password required
    admin_password = input("Enter admin password: ")
    if admin_user.get("password") != admin_password:
        print("Invalid root admin password.")
        return
        
    # Password verified, proceed with deletion
    if collection == "note":
        note = note_repo.get_by_id(id)
        if note:
            note_repo.delete_by_id(id)
            print(f"Note {id} deleted successfully")
        else:
            print(f"Note with ID {id} not found")
    elif collection == "user":
        user = user_repo.get_by_id(id)
        if user:
            # Delete all notes associated with this user using the optimized method
            note_repo.delete_by_user_id(id)
            
            # Delete the user
            user_repo.delete_by_id(id)
            print(f"User {id} deleted successfully")
            print(f"All notes owned by user {id} have been deleted")
        else:
            print(f"User with ID {id} not found")
    else:
        print("Invalid collection type. Use 'note' or 'user'")