import sys
import re

class PPlusPlus:
    def __init__(self):
        self.nTabsPrev = 0
        self.fileEndStr = "// File writen with P++"

        arglen = len(sys.argv) - 1

        if arglen > 1 or arglen == 0:
            print("Usage python pplusplus.py [File]")
        else:
            self.compile(sys.argv[1])

    def compile(self, path):
        #read file
        file = open(path, "r", encoding="utf8")
        fileStr = file.read() + "\n" + self.fileEndStr
        file.close()

        #compile line by line
        lines = fileStr.split("\n")

        outputLines = []

        for line in lines:
            line = self.addSemicolons(line)
            line = self.addCurlyBrackets(line)
            outputLines.append(line)

        #write file
        oPath = path[:-3] + "cpp"
        output = open(oPath, "w")
        output.write("".join(outputLines))
        output.close()
    
    def addSemicolons(self, line):
        #creating a list with all keywords where we dont want semicolon at the end
        allKeywords = ["#",";","{","}","if","else","class","goto","try","catch"]

        output, comment = "", ""
        #few different cases to add semicolons
        for j in range(len(line) - 1):       
            #if there is a comment within a line
            if (line[j] == '/' and line[j+1] == '/'):
                comment = line[j:]                
                line = line[:j]
                break

        #if we find an empty line we skip it   
        if (re.search("^\s*$", line)):
            pass
        #keyword match dont add semicolon
        elif any(word in line for word in allKeywords):            
            output = line                 
        else:
            #no match add semicolon                
            output = line + ";"

        output += comment + "\n"

        return output

    def addCurlyBrackets(self, line):
        #count Spaces in front of the line
        nSpaces, char = 0, ' '
        for char in line:
            if char == ' ': nSpaces += 1
            else: break
        
        #if line is not empty and do not start with a comment
        if char != ' ' and char != '/': 
            line = self.evaluateTabs(int(nSpaces/4), line)
        elif line.strip() == self.fileEndStr:
            line = self.evaluateTabs(0, "") + "\n" + self.fileEndStr
        
        return line
    
    def evaluateTabs(self, nTabs, output):
        diff = self.nTabsPrev - nTabs
        if(self.nTabsPrev < nTabs): 
            for i in range(-diff):
                output = "\t"*(nTabs-i-1) + "{\n" + output
        else:
            for i in range(diff):
                output = "\t"*(self.nTabsPrev - diff + i) + "}\n" + output

        self.nTabsPrev = nTabs
        return output
        

if __name__ == "__main__":
    PPlusPlus()