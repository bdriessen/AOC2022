#
# Advent of code 2022: Day 15
#
# Author: Bart Driessen
# Date: 2023-01-01
#

import numpy as np
import re
import intervaltree

# Read input file
def read_input_file(fn):
    numlist = []

    # Read input file
    with open(fn, 'r') as f:
        # Read line of input file and store integers that follow the '=' character in a list
        for line in f:
            # Split line on '=' or ' ' characters

            tokens = re.split('=| |,|:|\n', line)
            # Remove empty strings from list
            tokens = list(filter(None, tokens))

            nums = []
            for token in tokens:

                if token[0] == '-':
                    if token[1:].isdigit():
                        nums.append(-int(token[1:]))
                else:
                    if token[:].isdigit():
                        nums.append(int(token[:]))

            numlist.append(nums)
#        for nums in numlist: print(nums)


    return numlist



class World:
    def __init__(self, data):
        self.data = np.array(data)
#        print(self.data)
        self.sensors = self.data[:,0:2]
        self.beacons = self.data[:,2:4]
#        print("Sensors:\n", self.sensors)
#        print("Beacons:\n", self.beacons)
        self.beacon_ranges = []
        for i in range(len(self.beacons)):

            self.beacon_ranges.append(World.distance(self.sensors[i], self.beacons[i]))
#        print("Ranges:\n",self.beacon_ranges)
        self.intersections = []
        return

    def analyze_row(self, row):
        self.intersections = []
        for i in range(len(self.sensors)):
            # Check which segement of row is in range of sensor i
            seg = World.row_intersection(row, self.sensors[i], self.beacon_ranges[i])
            if seg is not None:
                self.intersections.append(seg)
#        print("Intersections:\n", self.intersections)

        # Create interval tree
        itree = intervaltree.IntervalTree()
        for seg in self.intersections:
            itree.addi(seg[0], seg[1])
        # Merge overlapping intervals
        itree.merge_overlaps()
#        print("Interval tree:\n", itree)

        return itree

    def row_intersection(row, sensor, radius):
        dist = abs(row - sensor[1])
        if dist > radius:
            return None
        else:
            return (sensor[0] - (radius - dist), sensor[0] + (radius - dist) + 1)

    def distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


# Part 1
def part1(fn, row):
    data = read_input_file(fn)
    world = World(data)
    itree = world.analyze_row(row)
    interval = []
    for interval in itree:
        print(interval.end-interval.begin-1)

    return interval.end-interval.begin-1

# Part 2
def part2(fn, maxrow):
    data = read_input_file(fn)
    world = World(data)
#    print("Max tree:\n", tree_max)
    tree_trunc = intervaltree.IntervalTree()

#    for row in range(maxrow): # This is for the entire grid. Takes too long. Found solution earlier, so focus on that.
    for row in range(3041245, 3041247):
        tree_trunc.clear()
        add_interval = False
        itree = world.analyze_row(row)
#        print("Original tree in row ", row, " : ", itree)

        if not itree.is_empty():
            for interval in itree:
                add_interval = False
                if interval.begin < 0 and interval.end < 0:
                    add_interval = False
                elif interval.begin < 0 and interval.end >= maxrow:
                    add_interval = True
                    ib = 0
                    ie = maxrow + 1
                elif interval.begin < 0 and interval.end > 0:
                    add_interval = True
                    ib = 0
                    ie = interval.end
                elif interval.begin >= 0 and interval.end <= maxrow:
                    add_interval = True
                    ib = interval.begin
                    ie = interval.end
                elif interval.begin >= 0 and interval.end > maxrow:
                    add_interval = True
                    ib = interval.begin
                    ie = maxrow + 1
                elif interval.begin > maxrow:
                    add_interval = False
                if add_interval:
                    tree_trunc.addi(ib, ie)
            tree_trunc.merge_overlaps(strict=False)
#            print("Truncated tree at row: ", row, " : ", tree_trunc)
#            print(len(tree_trunc))
            if len(tree_trunc) > 1:

                items = tree_trunc.items()
                firstitem = True
                x = 0
                for item in items:
                    if firstitem: x = item.end
                    firstitem = False
                    print(x)
                return [row, x, x*4000000 + row]

            if row%10000 == 0:
                print("Row: ", row)


    return 0

if __name__ == "__main__":

    testrun = True
    testrun = False

    if testrun:
#        res1 = part1("testinput.txt", 10)
#        print("Part 1: ", res1)
        res2 = part2("testinput.txt", 20)
        print("Part 2: ", res2)
    else:
#        res1 = part1("input.txt", 2000000)
#        print("Part 1: ", res1)
        res2 = part2("input.txt", 4000000)
        print("Part 2: ", res2)


