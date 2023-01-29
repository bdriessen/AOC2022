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
    ab = []
    if map[u+1][v] == "." and map[u-1][v] == "." and map[u][v-1] == "." and map[u][v+1] == "." \
            and map[u+1][v+1] == "." and map[u+1][v-1] == "." and map[u-1][v+1] == "." and map[u-1][v-1] == ".":
        # No empty spots around elf
        return []
    if rule == 0:
        if map[u-1][v-1] == "." and map[u-1][v] == "." and map[u-1][v+1] == ".":  # North is empty
            return [u-1,v]
    elif rule == 1:
        if map[u+1][v-1] == "." and map[u+1][v] == "." and map[u+1][v+1] == ".":  # South is empty
            return [u+1,v]
    elif rule == 2:
        if map[u-1][v-1] == "." and map[u][v-1] == "." and map[u+1][v-1] == ".":  # West is empty
            return [u,v-1]
    elif rule == 3:
        if map[u-1][v+1] == "." and map[u][v+1] == "." and map[u+1][v+1] == ".":  # East is empty
            return [u,v+1]
    return []

def try_move(uv, map, start_rule):
    rule = start_rule
    for i in range(4):

#        print("Checking rule: ", rule)
        ab = move(uv, map, rule)
        if not (ab == []):
            return ab
        rule = (rule+1) % 4
    return []


# Part 1
def part1(fn):
    map = read_input_file(fn)
    round = 0
    start_rule = -1

    while round < 10:
        round += 1

        start_rule = (start_rule + 1) % 4
        # extend map with a ring of '.'
        map = np.pad(map, 1, 'constant', constant_values='.')
  #      print("Round: ", round, " start_rule: ", start_rule)
        # print each row of map without quotes
#        for row in range(len(map)):
#            print(''.join(map[row]))
        UV = []  # Coordinates of original elf
        AB_dest = []  # Suggested new coordinates
        AB_source = []  # Coordinates before
        XY = []  # Coordinates of elf after move
        for i in range(0, len(map)):
            # Build list of elves
            for j in range(0, len(map[0])):
                if map[i][j] == "#":
                    UV.append([i, j])
#        print("UV: ", UV)
        for i in range(len(UV)):
            # Try to move. AB will contain the new coordinates. UV_fromAB will contain the original coordinates
            ab = try_move(UV[i], map, start_rule)
            if not (ab == []):
                AB_dest.append(ab)
                AB_source.append(UV[i])
 #       print("AB_source: ", AB_source)
 #       print("AB_dest: ", AB_dest)

        for i in range(len(AB_dest)):
            # check for collisions
            if AB_dest.count(AB_dest[i]) == 1:
                # No collision
                XY.append(AB_dest[i])
            else:
                # Collision
                XY.append(AB_source[i])
   #     print("XY: ", XY)
        for i in range(len(XY)):
            # Move elf
            map[AB_source[i][0]][AB_source[i][1]] = "."  # Remove elf from old position
        for i in range(len(XY)):
            map[XY[i][0]][XY[i][1]] = "#"  # Add elf to new position

        # Chek if top row is empty
        while (map[0, :]==".").all():  # all() returns True if all elements are True
            map = np.delete(map, 0, 0)
        # Check if bottom row is empty
        while (map[-1, :]==".").all():  # all() returns True if all elements are True
            map = np.delete(map, -1, 0)
        # Check if left column is empty
        while (map[:, 0]==".").all():  # all() returns True if all elements are True
            map = np.delete(map, 0, 1)
        # Check if right column is empty
        while (map[:, -1]==".").all():  # all() returns True if all elements are True
            map = np.delete(map, -1, 1)

    # Count empty spots
#    for row in range(len(map)):
#        print(''.join(map[row]))

    count = 0
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if map[i][j] == ".":
                count += 1

    print(count)


    return count


# Part 2
def part2(fn):

    map = read_input_file(fn)
    round = 0
    start_rule = -1
    has_moved = True

    while has_moved:
        round += 1
        has_moved = False
        if round % 100 == 0:
            print("Round: ", round)
        start_rule = (start_rule + 1) % 4
        # extend map with a ring of '.'
        map = np.pad(map, 1, 'constant', constant_values='.')
        #      print("Round: ", round, " start_rule: ", start_rule)
        # print each row of map without quotes
#        for row in range(len(map)):
#            print(''.join(map[row]))
        UV = []  # Coordinates of original elf
        AB_dest = []  # Suggested new coordinates
        AB_source = []  # Coordinates before
        XY = []  # Coordinates of elf after move
        for i in range(0, len(map)):
            # Build list of elves
            for j in range(0, len(map[0])):
                if map[i][j] == "#":
                    UV.append([i, j])
#        print("UV: ", UV)
        for i in range(len(UV)):
            # Try to move. AB will contain the new coordinates. UV_fromAB will contain the original coordinates
            ab = try_move(UV[i], map, start_rule)
            if not (ab == []):
                AB_dest.append(ab)
                AB_source.append(UV[i])
        #       print("AB_source: ", AB_source)
        #       print("AB_dest: ", AB_dest)

        for i in range(len(AB_dest)):
            # check for collisions
            if AB_dest.count(AB_dest[i]) == 1:
                # No collision
                XY.append(AB_dest[i])
                has_moved = True
            else:
                # Collision
                XY.append(AB_source[i])
        #     print("XY: ", XY)
        for i in range(len(XY)):
            # Move elf
            map[AB_source[i][0]][AB_source[i][1]] = "."  # Remove elf from old position
        for i in range(len(XY)):
            map[XY[i][0]][XY[i][1]] = "#"  # Add elf to new position

        # Chek if top row is empty
        while (map[0, :] == ".").all():  # all() returns True if all elements are True
            map = np.delete(map, 0, 0)
        # Check if bottom row is empty
        while (map[-1, :] == ".").all():  # all() returns True if all elements are True
            map = np.delete(map, -1, 0)
        # Check if left column is empty
        while (map[:, 0] == ".").all():  # all() returns True if all elements are True
            map = np.delete(map, 0, 1)
        # Check if right column is empty
        while (map[:, -1] == ".").all():  # all() returns True if all elements are True
            map = np.delete(map, -1, 1)


    # # Count empty spots
    # for row in range(len(map)):
    #     print(''.join(map[row]))
    #
    # count = 0
    # for i in range(0, len(map)):
    #     for j in range(0, len(map[0])):
    #         if map[i][j] == ".":
    #             count += 1

    print("Last round: ", round)


    return round




def main():
    real = True
    part = 2


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
