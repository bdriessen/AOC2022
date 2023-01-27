#
# Advent of code 2022: Day 20
#
# Author: Bart Driessen
# Start date: 2023-01-23
# Part 1 done:
# Part 2 done:
#
import re
import numpy as np
import time

# Read input file
def read_map_file(fn):
    with open(fn) as f:
        lines = f.readlines()
        # remove \n
        lines = [x.strip('\n') for x in lines]

        nrows = len(lines)
        ncols = 0
        for line in lines:
            ncols = max(ncols, len(line))
        map = np.empty((nrows, ncols,), dtype=str)
        map[:] = ' '
        for row in range(nrows):
            for col in range(len(lines[row])):
                map[row, col] = lines[row][col]

        # Create wrap around
        wrap_horizontal = np.empty((nrows, 2,), dtype=int)
        for row in range(nrows):
            for col in range(ncols):
                if map[row, col] == '#' or map[row, col] == '.':
                    wrap_horizontal[row, 1] = col
                    break
            for col in range(ncols-1, -1, -1):
                if map[row, col] == '#' or map[row, col] == '.':
                    wrap_horizontal[row, 0] = col
                    break
        wrap_vertical = np.empty((2, ncols,), dtype=int)
        for col in range(ncols):
            for row in range(nrows):
                if map[row, col] == '#' or map[row, col] == '.':
                    wrap_vertical[1, col] = row
                    break
            for row in range(nrows-1, -1, -1):
                if map[row, col] == '#' or map[row, col] == '.':
                    wrap_vertical[0, col] = row
                    break
        # for row in range(nrows):
        #     print(map[row, :])
        #
        # print(repr(wrap_horizontal))
        # print(repr(wrap_vertical))


    return map, wrap_vertical, wrap_horizontal

def read_traject_file(fn):
    traject = []
    with open(fn) as f:
        # read alternating numbers and letters and store in list
        line = f.readline()
        seq = re.split(r'(\d+)', line)
        seq = [x for x in seq if x]
        for i in range(0, len(seq), 2):
            traject.append((seq[i], seq[i+1]))

#    print(traject)
    return traject


# Part 1
def part1(mapfn, trajectfn):
    map, wrap_v, wrap_h = read_map_file(mapfn)
    traject = read_traject_file(trajectfn)

    idx_row = 0
    idx_col = 0
    for col in range(map.shape[1]):
        if map[idx_row, col] == '.' or map[idx_row, col] == '#':
            idx_col = col
            break
    print(idx_row, idx_col)



    return 0

# Part 2
def part2(mapfn, trajectfn):

    return 0




def main():
    real = False
    part = 1


    # Start timer
    tic = time.perf_counter()

    if part == 1:
        if real:
            mapfn = "Day22/input_map.txt"
            trajectfn = "Day22/input_traject.txt"
        else:
            mapfn = "Day22/input_test_map.txt"
            trajectfn = "Day22/input_test_traject.txt"
        res1 = part1(mapfn, trajectfn)
        print("Part 1: ", res1)
    else:
        if real:
            mapfn = "Day22/input_map.txt"
            trajectfn = "Day22/input_traject.txt"
        else:
            mapfn = "Day22/input_test_map.txt"
            trajectfn = "Day22/input_test_traject.txt"
        res2 = part2(mapfn, trajectfn)
        print("Part 2: ", res2)

    # Stop timer
    toc = time.perf_counter()
    print(f"Time elapsed: {toc - tic:0.4f} seconds")
    return
