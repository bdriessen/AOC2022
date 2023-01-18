#
# Advent of code 2022: Day 19
#
# Author: Bart Driessen
# Start date: 2023-01-18
# Part 1 done:
# Part 2 done:
#
import re

# Read input file
def read_input_file(fn):

    with open(fn) as f:
        lines = f.readlines()
    for line in lines:
        sections = re.split(r': ', line)[1].split('. ')
        for section in sections:
            for x, y in re.findall(r'(\d+) (\w+)', section):
                print(x, y)

    return


def parse_input():
    return

# Part 1
def part1(fn):
    read_input_file(fn)
    return 0


# Part 2
def part2(fn):
    return 0


def main(realinput):
    if realinput:
        fn = "Day19/input.txt"
    else:
        fn = "Day19/testinput.txt"

    res1 = part1(fn)
    print("Part 1: ", res1)
#    res2 = part2(fn)
#    print("Part 2: ", res2)
    return


if __name__ == "__main__":
    #    main(True)
    #    main(False)
    pass
