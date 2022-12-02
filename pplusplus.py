import sys

class PPlusPlus:
    def __init__(self):
        self.t = 0

        arglen = len(sys.argv) - 1

        if arglen > 1 or arglen == 0:
            print("Usage python pplusplus.py [File]")
        else:
            self.compile(sys.argv[1])

    def compile(self, path):
        file = open(path, "r", encoding="utf8")
        bytes = file.read()
        file.close()

        oPath = path[:-4] + "cpp"
        self.output = open(oPath, "w")

        startL = True
        tNum = 0

        for byte in bytes:
            match(byte):
                case '\n':
                    startL = True
                    tNum = 0
                case ' ':
                    if startL: tNum =+ 1
                case _:
                    if startL: self.evaluateTabs(tNum)
                    startL = False

            self.output.write(byte)
            

        self.output.close()

    def evaluateTabs(self, n):
        diff = self.t - n
        if(self.t > n): 
            for i in range(diff):
                self.output.write("}\n")
        else:
            for i in range(-diff):
                self.output.write("{\n")
                self.output.write("\t"*n)

        self.t = n

if __name__ == "__main__":
    PPlusPlus()
#EOF