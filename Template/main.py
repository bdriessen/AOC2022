#
# Advent of code 2022: Day xx
#
# Author: Bart Driessen
# Date: xxxx-xx-xx
#

# Read input file
def read_input_file(fn):
    with open(fn, "r") as file:
        return file.read().splitlines()

# Parse input file
def parse_input_file(input_file):
    return int(input_file[0]), input_file[1].split(",")

# Part 1
def part1(fn):
    input = read_input_file(fn)

    return

# Part 2
def part2(fn):
    input = read_input_file(fn)

    return


if __name__ == "__main__":

    testrun = True
#    testrun = False

    if testrun:
        res1 = part1("testinput.txt")
        print("Part 1: ", res1)
        res2 = part2("testinput.txt")
        print("Part 2: ", res2)
    else:
        res1 = part1("input.txt")
        print("Part 1: ", res1)
        res2 = part2("input.txt")
        print("Part 2: ", res2)


