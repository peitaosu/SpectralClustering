import os, path

class Preprocesser():
    def __init__(self):
        self.data = {
            "X": [],
            "Y": []
        }

    def process(self, input):
        if not os.path.isfile(input):
            print(input + " is not exists.")
            sys.exit(-1)
        with open(input) as in_file:
            for line in in_file.readlines():
                self.data["X"].append(float(line.split("\t")[0]))
                self.data["Y"].append(float(line.split("\t")[1]))
        return self.data

