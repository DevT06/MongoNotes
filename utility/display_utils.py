def format_note(note):
    # Format tags as a list of titles
    tag_list = []
    for tag in note.get('tags', []):
        if isinstance(tag, dict):
            tag_list.append(f"{tag.get('title')} (created At: {tag.get('created_at')})")
        else:
            tag_list.append(str(tag))
    
    return f"""
    ID: {note.get('_id')}
    Title: {note.get('title')}
    Content: {note.get('content')}
    Created At: {note.get('created_at')}
    Updated At: {note.get('updated_at')}
    Weight: {note.get('weight')}
    Status: {note.get('status')}
    Tags: {', '.join(tag_list) if tag_list else 'None'}
    Owner ID: {note.get('owner_id')}
    """

def format_user(user):
    return f"""
    ID: {user.get('_id')}
    Name: {user.get('name')}
    Is Admin: {"true" if user.get('is_admin') else "false"}
    Created At: {user.get('created_at')}
    """