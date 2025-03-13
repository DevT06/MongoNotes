import shlex

from db import mongo_db

def get(args):
    pass

def edit(args):
    pass

def delete(args):
    pass

if __name__ == "__main__":
    # mongo_db.connent()
    is_running = True
    while is_running:
        entered_value = input("MongoNotes: ")
        args = shlex.split(entered_value)
        cmd = args.pop(0)
        match cmd.lower():
            case "get":
                get(args)
            case "edit":
                edit(args)
            case "delete":
                delete(args)
            case "exit":
                exit(0)
            case _:
                print("No")
