from db import mongo_db
import datetime

users = mongo_db.users

def add_user(name, password, is_admin):
    user = {"name": name,
            "password": password,
            "is_admin": is_admin,
            "created_at": datetime.datetime.now()
            }
    users.insert_one(user)

def get_all_users():
    return users.find({}, {"password": 0})

def get_user_by_name(name):
    return users.find_one({"name": name}, {"password": 0})

def get_user_by_id(id):
    return users.find_one({"_id": id}, {"password": 0})

def delete_user_by_id(id):
    users.delete_one({"_id": id})