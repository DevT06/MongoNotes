from db import mongo_db
import datetime

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
    user = {"name": name,
            "password": password,
            "is_admin": is_admin,
            "created_at": datetime.datetime.now()
            }
    users.insert_one(user)

def update_by_id(id, name, password, is_admin):
    user = get_by_id(id)
    
    updated_user = {
        "name": name if name != user["name"] else user["name"],
        "password": password if password != user["password"] else user["password"],
        "is_admin": is_admin if is_admin != user["is_admin"] else user["is_admin"]
    }

    users.update_one({"_id": id}, {"$set": updated_user})

def delete_by_id(id):
    users.delete_one({"_id": id})