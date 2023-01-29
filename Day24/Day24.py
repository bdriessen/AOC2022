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
#        print("Blizzards:\n", self.blizzards)
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

    def print_state(self):
        state = self.state.copy()
        for row in range(1, len(state)-1):
            for col in range(1, state.shape[1]-1):
                state[row,col] = "."
        for blizzard in self.blizzards:
            dir = blizzard[2]
            if dir == (-1,0):
                state[blizzard[0],blizzard[1]] = "^"
            elif dir == (1,0):
                state[blizzard[0],blizzard[1]] = "v"
            elif dir == (0,-1):
                state[blizzard[0],blizzard[1]] = "<"
            elif dir == (0,1):
                state[blizzard[0],blizzard[1]] = ">"
        for row in range(len(state)):
            print("".join(state[row]))
        return

def avoid_blizzards(state, start, end):
    blizzards = Blizzards(state)
    # for i in range(10):
    #     blizzards.move()
    #     print(blizzards.blizzards)
    #     print(blizzards.blizzard_cells)

    solutions = set()

    solutions.add(start)
    cycle = 0
    #    blizzards.print_state()
    while not end in solutions:
        cycle += 1
        solutions_new = set()
        blizzards.move()
        for sol in solutions:
            for step in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
                #               print(step)
                new_pos = (sol[0] + step[0], sol[1] + step[1])
                if new_pos[0] <= 0 or new_pos[0] >= len(blizzards.state) - 1:
                    if new_pos != start and new_pos != end:
                        continue
                if new_pos[1] <= 0 or new_pos[1] >= blizzards.state.shape[1] - 1:
                    continue
                if not new_pos in blizzards.blizzard_cells:
                    solutions_new.add(new_pos)
        solutions = solutions_new.copy()
        #       print(solutions)
        if cycle % 1000 == 0:
            print("Cycle: ", cycle)
    #       blizzards.print_state()
    #   print("Cycle: ", cycle, " Solutions: ", solutions)

    return cycle

# Part 1
def part1(fn):
    state = read_input_file(fn)
    blizzards = Blizzards(state)
    # for i in range(10):
    #     blizzards.move()
    #     print(blizzards.blizzards)
    #     print(blizzards.blizzard_cells)
    start = end = (0,0)
    solutions = set()
    for col in range(blizzards.state.shape[1]):
        if state[0,col] == ".":
            start = (0,col)
        if state[-1,col] == ".":
            end = (len(state)-1,col)
#    print(start, end)

    solutions.add(start)
    cycle = 0
#    blizzards.print_state()
    while not end in solutions:
        cycle += 1
        solutions_new = set()
        blizzards.move()
        for sol in solutions:
            for step in [(0,1),(0,-1),(1,0),(-1,0),(0,0)]:
 #               print(step)
                new_pos = (sol[0]+step[0], sol[1]+step[1])
                if new_pos[0] <= 0 or new_pos[0] >= len(blizzards.state)-1:
                    if new_pos != start and new_pos != end:
                        continue
                if new_pos[1] <= 0 or new_pos[1] >= blizzards.state.shape[1]-1:
                    continue
                if not new_pos in blizzards.blizzard_cells:
                    solutions_new.add(new_pos)
        solutions = solutions_new.copy()
#       print(solutions)
        if cycle % 1000 == 0:
            print("Cycle: ", cycle)
 #       blizzards.print_state()
 #   print("Cycle: ", cycle, " Solutions: ", solutions)

    return cycle



# Part 2
def part2(fn):
    return 0




def main():
    real = True
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
