import os, sys
import matplotlib.pyplot as plt

class Visualizer():
    
    def __init__(self, input=None):
        if input:
            self.get_data_from_file(input)
    
    def get_data_from_file(self, input):
        self.input = input
        with open(input) as in_file:
            self.data = {
                "X": [],
                "Y": []
            }
            for line in in_file.readlines():
                self.data["X"].append(float(line.split("\t")[0]))
                self.data["Y"].append(float(line.split("\t")[1]))
    
    def show(self, size=1):
        plt.axis([min(self.data["X"]), max(self.data["X"]), min(self.data["Y"]), max(self.data["Y"])])
        plt.scatter(self.data["X"], self.data["Y"], s=size)
        plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("python visualize.py <path_to_data_file>")
        sys.exit(-1)
    input = sys.argv[1]
    visualizer = Visualizer(input)
    visualizer.show()
