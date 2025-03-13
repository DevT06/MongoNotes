import shlex

def get(args):
    pass

def edit(args):
    pass

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
            case _:
                print("Invalid command")
