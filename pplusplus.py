import sys
import re

class PPlusPlus:
    def __init__(self):
        self.nTabsPrev = 0

        arglen = len(sys.argv) - 1
        self.start = 0
        self.current = 0
        self.line = 1

        if arglen > 1 or arglen == 0:
            print("Usage python pplusplus.py [File]")
        else:
            self.compile(sys.argv[1])

    def compile(self, path):
        file = open(path, "r", encoding="utf8")
        fileStr = file.read() + "\n// File writen with P++"
        file.close()

        fileStr = self.addSemicolons(fileStr)
        fileStr = self.addCurlyBrackets(fileStr)

        oPath = path[:-3] + "cpp"
        output = open(oPath, "w")
        output.write(fileStr)
        output.close()

    def addSemicolons(self, fileStr):
        #creating a list with all keywords where we dont want semicolon at the end
        allKeywords = ["#",";", ":","{","}","//","if","else","class","goto","try","catch"]
        #took the file and split it into a list
        #all the elements in the list are a line
        fileList = list(fileStr.split("\n"))
        output = ""
        for line in fileList:         
            #if we find an empty line we skip it   
            if (re.search("^\s*$", line)):
                continue
            #keyword match dont add semicolon
            elif any(word in line for word in allKeywords):            
                output += line                  
            else:
                #no match add semicolon
                output += line + ";"

            output += "\n"

        return output
    
    def evaluateTabs(self, nTabs, output):
        diff = self.nTabsPrev - nTabs
        if(self.nTabsPrev > nTabs): 
            for i in range(diff):
                output += "\t"*(self.nTabsPrev-1-i)
                output += "}\n"

        else:
            for _ in range(-diff):
                output += "\t"*(nTabs-1)
                output += "{\n"

        self.nTabsPrev = nTabs
        return output

    def addCurlyBrackets(self, fileStr):
        startLine, printChar = True, True
        nSpaces = 0
        output = ""

        for char in fileStr:
            printChar = True
            match(char):
                case '\n':
                    startLine = True
                    nSpaces = 0
                case ' ':
                    if startLine:
                        nSpaces += 1
                        printChar = False
                case _:
                    if startLine: 
                        output = self.evaluateTabs(int(nSpaces/4), output)
                        output += " "*nSpaces
                        startLine = False

            if printChar: output += char

        return output

        

if __name__ == "__main__":
    PPlusPlus()