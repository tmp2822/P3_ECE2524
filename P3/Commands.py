import re

class Commands:

    def Search(self, args):
        caseSensitivity = args[0]
        searchString = args[1]
        fileName = args[2]
        lineCount = 0
        found = False

        with open(fileName, 'r') as file:
            for line in file:
                lineCount += 1
                if caseSensitivity == '-i':
                    if re.search(searchString, line):
                        print("(" + searchString + ")", "found at line number: ", lineCount, "\n")
                        print(line)
                        found = True
                else:
                    if re.search(searchString, line, re.IGNORECASE):
                        print("(" + searchString + ")", "found at line number: ", lineCount, "\n")
                        print(line)
                        found = True
            if found == False:
                print("(" + searchString + ")", "was not found")

    def Remove(self, args):
        caseSensitivity = args[0]
        searchString = args[1]
        fileName = args[2]
        lineCount = 0
        found = False
        updatedFileData = []

        with open(fileName, 'r') as file:
            for line in file:
                lineCount += 1
                if caseSensitivity == '-i':
                    if re.search(searchString, line):
                        print("(" + searchString + ")", "removed at line number: ", lineCount, "\n")
                        print(line)
                        line = re.sub(searchString, "", line)
                        found = True
                else:
                    if re.search(searchString, line, re.IGNORECASE):
                        print("(" + searchString + ")", "removed at line number: ", lineCount, "\n")
                        print(line)
                        line = re.sub(searchString, "", line, 0, re.IGNORECASE)
                        found = True
                updatedFileData.append(line)

            if found == False:
                print("(" + searchString + ")", "was not found")
            else:
                with open(fileName, 'w') as file:
                    for line in updatedFileData:
                        file.write(line)

    def Merge():
        return 0

    def List():
        return 0

    def Copy():
        return 0
