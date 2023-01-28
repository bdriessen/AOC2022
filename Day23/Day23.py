#
# Advent of code 2022: Day 23
#
# Author: Bart Driessen
# Start date: 2023-01-28
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
        map = np.array([list(x) for x in lines])
    return map

def parse_input():
    return

def move(uv, map, rule):
    u = uv[0]
    v = uv[1]
    if rule == 0:
        if map[u-1][v-1] == "." and map[u-1][v] == "." and map[u-1][v+1] == ".":  # North is empty
            ab = [u-1,v]
    elif rule == 1:
        if map[u+1][v+1] == "." and map[u+1][v] == "." and map[u+1][v+1] == ".":  # South is empty
            ab = [u+1,v]
    elif rule == 2:
        if map[u-1][v-1] == "." and map[u][v-1] == "." and map[u+1][v-1] == ".":  # West is empty
            ab = [u,v-1]
    elif rule == 3:
        if map[u-1][v+1] == "." and map[u][v+1] == "." and map[u+1][v+1] == ".":  # East is empty
            ab = [u,v+1]
    else:
        ab = []  # No move possible
    return ab

def try_move(uv, map, rule_idx):
    ridx = rule_idx
    ab = move(uv, map, ridx)
    if ab == []:
        ridx += 1
        if ridx > 3:
            ridx = 0
        ab = move(uv, map, ridx) is de index per elf of niet???

# Part 1
def part1(fn):
    map = read_input_file(fn)
    # extend map with a ring of '.'
    map = np.pad(map, 1, 'constant', constant_values='.')
    UV = []  # Coordinates of original elf
    AB = []  # Suggested new coordinates
    XY = []  # Coordinates of elf after move
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if map[i][j] == "#":
                UV.append([i, j])
    for i in range(len(UV)):
        ab = move(UV[i], map)
        AB.append(ab)
    for i in range(len(UV)):
        if UV.count(UV[i]) == 1:
            XY.append(AB[i])
        else:
            XY.append(UV[i])
    for i in range(len(XY)):
        map[UV[i][0]][UV[i][1]] = "."
        map[XY[i][0]][XY[i][1]] = "#"

    # Chek if top row is empty
    if map[0].all() == ".":  # all() returns True if all elements are True
        map = np.delete(map, 0, 0)
    # Check if bottom row is empty
    if map[-1].all() == ".":  # all() returns True if all elements are True
        map = np.delete(map, -1, 0)
    # Check if left column is empty
    if map[:, 0].all() == ".":  # all() returns True if all elements are True
        map = np.delete(map, 0, 1)
    # Check if right column is empty
    if map[:, -1].all() == ".":  # all() returns True if all elements are True
        map = np.delete(map, -1, 1)

    return 0

# Part 2
def part2(fn):

    return




def main():
    real = False
    part = 1


    # Start timer
    tic = time.perf_counter()
    if part == 1:
        if real:
            fn = "Day23/input.txt"
        else:
            fn = "Day23/input_test.txt"
        res1 = part1(fn)
        print("Part 1: ", res1)
    else:
        if real:
            fn = "Day23/input.txt"
        else:
            fn = "Day23/input_test.txt"
        res2 = part2(fn)
        print("Part 2: ", res2)
    toc = time.perf_counter()
    print(f"Time elapsed: {toc - tic:0.4f} seconds")
    return
