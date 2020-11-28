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

    def Merge(self, args):
        mergedFileData = []
        outputFile = args[0]
        files = args[1:];
        for f in files:
            with open(f, 'r') as file:
                mergedFileData.append(file.read())

        with open(outputFile, 'w') as file:
            for line in mergedFileData:
                file.write(line)
                file.write("\n")

    def List():
        return 0

    def Copy():
        return 0
