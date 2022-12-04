import sys

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
        fileStr = file.read()
        file.close()

        oPath = path[:-4] + "cpp"
        self.output = open(oPath, "w")

        allKeywords = ["#","(","{","}",")","//","if","else","class","goto","try","catch","EOF"]
        tempList = list(fileStr.split("\n"))
        for i in range (len(tempList)):
            if any(word in tempList[i] for word in allKeywords):            
                print(tempList[i])                            
            else:
                print(tempList[i]+";")
        
        startLine = True
        nTabs = 0

        for char in fileStr:
            match(char):
                case '\n':
                    startLine = True
                    nTabs = 0
                case ' ':
                    if startLine: nTabs =+ 1
                case _:
                    if startLine: self.evaluateTabs(nTabs)
                    startLine = False

            self.output.write(char)
            
        self.output.close()

    def evaluateTabs(self, nTabs):
        diff = self.nTabsPrev - nTabs
        if(self.nTabsPrev > nTabs): 
            for _ in range(diff):
                self.output.write("}\n")
        else:
            for _ in range(-diff):
                self.output.write("{\n")
                self.output.write("\t"*nTabs)

        self.nTabsPrev = nTabs

if __name__ == "__main__":
    PPlusPlus()

