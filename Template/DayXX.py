#
# Advent of code 2022: Day xx
#
# Author: Bart Driessen
# Date: xxxx-xx-xx
#

import time

# Read input file
def read_input_file(fn):
    with open(fn, "r") as file:
        return file.read().splitlines()

# Parse input file
def parse_input_file(input_file):
    return

# Part 1
def part1(fn):
    input = read_input_file(fn)

    return

# Part 2
def part2(fn):
    input = read_input_file(fn)

    return


def main():
    real = False   # True = real input, False = test input
    part = 1
    day = 24

    # Start timer
    tic = time.perf_counter()
    if real:
        fn = "Day" + str(day) + "/input.txt"
    else:
        fn = "Day" + str(day) + "/input_test.txt"

    if part == 1:
        res1 = part1(fn)
        print("Part 1: ", res1)
    else:
        res2 = part2(fn)
        print("Part 2: ", res2)
    toc = time.perf_counter()
    print(f"Time elapsed: {toc - tic:0.4f} seconds")

    return
