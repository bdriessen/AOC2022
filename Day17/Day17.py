#
# Advent of code 2022: Day 17
#
# Author: Bart Driessen
# Date: 2022-01-04
#

import numpy as np
from os import system, name
import time

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Token:
    token0 = np.array([[1, 1, 1, 1]])
    token1 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    token2 = np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]])
    token3 = np.array([[1], [1], [1], [1]])
    token4 = np.array([[1, 1], [1, 1]])

    def __init__(self, nr, top):

        if nr == 0:
            self.token = self.token0
            self.low = [0, 0, 0, 0]
            self.high = [0, 0, 0, 0]
            self.left = [0]
            self.right = [3]
        elif nr == 1:
            self.token = self.token1
            self.low = [1, 0, 1]
            self.high = [1, 2, 1]
            self.left = [1, 0, 1]
            self.right = [1, 2, 1]
        elif nr == 2:
            self.token = self.token2
            self.low = [0, 0, 0]
            self.high = [0, 0, 2]
            self.left = [0, 2, 2]
            self.right = [2, 2, 2]

        elif nr == 3:
            self.token = self.token3
            self.low = [0]
            self.high = [3]
            self.left = [0,0,0,0]
            self.right = [0,0,0,0]
        elif nr == 4:
            self.token = self.token4
            self.low = [0, 0]
            self.high = [1, 1]
            self.left = [0, 0]
            self.right = [1, 1]
        self.x = 2
        self.y = top + 3 + 1

        self.state = "idle"  # idle, moving, landed
        self.vx = 0
        self.vy = 0

        return

    def vel(self, vy, vx):
        self.vx = vx
        self.vy = vy
        return

    def move(self):
        self.y += self.vy
        self.x += self.vx
        return

    def __str__(self):
        return str(self.token)


class Tower:
    def __init__(self, line):
        self.height = 0
        self.tower = np.ones((1, 7), dtype=np.int8)
        print("self.tower", self.tower)
        self.tower_tops = np.zeros(7, dtype=int)
        print("self.tower_tops", self.tower_tops)
        self.next_token = Token(0, 0)
        self.throttle = line
        self.offset = 0

    def __str__(self):
        return "Tower height: " + str(self.height)

    def can_move_down(self, token):
        # Calculate distance to tower for each column of token
        for col in range(token.token.shape[1]):
            col_token_bottom = token.y + token.low[col]
            if self.tower[col_token_bottom -1, token.x + col] == 1:
                return False
        return True

    def can_move_left(self, token):
        for row in range(token.y, token.y + token.token.shape[0]):
            left_1_col = token.x + token.left[row - token.y]
            if left_1_col == 0:
                return False
            if left_1_col > 0:
                if self.tower[row, left_1_col - 1] == 1:
                    return False
        return True

    def can_move_right(self, token):
        for row in range(token.y, token.y + token.token.shape[0]):
            right_1_col = token.x + token.right[row - token.y]
            if right_1_col == 6:
                return False
            if right_1_col < 6:
                if self.tower[row, right_1_col + 1] == 1:
                    return False
        return True

    def update_tower(self, token):
        for row in range(token.y, token.y + token.token.shape[0]):
            for col in range(token.token.shape[1]):
                if token.token[row - token.y, col] == 1:
                    self.tower[row, token.x + col] = 1
            # Update tower_tops as maximum index of 1 in each column
            for col in range(token.token.shape[1]):
                # Find highest rownumber with 1 in this column
                if token.y + token.high[col] > self.tower_tops[token.x + col]:
                    self.tower_tops[token.x + col] = token.y + token.high[col]
#        print("Tower tops updated ", self.tower_tops)
        return

    def plot(self, nrows, ncols):
        clear()
        for plotrow in range(nrows):
            towerstr = ""
            for plotcol in range(ncols):
                towerrow = nrows*ncols - 1 - plotcol*nrows - plotrow
                if towerrow < len(self.tower):
                    towerstr += str(self.tower[towerrow, :])
                else:
                    towerstr += "_" * 15
            print(towerstr)
        time.sleep(0.1)
        return


    def simulate(self):
        tokenlist = []
        tokenlist.append(Token(0, 0))
        tokenlist.append(Token(1, 0))
        tokenlist.append(Token(2, 0))
        tokenlist.append(Token(3, 0))
        tokenlist.append(Token(4, 0))

        tkn = 0
        throttle_index = 0
        while tkn < 1000000000000:
#        while tkn < 2022:
            if tkn % 100000 == 0:
                print("tkn", tkn)
                print("Length of tower", len(self.tower))
            # calculate max of tower_tops
            token = tokenlist[tkn % 5]
            token.x = 2
            token.y = self.tower_tops.max() + 3 + 1

#            token = Token(tkn % 5, np.max(self.tower_tops))
#            print("New token: ", tkn % 5)
            token.vel(0, 0)
            token.state = "moving"
            extra_rows = token.y + token.token.shape[0] - self.tower.shape[0]
            if extra_rows > 0:
                self.tower = np.vstack((self.tower, np.zeros((extra_rows, 7), dtype=np.int8)))


            while token.state == "moving":
                throttle = self.throttle[throttle_index]
#                print("Throttle: ", throttle)
                throttle_index += 1
                throttle_index = throttle_index % len(self.throttle)

                if throttle == '<' and self.can_move_left(token):
                    token.vel(0, -1)
                elif throttle == '>' and self.can_move_right(token):
                    token.vel(0, 1)
                token.move()  # Horizontal movement by throttle
                token.vel(0,0)
                if self.can_move_down(token):
                    token.vel(-1,0)
                    token.state = "moving"
                else:
                    token.vel(0, 0)
                    token.state = "landed"
                token.move()  # Vertical movement by gravity
                token.vel(0,0)
                if token.state == "landed":
                    self.update_tower(token)
                    tkn += 1
#            del token
            self.plot(20, 10)


            if tkn % 100 == 0:
                 # find rows with all 1's
                 rows = []
                 for row in range(1, self.tower.shape[0]):
                     if np.sum(self.tower[row, :]) == 7:
                         rows.append(row)
                 if len(rows) > 0:

                     highest_row = np.max(rows)

                     # delete all rows from 0 to highest_row, and keep highest_row

                     self.tower = self.tower[highest_row:, :]

                     self.offset += highest_row
                     self.tower_tops -= highest_row
#                     print("Removed rows. Highest row is now:", self.tower.shape[0] - 1)


#            print(self.tower)

        print("Tower height: ", np.max(self.tower_tops)+self.offset)
        # Print maximum x value of tower

        # find rows with only 1's
        rows = []
        for row in range(self.tower.shape[0]):
            if np.sum(self.tower[row, :]) == 7:
                rows.append(row)
        print("Rows with only 1's: ", rows)
        return


# Read input file
def read_input_file(fn):
    # Read single line input file and store in list
    with open(fn, "r") as f:
        line = f.readline().strip()
        print("Length of input file: ", len(line))
    return line


# Part 1
def part1(fn):
    line = read_input_file(fn)

    tower = Tower(line)
    tower.simulate()
    print("Input length: ", len(line))
    return 0


# Part 2
def part2(fn):
    return 0


def main(realinput):
    if realinput:
        fn = "Day17/input.txt"
    else:
        fn = "Day17/testinput.txt"

    res1 = part1(fn)
    print("Part 1: ", res1)
    res2 = part2(fn)
    print("Part 2: ", res2)
    return


if __name__ == "__main__":
    #    main(True)
    #    main(False)
    pass
