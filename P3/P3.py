import sys

class Commands:

    def Search():
        return 0

    def Remove():
        return 0

    def Merge():
        return 0

    def List():
        return 0

    def Copy():
        return 0

if len(sys.argv) < 2:
    print("Error to few arguments")
    exit(0)

print(sys.argv[1])


