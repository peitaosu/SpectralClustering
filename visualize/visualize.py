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
    
    def visualize(self):
        plt.plot(self.data["X"], self.data["Y"], 'ro')
        plt.axis([450, 600, -1000, 5000])
        plt.show()

if __name__ == "__main__":
    input = sys.argv[1]
    visualizer = Visualizer(input)
    visualizer.visualize()
