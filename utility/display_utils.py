def format_note(note):
    return f"""
    Title: {note.get('title')}
    Content: {note.get('content')}
    Created At: {note.get('created_at')}
    Updated At: {note.get('updated_at')}
    Weight: {note.get('weight')}
    Status: {note.get('status')}
    Tags: {', '.join(note.get('tags', []))}
    Owner ID: {note.get('owner_id')}
    """

def format_user(user):
    return f"""
    Name: {user.get('name')}
    Is Admin: {user.get('is_admin')}
    Created At: {user.get('created_at')}
    """