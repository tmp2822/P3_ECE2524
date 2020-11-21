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
    command.Search(sys.argv[2:])



