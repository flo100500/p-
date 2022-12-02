import sys

class PPlusPlus:
    def __init__(self):
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
        output = open(oPath, "w")
        output.write("test")
        output.close()


if __name__ == "__main__":
    PPlusPlus()
