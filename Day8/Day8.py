# This is a sample Python script.

import numpy as np
import matplotlib.pyplot as plt

def read_input(filename):
    with open(filename, 'r') as f:
        # create numpy matrix with cell values from each digit in the input file
        return np.array([[int(digit) for digit in line.strip()] for line in f.readlines()])



def parse_input(lines, G):
    return

def main():
    matrix = read_input('testinput.txt')
    print(matrix)

    return

if __name__ == '__main__':
    main()

