import sys
import Commands

command = Commands.Commands() 

if len(sys.argv) < 2:
    print("Error to few arguments")
    exit(0)

commandArg = sys.argv[1]

availableCommands = ["search", "remove", "merge", "list", "copy"]

if commandArg not in availableCommands:
    print("Invalid command argument")
    exit(0)


if commandArg == "search":
    if len(sys.argv[2:]) != 3:
        print("Error: the search command takes 3 arguments")
        exit(0)

    if sys.argv[2] != "i" and sys.argv[2] != "-i":
        print(sys.argv[2])
        print("Error: the second argument is the case sensitivity (i) or (-i)")
        exit(0)
    try:
        file = open(sys.argv[4])
    except FileNotFoundError:
        print("Could not open file")
        exit(0)
    file.close()

    command.Search(sys.argv[2:])

if commandArg == "remove":
    if len(sys.argv[2:]) != 3:
        print("Error: the remove command takes 3 arguments")
        exit(0)

    if sys.argv[2] != "i" and sys.argv[2] != "-i":
        print(sys.argv[2])
        print("Error: the second argument is the case sensitivity (i) or (-i)")
        exit(0)
    try:
        file = open(sys.argv[4])
    except FileNotFoundError:
        print("Could not open file")
        exit(0)
    file.close()

    command.Remove(sys.argv[2:])

if commandArg == "merge":
    for f in sys.argv[3:]:
        try:
            file = open(f)
        except FileNotFoundError:
            print("Could not open file, all arguments after merge command need to be valid files")
            exit(0)
        file.close()
    command.Merge(sys.argv[2:])

if commandArg == "list":
    if len(sys.argv[2:]) != 1:
        print("Error: the list command takes 1 argument, which is the file to be listed")
        exit(0)

    try:
        file = open(sys.argv[2])
    except FileNotFoundError:
        print("Could not open file")
        exit(0)
    file.close()

    command.List(sys.argv[2])

if commandArg == "copy":
    if len(sys.argv[2:]) != 2:
        print("Error: the copy command takes 2 arguments")
        exit(0)

    try:
        file = open(sys.argv[2])
    except FileNotFoundError:
        print("Could not open file")
        exit(0)

    command.Copy(sys.argv[2:])

