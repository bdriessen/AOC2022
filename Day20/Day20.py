#
# Advent of code 2022: Day 20
#
# Author: Bart Driessen
# Start date: 2023-01-20
# Part 1 done:
# Part 2 done:
#

import numpy as np

# Read input file
def read_input_file(fn):
    with open(fn) as f:
        lines = f.readlines()
        # remove \n and empty strings
        lines = [x.strip() for x in lines if x.strip()]
        print(lines)
        msg = [int(x) for x in lines]
    return msg

def parse_input():
    return


class GPS:
    def __init__(self, msg):
        self.msg = np.array(msg)
        self.decrypted = self.msg
        self.length = len(msg)
        self.msg_ptr = np.arange(self.length)
        return

    def decode(self):
        # Find where to insert
        for idx, item in enumerate(self.msg):
            ptr = self.msg_ptr[idx]   # pointer points to the position in the decrypted message
            to_move = self.decrypted[ptr]
            if item != to_move:
                print("Error at index", idx)
                return
            if item > 0:
                move = item % self.length
            elif item < 0:
                # Move backwards identical to moving forward, but complemented
                move = self.length - item % self.length
            else:
                move = 0

            # Step 1: insert the item to its new position
            new_idx = (ptr + move) % self.length
            self.decrypted = np.insert(self.decrypted, new_idx, item)
            # Step 2: remove the old item
            self.decrypted = np.delete(self.decrypted, self.msg[ptr], idx)
            # Step 3: update all affected entries in msg_ptr
            self.msg_ptr[idx] = new_idx

            if ptr + move < self.length:

                ### fout!

                self.msg_ptr[idx+1:new_idx] -= 1
            if idx + move >= self.length:
                # The item was moved beyond the end of the list
                # Update all entries in msg_ptr
                self.msg_ptr[idx+1:] -= 1
                self.msg_ptr[:new_idx] -= 1
                self.msg_ptr[0] = self.length - 1
            print(idx, "Item: ", item, "Move: ", move, "New idx: ", new_idx, "Original list: ", self.msg, "New list: ", self.decrypted)
        return


# Part 1
def part1(fn):
    msg = read_input_file(fn)
    gps = GPS(msg)
    gps.decode()
    return 0

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
