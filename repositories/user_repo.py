from db import mongo_db
import datetime
import utility.auto_increment as auto_increment

users = mongo_db.users

def get_all():
    return users.find({}, {"password": 0})

def get_by_name(name):
    return users.find_one({"name": name}, {"password": 0})

def get_by_id(id):
    return users.find_one({"_id": id}, {"password": 0})

def get_by_search(searchQuery):
    return users.find(searchQuery)

def add(name, password, is_admin):
    user = {
        "_id": auto_increment.get_next_sequence("Users"),
        "name": name,
        "password": password,
        "is_admin": is_admin,
        "created_at": datetime.datetime.now()
    }
    users.insert_one(user)

def add_with_id(id, name, password, is_admin, created_at):
    user = {
        "_id": id,
        "name": name,
        "password": password,
        "is_admin": is_admin,
        "created_at": created_at
    }
    users.insert_one(user)

def update_user_by_id(id, name=None, password=None, is_admin=None):
    user = get_by_id(id)
    updated_user = {
        "name": user["name"] if name is None else name,
        "password": user["password"] if password is None else password,
        "is_admin": user["is_admin"] if is_admin is None else is_admin
    }

    users.update_one({"_id": id}, {"$set": updated_user})

def delete_by_id(id):
    users.delete_one({"_id": id})