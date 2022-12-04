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

        oPath = path[:-4] + "cpp"
        self.output = open(oPath, "w")

        startLine, printChar = True, True
        nSpaces = 0

        #creating a list with all keywords where we dont want semicolon at the end
        allKeywords = ["#",";","(","{","}",")","===","//","if","else","class","goto","try","catch","EOF"]
        #took the file and split it into a list
        #all the elements in the list are a line
        tempList = list(fileStr.split("\n"))
        for i in range (len(tempList)):         
            #if we find an empty line we skip it   
            if (re.search("^\s*$", tempList[i])):
                continue
            #keyword match dont add semicolon
            elif any(word in tempList[i] for word in allKeywords):            
                print(tempList[i])                       
            else:
                #no match add semicolon
                print(tempList[i]+";")

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
                        self.evaluateTabs(int(nSpaces/4))
                        self.output.write(" "*nSpaces)
                        startLine = False

            if printChar: self.output.write(char)
            
        self.output.close()

    def evaluateTabs(self, nTabs):
        diff = self.nTabsPrev - nTabs
        if(self.nTabsPrev > nTabs): 
            for i in range(diff):
                self.output.write("\t"*(self.nTabsPrev-1-i))
                self.output.write("}\n")


        else:
            for _ in range(-diff):
                self.output.write("\t"*(nTabs-1))
                self.output.write("{\n")

        self.nTabsPrev = nTabs

if __name__ == "__main__":
    PPlusPlus()