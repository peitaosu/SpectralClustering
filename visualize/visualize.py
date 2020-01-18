import os, sys

class Visualizer():
    
    def __init__(self, input=None):
        if input:
            self.get_data_from_file(input)
    
    def get_data_from_file(self, input):
        self.input = input
        with open(input) as in_file:
            self.data = []
            for line in in_file.readlines():
                self.data.append((line.split("\t")[0], line.split("\t")[1]))
       
if __name__ == "__main__":
    input = sys.argv[1]
    visualizer = Visualizer(input)
    print(visualizer.data)
