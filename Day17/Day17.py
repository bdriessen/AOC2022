#
# Advent of code 2022: Day 17
#
# Author: Bart Driessen
# Date: 2022-01-04
#

import numpy as np


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
        self.y = top + 3 + self.token.shape[0]

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
    def __init__(self):
        self.height = 0
        self.tower = np.ones((1, 7), dtype=int)
        print("self.tower", self.tower)
        self.tower_tops = np.zeros(7, dtype=int)
        print("self.tower_tops", self.tower_tops)
        self.next_token = Token(0, 0)

    def __str__(self):
        return "Tower height: " + str(self.height)

    def can_move_down(self, token):
        for col in range(token.x, token.x + token.token.shape[1]):
            if self.tower_tops[col] >= token.y - token.token.shape[0] + token.low[col-token.x] - 1:
                return False
        return True

    def can_move_left(self, tower_tops):
        return

    def can_move_right(self, tower_tops):
        return

    def update_tower(self, token):
        for row in range(token.y, token.y + token.token.shape[0]):
            for col in range(token.x, token.x + token.token.shape[1]):
                self.tower[row, col] = token.token[row-token.y, col-token.x]
            # Update tower_tops as maximum index of 1 in each column
            for col in range(self.tower.shape[1]):
                # Find highest rownumber with 1 in this column
                self.tower_tops[col] = token.y + token.high[col]
        print("Tower tops updated ", self.tower_tops)
        return

    def simulate(self):
        tkn = 0
        while tkn < 5:
            token = Token(tkn % 5, np.max(self.tower_tops))
            token.vel(-1, 0)
            token.state = "moving"
            extra_rows = token.y - self.tower.shape[0]
            if extra_rows > 0:
                self.tower = np.vstack((self.tower, np.zeros((extra_rows, 7), dtype=int)))

            while token.state == "moving":
                if self.can_move_down(token):
                    token.state = "moving"
                else:
                    token.vel(0, 0)
                    token.state = "landed"

                token.move()

                if token.state == "landed":
                    self.update_tower(token)
                    tkn += 1


                print(self.tower)
        return


# Read input file
def read_input_file(fn):
    # Read single line input file and store in list
    with open(fn) as f:
        line = f.readline().rstrip()
        print("Length of input file: ", len(line))
    return 0


# Part 1
def part1(fn):
    read_input_file(fn)

    # tokens = []
    # for i in range(5):
    #     tokens.append(Token(i, 0))
    #     print(tokens[i])
    #     print(tokens[i].token.shape)
    #     print("Pos y: ", tokens[i].y)
    tower = Tower()
    tower.simulate()

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
    main(False)
