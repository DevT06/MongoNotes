import shlex

from db import mongo_db

#init connection
mongo_db.connent()

is_running = True

while is_running:
    entered_value = input("MongoNotes: ")
    args = shlex.split(entered_value)
    cmd = args.pop(0)
    match cmd.lower():
        case "get":

            break
        case "edit":

            break
        case "delete":

            break
        case "exit":

            break