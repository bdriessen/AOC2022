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
    token2 = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])
    token3 = np.array([[1], [1], [1], [1]])
    token4 = np.array([[1, 1], [1, 1]])
    def __init__(self, nr, top):
        if nr == 0:
            self.token = self.token0
        elif nr == 1:
            self.token = self.token1
        elif nr == 2:
            self.token = self.token2
        elif nr == 3:
            self.token = self.token3
        elif nr == 4:
            self.token = self.token4
        self.x = 2
        self.y = top + 3 + self.token.shape[0]


        self.state = "idle" # idle, moving, landed
        return

    def vel(self, Vy, Vx):
        self.Vx = Vx
        self.Vy = Vy
        return

    def move(self):
        self.y += self.Vy
        self.x += self.Vx
        return

    def can_move_down(self, tower_tops):

        # Onderstaande code is niet correct
        tower_mat = np.array(tower[self.y + self.token.shape[0] - 1, self.x:self.x + self.token.shape[1]])
        if tower_mat * self.token[-1, :] != 0:
            return False

        return True

    def can_move_left(self, tower_tops):

        return True


    def can_move_right(self, tower_tops):
        return

    def __str__(self):
        return str(self.token)



class Tower:
    def __init__(self, name, weight, children):
        self.height = 0

    def __str__(self):
        return "Tower height: " + str(self.height)




# Read input file
def read_input_file(fn):
    # Read single line input file and store in list
    with open(fn) as f:
        line = f.readline().rstrip()
        print("Length of input file: ", len(line))
    return 0

# Parse input file
def parse_input_file(input_file):
    return


# Part 1
def part1(fn):
    res = read_input_file(fn)


    tokens = []
    for i in range(5):
        tokens.append(Token(i, 0))
        print(tokens[i])
        print(tokens[i].token.shape)
        print("Pos y: ", tokens[i].y)

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

    testrun = True
#    testrun = False

    if testrun:
        res1 = part1("testinput.txt")
#        res2 = part2("testinput.txt")
#        print("Part 2: ", res2)
    else:
        res1 = part1("input.txt")
        print("Part 1: ", res1)
#        res2 = part2("input.txt")
#        print("Part 2: ", res2)


