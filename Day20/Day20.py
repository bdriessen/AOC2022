#
# Advent of code 2022: Day 20
#
# Author: Bart Driessen
# Start date: 2023-01-20
# Part 1 done:
# Part 2 done:
#

# Read input file
def read_input_file(fn):
    with open(fn) as f:
        lines = f.readlines()
        msg = [int(x) for x in lines]
    return msg

def parse_input():
    return

# Part 1
def part1(fn):
    msg = read_input_file(fn)
    print(msg)
    return 0

class GPS:
    def __init__(self, msg):
        self.msg = msg
        self.decrypted = msg
        self.lenght = len(msg)
        self.msg_ptr = [x for x in range(len(msg))]
        self.msg_ptr_ptr = 0
        return

    def insert(self, pos):
        # Find where to insert
        ptr = self.msg_ptr[pos]
        val = self.decrypted[ptr]
        val2 = self.decrypted[pos]
        if val1 != val2:
            print("Error")
            return

        # Calculate new position






# Part 2
def part2(fn):
    return 0


def main(realinput):
    if realinput:
        fn = "Day20/input.txt"
    else:
        fn = "Day20/input_test.txt"

    res1 = part1(fn)
    print("Part 1: ", res1)
#    res2 = part2(fn)
#    print("Part 2: ", res2)
    return
