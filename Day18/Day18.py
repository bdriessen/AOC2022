#
# Advent of code 2022: Day 18
#
# Author: Bart Driessen
# Date: 2022-01-09
#

import numpy as np

class Voxel:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.active = False
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_active_neighbors(self):
        active_neighbors = 0
        for neighbor in self.neighbors:
            if neighbor.active:
                active_neighbors += 1
        return active_neighbors

    def set_active(self, active):
        self.active = active

    def __str__(self):
        return "Voxel: x: " + str(self.x) + ", y: " + str(self.y) + ", z: " + str(self.z) + ", active: " + str(self.active)

# Read input file
def read_input_file(fn):
    # Read single line input file and store in list
    coords = []
    with open(fn, "r") as f:
        lines = f.readlines()

    voxels = []
    for line in lines:
        # Seperate line into list of integer coordinates
        coords.append([int(x) for x in line.split(",")])

    return coords

def parse_input(coords):
    voxels = []
    print(coords)
    for coord in coords:
        voxel = Voxel(coord[0], coord[1], coord[2])
        voxels.append(voxel)
    for coord in coords:
        voxel = Voxel(coord[0], coord[1], coord[2])
        # Check if voxel has neighbors
        if [coord[0] - 1, coord[1], coord[2]] in coords:
            neighbor_voxel = voxels[coords.index([coord[0] - 1, coord[1], coord[2]])]
            voxel.add_neighbor(neighbor_voxel)
            neighbor_voxel.add_neighbor(voxel)
        if [coord[0] + 1, coord[1], coord[2]] in coords:
            neighbor_voxel = voxels[coords.index([coord[0] + 1, coord[1], coord[2]])]
            voxel.add_neighbor(neighbor_voxel)
            neighbor_voxel.add_neighbor(voxel)
        if [coord[0], coord[1] - 1, coord[2]] in coords:
            neighbor_voxel = voxels[coords.index([coord[0], coord[1] - 1, coord[2]])]
            voxel.add_neighbor(neighbor_voxel)
            neighbor_voxel.add_neighbor(voxel)
        if [coord[0], coord[1] + 1, coord[2]] in coords:
            neighbor_voxel = voxels[coords.index([coord[0], coord[1] + 1, coord[2]])]
            voxel.add_neighbor(neighbor_voxel)
            neighbor_voxel.add_neighbor(voxel)
        if [coord[0], coord[1], coord[2] - 1] in coords:
            neighbor_voxel = voxels[coords.index([coord[0], coord[1], coord[2] - 1])]
            voxel.add_neighbor(neighbor_voxel)
            neighbor_voxel.add_neighbor(voxel)
        if [coord[0], coord[1], coord[2] + 1] in coords:
            neighbor_voxel = voxels[coords.index([coord[0], coord[1], coord[2] + 1])]
            voxel.add_neighbor(neighbor_voxel)
            neighbor_voxel.add_neighbor(voxel)

    return voxels


# Part 1
def part1(fn):
    coords = read_input_file(fn)
    voxels = parse_input(coords)

    nr_of_open_sides = 0
    for voxel in voxels:
        nr_of_open_sides += 6 - len(voxel.neighbors)
    print("Number of open sides: ", nr_of_open_sides)

    return nr_of_open_sides



# Part 2
def part2(fn):
    return 0
def main(realinput):
    if realinput:
        fn = "Day18/input.txt"
    else:
        fn = "Day18/testinput.txt"

    res1 = part1(fn)
    print("Part 1: ", res1)
#    res2 = part2(fn)
#    print("Part 2: ", res2)
    return


if __name__ == "__main__":
    #    main(True)
    #    main(False)
    pass
