import shlex
import repositories as repo
import utility as utils

note_repo = repo.note_repo

user_repo = repo.user_repo

display = utils.display_utils

def get(args):
    if len(args) == 1:
        match args[0]:
            case "notes":
                notes = note_repo.get_all_notes()
                for note in notes:
                    display.format_note(note)
            case "users":
                users = user_repo.get_all_users()
                for user in users:
                    display.format_user(user)
            case _:
                print("Invalid arguments")
                return
        # todo

def edit(args):
    if len(args) != 2:
        print("Requires two arguments: collection and id")
        return
    else:
        collection = args[0]
        id = args[1]
        match collection:
            case "user":
                user = user_repo.get_user_by_id(id)
                edit_dict(user)
            case "note":
                note = note_repo.get_note_by_id(id)
                edit_dict(note)


def edit_dict(dict):
    os.system('cls')
    print("[Object object]")


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
                get(parts)
            case "edit":
                edit(parts)
            case "delete":
                delete(parts)
            case "exit":
                exit(0)
            case "help":
                print("Commands: get, edit, delete, exit")
                # add options for each command
            case _:
                print("Invalid command")