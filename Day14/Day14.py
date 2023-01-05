#
# Advent of code 2022: Day 14
#
# Author: Bart Driessen
# Date: 2022-12-29
#

import numpy as np

class Cave:
    def __init__(self, data, part):
        if part == 'A':
            self.data = data
            # for all lines in the data, find the maximum x and y coordinates
            self.max_x = 0
            self.max_y = 0
            self.min_x = 10000000000
            self.min_y = 10000000000
            self.state = 'running' #running, stopped
            self.part = 'A'

            for line in self.data:
                for coord in line:
                    if coord[0] > self.max_x:
                        self.max_x = coord[0]
                    if coord[0] < self.min_x:
                        self.min_x = coord[0]
                    if coord[1] > self.max_y:
                        self.max_y = coord[1]
                    if coord[1] < self.min_y:
                        self.min_y = coord[1]

            self.max_x += 2
            self.min_x -= 2
#            print("Cave dimensions: ", self.min_x, self.max_x, self.min_y, self.max_y)
#            print("Cave size: ", self.max_x-self.min_x+1, self.max_y+1)
            self.cave = np.zeros((self.max_y + 2, self.max_x - self.min_x + 1), dtype=int)

            return
        if part == 'B':
            self.data = data
            # for all lines in the data, find the maximum x and y coordinates
            self.max_x = 0
            self.max_y = 0
            self.min_x = 10000000000
            self.min_y = 10000000000
            self.state = 'running'  # running, stopped
            self.part = 'B'

            for line in self.data:
                for coord in line:
                    if coord[0] > self.max_x:
                        self.max_x = coord[0]
                    if coord[0] < self.min_x:
                        self.min_x = coord[0]
                    if coord[1] > self.max_y:
                        self.max_y = coord[1]
                    if coord[1] < self.min_y:
                        self.min_y = coord[1]

#            print("Cave dimensions part B: ", self.min_x, self.max_x, self.min_y, self.max_y)
            if self.max_x < 500 + self.max_y + 10:
                self.max_x = 500 + self.max_y + 10
            if self.min_x > 500 - (self.max_y + 10):
                self.min_x = 500 - (self.max_y + 10)

#            print("Cave dimensions: ", self.min_x, self.max_x, self.min_y, self.max_y)
#            print("Cave size: ", self.max_x-self.min_x+1, self.max_y+1)
            self.cave = np.zeros((self.max_y + 2 + 10, self.max_x - self.min_x + 1), dtype=int)
            self.cave[self.max_y+2, :] = 1
            return


    def parse_input_data(self, data):

        for line in data:

            lnght = len(line)-1
            for i in range(lnght):

                dx = line[i+1][0] - line[i][0]
                dy = line[i+1][1] - line[i][1]
                if dx == 0:
                    # vertical line
                    y0 = min(line[i][1], line[i+1][1])
                    y1 = max(line[i][1], line[i+1][1])
                    x = line[i][0]-self.min_x

                    self.cave[y0:y1 + 1, x] = 1
                if dy == 0:
                    x0 = min(line[i][0], line[i+1][0])-self.min_x
                    x1 = max(line[i][0], line[i+1][0])-self.min_x
                    y = line[i][1]
                    self.cave[y, x0:x1 + 1] = 1

        return

    def print_cave(self):
        print("Cave dimensions: ", self.min_x, self.max_x, self.min_y, self.max_y)
        print(self.cave)
        return

    def simulate(self):
        s = Sand(0)
        print(s)
        snr = 0
        while self.state == 'running':
            while s.state  ==  'falling':
                # Determine sand direction
                if self.cave[s.y+1, s.x-self.min_x] == 0:
                    s.set_vel(1, 0)
                elif self.cave[s.y+1, s.x-1-self.min_x] == 0:
                    s.set_vel(1, -1)
                elif self.cave[s.y+1, s.x+1-self.min_x] == 0:
                    s.set_vel(1, 1)
                else:
                    s.set_vel(0, 0)
                    s.state = 'stationary'
                    self.cave[s.y, s.x-self.min_x] = 2
                    break
                if self.cave[s.y, s.x - self.min_x] == 3:
                    self.cave[s.y, s.x - self.min_x] = 0
                s.move()
                if self.part == 'A':
                    if s.y <= self.max_y:
                        self.cave[s.y, s.x-self.min_x] = 3
#                    print("Cave state:")
#                    print(self.cave)
                    if s.x > self.max_x or s.x < self.min_x:
                        self.state = 'stopped'
                        break
                    if s.y > self.max_y:
                        self.state = 'gone'
                        break
            snr += 1
            s = Sand(snr)
            if self.cave[0, 500-self.min_x] != 0:
                self.state = 'full'
#            print(self.state)
#            if (snr % 1000) == 0:  print(s)
#        print(self.cave)
        return snr - 1


class Sand:
    def __init__(self, id):
        self.x = 500
        self.y = 0
        self.id = id
        self.vel_x = 0
        self.vel_y = 1
        self.state = "falling" # falling, stationary


    def __str__(self):
        return "Sand: x = " + str(self.x) + ", y = " + str(self.y) + ", vel_x = " + str(self.vel_x) + ", vel_y = " + str(self.vel_y) + ", state = " + str(self.state) + "id = " + str(self.id)

    def __repr__(self):
        return "Sand: x = " + str(self.x) + ", y = " + str(self.y) + ", vel_x = " + str(self.vel_x) + ", vel_y = " + str(self.vel_y) + ", state = " + str(self.state) + "id = " + str(self.id)

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        return

    def set_state(self, state):
        if state == 'stationary':
            self.set_vel(0, 0)
        self.state = state
        return

    def set_vel(self, vel_y, vel_x):
        self.vel_x = vel_x
        self.vel_y = vel_y
        return


# Read input file
def read_input_file(fn):
    result = []
    with open(fn, 'r') as f:
        # For each line in the file, read it as a list of strings and remove the newline character
        for line in f:
            coords = []
            # Read line
            # convert line to list of strings
            line = line.split()
            # remove newline character and the element '->" from the list
            line = [x.strip() for x in line if x != '->']
            # convert each string element to a list of 2 integers
            for s in line:
                # split s in 2 integers with delimiter ','  and convert to integers
                coord = s.split(',')
                coord = [int(x) for x in coord]
                coords.append(coord)


            # add the list of integers to the list of lists
            result.append(coords)

    return result




# Part 1
def part1(fn):
    data = read_input_file(fn)
    cave = Cave(data, 'A')
    cave.parse_input_data(data)
#    cave.print_cave()
    snr = cave.simulate()
    print("Number of stationary sand grains: ", snr)
    return snr

# Part 2
def part2(fn):
    data = read_input_file(fn)
    caveB = Cave(data, 'B')
    caveB.parse_input_data(data)
#    caveB.print_cave()
    snr = caveB.simulate()
    print("Number of stationary sand grains: ", snr + 1)
    return snr+1

def main(realinput):
    if realinput:
        fn = 'input.txt'
    else:
        fn = 'testinput.txt'

    part1(fn)
    part2(fn)

if __name__ == "__main__":

    testrun = True
    testrun = False

    if testrun:
        res1 = part1("Day14/testinput.txt")
        print("Part 1: ", res1)
        res2 = part2("Day14/testinput.txt")
        print("Part 2: ", res2)
    else:
        res1 = part1("Dainput.txt")
        print("Part 1: ", res1)
        res2 = part2("input.txt")
        print("Part 2: ", res2)


