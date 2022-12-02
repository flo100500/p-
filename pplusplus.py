import sys

class PPlusPlus:
    def __init__(self):
        arglen = len(sys.argv) - 1
        self.start = 0
        self.current = 0
        self.line = 1

        if arglen > 1 or arglen == 0:
            print("Usage python pplusplus.py [File]")
        else:
            self.compile(sys.arg[1])

    def compile(self, path):
        file = open(path, "r", encoding="utf8")
        bytes = file.read()
        
            