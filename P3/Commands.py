import re

class Commands:

    def Search(self, args):
        caseSensitivity = args[0]
        searchString = args[1]
        fileName = args[2]
        lineCount = 0

        with open(fileName, 'r') as file:
            for line in file:
                lineCount += 1
                if caseSensitivity == 'i':
                    if re.search(searchString, line):
                        print("(" + searchString + ")", "found at line number: ", lineCount, "\n")
                        print(line)
                else:
                    if re.search(searchString, line, re.IGNORECASE):
                        print("(" + searchString + ")", "found at line number: ", lineCount, "\n")
                        print(line)
    def Remove():
        return 0

    def Merge():
        return 0

    def List():
        return 0

    def Copy():
        return 0
