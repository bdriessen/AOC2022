#
# Advent of code 2022: Day 24
#
# Author: Bart Driessen
# Start date: 2023-01-29
# Part 1 done:
# Part 2 done:
#

import time
import numpy as np

# Read input file
def read_input_file(fn):
    with open(fn) as f:
        lines = f.readlines()
        # remove \n and empty strings
        lines = [x.strip() for x in lines if x.strip()]
        state = np.array([list(x) for x in lines])
    return state

def parse_input():
    return

class Blizzards:
    def __init__(self, state):
        self.state = state
        self.blizzards = []
        self.blizzard_cells = []
        self.directions = {
            "^": (-1,0),
            "v": (1,0),
            "<": (0,-1),
            ">": (0,1) }
        self.parse_blizzards()
        return

    def parse_blizzards(self):
        for row in range(len(self.state)):
            for col in range(len(self.state[row])):
                if self.state[row][col] in self.directions:
                    self.blizzards.append([row,col,self.directions[self.state[row][col]]])
                    self.blizzard_cells.append([row,col])
        print("Blizzards:\n", self.blizzards)
        return

    def move(self):
        new_blizzards = []
        for idx, blizzard in enumerate(self.blizzards):
            new_row = blizzard[0] + blizzard[2][0]
            new_col = blizzard[1] + blizzard[2][1]

            if new_col >= self.state.shape[1]-1:
                new_col = 1
            elif new_col <= 0:
                new_col = len(self.state[1])-2
            if new_row >= len(self.state)-1:
                new_row = 1
            elif new_row <= 0:
                new_row = len(self.state)-2
            new_blizzards.append([new_row, new_col, blizzard[2]])

        self.blizzards = new_blizzards
        self.blizzard_cells = set([(x[0],x[1]) for x in self.blizzards])
        return

# Part 1
def part1(fn):
    state = read_input_file(fn)
    blizzards = Blizzards(state)
    # for i in range(10):
    #     blizzards.move()
    #     print(blizzards.blizzards)
    #     print(blizzards.blizzard_cells)

    return 0


# Part 2
def part2(fn):
    return 0




def main():
    real = False
    part = 1


    # Start timer
    tic = time.perf_counter()
    if part == 1:
        if real:
            fn = "Day24/input.txt"
        else:
            fn = "Day24/input_test.txt"
        res1 = part1(fn)
        print("Part 1: ", res1)
    else:
        if real:
            fn = "Day24/input.txt"
        else:
            fn = "Day24/input_test.txt"
        res2 = part2(fn)
        print("Part 2: ", res2)
    toc = time.perf_counter()
    print(f"Time elapsed: {toc - tic:0.4f} seconds")
    return
