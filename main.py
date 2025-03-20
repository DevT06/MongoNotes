import shlex
import repositories as repo
import utility as utils
import os

note_repo = repo.note_repo
user_repo = repo.user_repo

display = utils.display_utils
crud = utils.crud_utils

def edit(args):
    if len(args) != 2:
        print("Requires at least two arguments: collection and id")
        return
    else:

        collection = args.pop(0)
        id = args.pop(0)
        # values = args_to_dict()

def delete(args):
    pass

if __name__ == "__main__":
    is_running = True
    while is_running:
        userinput = input("MongoNotes: ")
        parts = shlex.split(userinput)
        cmd = parts.pop(0)
        match cmd:
            case "get":
                crud.get(parts)
            case "edit":
                edit(parts)
            case "delete":
                crud.delete(parts)
            case "exit":
                exit(0)
            case "help":
                print("Commands: get, edit, delete, exit")
                # add options for each command
            case _:
                print("Invalid command")