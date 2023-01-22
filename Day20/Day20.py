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
        msg = [int(x) for x in lines]
    return msg

def parse_input():
    return


class GPS:
    def __init__(self, msg):
        msg_ = np.array(msg)
        idx_ = np.arange(len(msg))
        self.msg = np.c_[idx_, msg_]
        self.length = len(msg)
        return

    def decode(self):
        # Find where to insert
        started = False
        counter = 0
        for i in range(3010):
            old_message = self.msg.copy()
            idx = i % self.length
            # Find where to idx number is in the msg
            idx_in_msg = np.where(self.msg[:, 0] == idx)[0][0]
            entry = [idx, self.msg[idx_in_msg, 1]]
            if not started:
                if entry[1] == 0:
                    print("Started at iteration", i)
                    started = True
                    counter = 0
            else:
                counter += 1
                if counter%1000 == 0 and counter > 100:
                    print("Counter: ", counter, "Value = ", entry[1])
                    # Find where a zero is in the msg:
                    zero_idx = np.where(self.msg[:, 1] == 0)[0][0]
                    # print("Zero idx: ", zero_idx)
                    next_idx = (zero_idx + 1) % self.length
                    value_after_zero = self.msg[next_idx, 1]
                    print("Value after zero: ", value_after_zero)
            # Make index for this entry -1
            self.msg[idx_in_msg, 0] = -1

            # Find where to insert
            move_dist = self.msg[idx_in_msg, 1]

            if move_dist > 0:
                move_dist %= self.length
                insert_idx = (idx_in_msg + move_dist + 1) % self.length
            elif move_dist < 0:
                move_dist %= self.length
                insert_idx = (idx_in_msg + move_dist) % self.length
            else:
                insert_idx = (idx_in_msg + 1) % self.length

            # Insert
            self.msg = np.insert(self.msg, insert_idx, entry, axis=0)
            # Remove old entry
            delete_idx = np.where(self.msg[:, 0] == -1)[0][0]
            self.msg = np.delete(self.msg, delete_idx, axis=0)

            print("Counter: ", counter, "Old message: ", old_message.T[1], "Value: ", entry[1], "Dist: ", move_dist,
                 "New message: ", self.msg.T[1])
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
