#
# Advent of code 2022: Day 18
#
# Author: Bart Driessen
# Date: 2022-01-09
#


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
        return "Voxel: x: " + str(self.x) + ", y: " + str(self.y) + ", z: " + str(self.z) + ", active: " + str(
            self.active)


# Read input file
def read_input_file(fn):
    # Read single line input file and store in list
    coords = []
    with open(fn, "r") as f:
        lines = f.readlines()

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

def distance(v1, v2):
    return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1]) + abs(v1[2] - v2[2])


def touching(v, coords):
    for dx, dy, dz in [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]:
        if [v[0] + dx, v[1] + dy, v[2] + dz] in coords:
            return True
    return False

def find_air(cubes):
    # Find min and max x, y and z
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0
    for cube in cubes:
        if cube[0] < min_x:
            min_x = cube[0]
        if cube[0] > max_x:
            max_x = cube[0]
        if cube[1] < min_y:
            min_y = cube[1]
        if cube[1] > max_y:
            max_y = cube[1]
        if cube[2] < min_z:
            min_z = cube[2]
        if cube[2] > max_z:
            max_z = cube[2]
    min_x -= 1
    min_y -= 1
    min_z -= 1

    max_x += 1
    max_y += 1
    max_z += 1

    # Find all coordinates that are not cubes
    coords_air_outside = [[0, 0, 0]]

    new_air = True
    while new_air:
        new_air = False
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                for z in range(min_z, max_z):
                    if touching([x, y, z], coords_air_outside) and not [x, y, z] in cubes and not [x, y, z] in coords_air_outside:
                        coords_air_outside.append([x, y, z])
                        new_air = True

    coords_air_inside = []
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            for z in range(min_z, max_z):
                if not [x, y, z] in coords_air_outside and not [x, y, z] in cubes:
                    coords_air_inside.append([x, y, z])

    return coords_air_outside, coords_air_inside

# Part 1
def part1(fn):
    coords_cubes = read_input_file(fn)
    voxels = parse_input(coords_cubes)


    nr_of_open_sides = 0
    for voxel in voxels:
        nr_of_open_sides += 6 - len(voxel.neighbors)
    print("Number of open sides: ", nr_of_open_sides)

    return nr_of_open_sides


# Part 2
def part2(fn):
    coords_cubes = read_input_file(fn)


    coords_air_outside, coords_air_inside = find_air(coords_cubes)
    print("Coords air outside: ", coords_air_outside)
    print("Coords air inside: ", coords_air_inside)

    # Merge inside coords with cube coords
    coords_cubes = coords_cubes + coords_air_inside

    voxels = parse_input(coords_cubes)


    nr_of_open_sides = 0
    for voxel in voxels:
        nr_of_open_sides += 6 - len(voxel.neighbors)
    print("Number of open sides: ", nr_of_open_sides)
    return 0


def main(realinput):
    if realinput:
        fn = "Day18/input.txt"
    else:
        fn = "Day18/testinput.txt"

    res1 = part1(fn)
    print("Part 1: ", res1)
    res2 = part2(fn)
    print("Part 2: ", res2)
    return


if __name__ == "__main__":
    #    main(True)
    #    main(False)
    pass
