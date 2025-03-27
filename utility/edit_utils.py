from utility.display_utils import format_note, format_user
import repositories.note_repo as note_repo
import repositories.user_repo as user_repo

def edit_note(note_id):
    note = note_repo.get_by_id(note_id)
    if not note:
        print(f"Note with ID {note_id} not found")
        return
        
    print("Current note details:")
    print(format_note(note))
    
    # Extract tag titles for display
    tag_titles = []
    for tag in note.get('tags', []):
        if isinstance(tag, dict):
            tag_titles.append(tag.get('title', ''))
        else:
            tag_titles.append(str(tag))
    
    # Edit fields one by one
    title = input(f"Title [{note.get('title', '')}] (leave empty to keep current): ")
    content = input(f"Content [{note.get('content', '')}] (leave empty to keep current, '-' to remove): ")
    weight_str = input(f"Weight [{note.get('weight', '')}] (leave empty to keep current, '-' to remove): ")
    status = input(f"Status [{note.get('status', '')}] (leave empty to keep current, '-' to remove): ")
    tags_str = input(f"Tags [{', '.join(tag_titles)}] (leave empty to keep current): ")
    
    # Process inputs (only update if provided)
    title = None if not title else title
    content = None if not content else content
    if weight_str != "-":
        weight = None if not weight_str else int(weight_str)
    else:
        weight = "-"
    status = None if not status else status
    tags = None if not tags_str else [tag.strip() for tag in tags_str.split(",") if tag.strip()]
    
    # Update the note
    note_repo.update_by_id(note_id, title, content, weight, status, tags)
    print(f"Note {note_id} updated successfully")
    if tags:
        print(f"Updated note with {len(tags)} tags")

def edit_user(user_id, current_user_id):
    user = user_repo.get_by_id(user_id)
    if not user:
        print(f"User with ID {user_id} not found")
        return
        
    # Get current user info to check admin status
    current_user = user_repo.get_by_id(current_user_id)
    if not current_user:
        print("Current user not found. Please log in again.")
        return
    
    # Check if current user is an admin
    is_current_user_admin = current_user.get("is_admin", False)
    
    print("Current user details:")
    print(format_user(user))
    
    # Edit fields one by one
    name = input(f"Name [{user.get('name', '')}] (leave empty to keep current): ")
    password = input("New password (leave empty to keep current): ")
    
    # Handle admin status change
    is_admin = None
    if is_current_user_admin:
        # Admin user can directly change admin status
        is_admin_str = input(f"Is admin [{user.get('is_admin', False)}] (y/n, leave empty to keep current): ")
        if is_admin_str:
            is_admin = is_admin_str.lower() == 'y'
            
            # Special protection for the admin user (ID 2)
            if user.get('_id') == 2 and is_admin is False:
                print("Error: Cannot remove admin status from user with ID 2")
                is_admin = True
    else:
        # Non-admin user - offer option to authenticate with admin password
        admin_auth = input("Do you want to change admin status? This requires admin authentication (y/n): ")
        
        if admin_auth.lower() == 'y':
            # Get admin user for authentication
            admin_user = user_repo.get_by_id_with_password(2)
            if not admin_user:
                print("Admin user not found. Cannot change admin status.")
            else:
                # Request admin password
                admin_password = input("Enter admin password: ")
                
                if admin_user.get("password") == admin_password:
                    # Password verified, allow admin status change
                    is_admin_str = input(f"Is admin [{user.get('is_admin', False)}] (y/n, leave empty to keep current): ")
                    if is_admin_str:
                        is_admin = is_admin_str.lower() == 'y'
                        
                        # Special protection for the admin user (ID 2)
                        if user.get('_id') == 2 and is_admin is False:
                            print("Error: Cannot remove admin status from user with ID 2")
                            is_admin = True
                else:
                    print("Invalid admin password. Admin status cannot be changed.")
        else:
            print("Admin status will remain unchanged.")
    
    # Process other inputs
    name = None if not name else name
    password = None if not password else password
    
    # Update the user
    user_repo.update_user_by_id(user_id, name, password, is_admin)
    print(f"User {user_id} updated successfully")