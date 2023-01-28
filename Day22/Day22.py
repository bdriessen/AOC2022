#
# Advent of code 2022: Day 20
#
# Author: Bart Driessen
# Start date: 2023-01-23
# Part 1 done:
# Part 2 done:
#
import re
import numpy as np
import time

# Read input file
def read_map_file(fn):
    with open(fn) as f:
        lines = f.readlines()
        # remove \n
        lines = [x.strip('\n') for x in lines]

        nrows = len(lines)
        ncols = 0
        for line in lines:
            ncols = max(ncols, len(line))
        map = np.empty((nrows, ncols,), dtype=str)
        map[:] = ' '
        for row in range(nrows):
            for col in range(len(lines[row])):
                map[row, col] = lines[row][col]

        # Create wrap around
        wrap_horizontal = np.empty((nrows, 2,), dtype=int)
        for row in range(nrows):
            for col in range(ncols):
                if map[row, col] == '#' or map[row, col] == '.':
                    wrap_horizontal[row, 1] = col
                    break
            for col in range(ncols-1, -1, -1):
                if map[row, col] == '#' or map[row, col] == '.':
                    wrap_horizontal[row, 0] = col
                    break
        wrap_vertical = np.empty((2, ncols,), dtype=int)
        for col in range(ncols):
            for row in range(nrows):
                if map[row, col] == '#' or map[row, col] == '.':
                    wrap_vertical[1, col] = row
                    break
            for row in range(nrows-1, -1, -1):
                if map[row, col] == '#' or map[row, col] == '.':
                    wrap_vertical[0, col] = row
                    break
        # for row in range(nrows):
        #     print(map[row, :])
        #
        # print(repr(wrap_horizontal))
        # print(repr(wrap_vertical))


    return map, wrap_vertical, wrap_horizontal

def read_traject_file(fn):
    traject = []
    with open(fn) as f:
        # read alternating numbers and letters and store in list
        line = f.readline()
        seq = re.split(r'(\d+)', line)
        seq = [x for x in seq if x]
        for i in range(0, len(seq), 2):
            traject.append((seq[i], seq[i+1]))

#    print(traject)
    return traject


# Part 1
def part1(mapfn, trajectfn):
    map, wrap_v, wrap_h = read_map_file(mapfn)
    traject = read_traject_file(trajectfn)

    idx_row = 0
    idx_col = 0
    for col in range(map.shape[1]):
        if map[idx_row, col] == '.' or map[idx_row, col] == '#':
            idx_col = col
            break
    print(idx_row, idx_col)

    ncols = map.shape[1]
    nrows = map.shape[0]



    dir = 0
    for step in traject:
        dist = int(step[0])
        print("Move", dist, "in direction", dir)
        for microstep in range(dist):
            # Move in direction until hit wall or enough steps
            # calculate next index
            if dir == 0: # right
                new_col = idx_col + 1
                if new_col >= ncols:
                    new_col = wrap_h[idx_row, 1]
                elif map[idx_row, new_col] == ' ': # wrap around
                    new_col = wrap_h[idx_row, 1]
                if map[idx_row, new_col] == '#':
                    new_col = idx_col
                    break
                idx_col = new_col
            elif dir == 1: # down
                new_row = idx_row + 1
                if new_row >= nrows:
                    new_row = wrap_v[1, idx_col]
                elif map[new_row, idx_col] == ' ':
                    new_row = wrap_v[1, idx_col]
                if map[new_row, idx_col] == '#':
                    new_row = idx_row
                    break
                idx_row = new_row
            elif dir == 2: # left
                new_col = idx_col - 1
                if new_col < 0:
                    new_col = wrap_h[idx_row, 0]
                elif map[idx_row, new_col] == ' ':
                    new_col = wrap_h[idx_row, 0]
                if map[idx_row, new_col] == '#':
                    new_col = idx_col
                    break
                idx_col = new_col
            elif dir == 3: # up
                new_row = idx_row - 1
                if new_row < 0:
                    new_row = wrap_v[0, idx_col]
                elif map[new_row, idx_col] == ' ':
                    new_row = wrap_v[0, idx_col]
                if map[new_row, idx_col] == '#':
                    new_row = idx_row
                    break
                idx_row = new_row
        # Turn
        rotation = step[1]
        if rotation == 'L':
            dir = (dir + 3) % 4
        elif rotation == 'R':
            dir = (dir + 1) % 4
        else:
            print("We should be ready now")
        print(idx_row, idx_col)


    return 1000*(idx_row+1) + 4*(idx_col+1) + dir

def over_the_edge(planes, neighbours, plane, row, col, dir):
    if dir == 0: # right
        new_plane = neighbours[plane][1][0]
        new_side = neighbours[plane][1][1]
    elif dir == 1: # down
        new_plane = neighbours[plane][2][0]
        new_side = neighbours[plane][2][1]
    elif dir == 2: # left
        new_plane = neighbours[plane][3][0]
        new_side = neighbours[plane][3][1]
    else: #      dir == 3: up
        new_plane = neighbours[plane][0][0]
        new_side = neighbours[plane][0][1]

    if dir == 3 and new_side == 3:
        new_row, new_col, new_dir = col, 0, 0
    elif dir == 0 and new_side == 3:
        new_row, new_col, new_dir = row, 0, 0
    elif dir == 2 and new_side == 3:
        new_row, new_col, new_dir = 49-row, 0, 0
    elif dir == 3 and new_side == 2:
        new_row, new_col, new_dir = 49, col, 3
    elif dir == 0 and new_side == 2:
        new_row, new_col, new_dir = 49, row, 3
    elif dir == 0 and new_side == 1:
        new_row, new_col, new_dir = 49-row, 49, 2
    elif dir == 1 and new_side == 1:
        new_row, new_col, new_dir = col, 49, 2
    elif dir == 2 and new_side == 1:
        new_row, new_col, new_dir = row, 49, 2
    elif dir == 1 and new_side == 0:
        new_row, new_col, new_dir = 0, col, 1
    else: #      dir == 2 and new_side == 0:
        new_row, new_col, new_dir = 0, row, 1

    return new_plane, new_row, new_col, new_dir




# Part 2
def part2(mapfn, trajectfn):
    map, wrap_v, wrap_h = read_map_file(mapfn)
    traject = read_traject_file(trajectfn)

    plane0 = np.zeros([50, 50], dtype=str)
    plane1 = np.zeros([50, 50], dtype=str)
    plane2 = np.zeros([50, 50], dtype=str)
    plane3 = np.zeros([50, 50], dtype=str)
    plane4 = np.zeros([50, 50], dtype=str)
    plane5 = np.zeros([50, 50], dtype=str)

    plane0[0:50, 0:50] = map[0:50, 50:100]
    plane1[0:50, 0:50] = map[0:50, 100:150]
    plane2[0:50, 0:50] = map[50:100, 50:100]
    plane3[0:50, 0:50] = map[100:150, 0:50]
    plane4[0:50, 0:50] = map[100:150, 50:100]
    plane5[0:50, 0:50] = map[150:200, 0:50]
    planes = [plane0, plane1, plane2, plane3, plane4, plane5]

    plane0_neighbours = [(5,3), (1,3), (2,0), (3,3)]  # Plane 0 connect to side 3 of plane5, side 3 of plane1 etc.
    plane1_neighbours = [(5,2), (4,1), (2,1), (0,1)]
    plane2_neighbours = [(0,2), (1,2), (4,0), (3,0)]
    plane3_neighbours = [(2,3), (4,3), (5,0), (0,3)]
    plane4_neighbours = [(2,2), (1,1), (5,1), (3,1)]
    plane5_neighbours = [(3,2), (4,2), (1,0), (0,0)]
    neighbours = [plane0_neighbours, plane1_neighbours, plane2_neighbours, plane3_neighbours, plane4_neighbours, plane5_neighbours]

    row = col = plane = 0  # Starting position
    dir = 0  # Starting direction
    for step in traject:
        dist = int(step[0])
        for microstep in range(dist):
            if dir == 0: # right
                new_plane = plane
                new_dir = dir
                new_col = col + 1
                new_row = row
                if new_col == 50:
                    new_plane, new_row, new_col, new_dir = over_the_edge(planes, neighbours, plane, row, col, dir)
                if planes[new_plane][new_row, new_col] == '#':
                    break
                row = new_row
                col = new_col
                plane = new_plane
                dir = new_dir
            elif dir == 1: # down
                new_plane = plane
                new_dir = dir
                new_col = col
                new_row = row + 1
                if new_row == 50:
                    new_plane, new_row, new_col, new_dir = over_the_edge(planes, neighbours, plane, row, col, dir)
                if planes[new_plane][new_row, new_col] == '#':
                    break
                row = new_row
                col = new_col
                plane = new_plane
                dir = new_dir
            elif dir == 2: # left
                new_plane = plane
                new_dir = dir
                new_col = col - 1
                new_row = row
                if new_col == -1:
                    new_plane, new_row, new_col, new_dir = over_the_edge(planes, neighbours, plane, row, col, dir)
                if planes[new_plane][new_row, new_col] == '#':
                    break
                row = new_row
                col = new_col
                plane = new_plane
                dir = new_dir
            else: # dir == 3: # up
                new_plane = plane
                new_dir = dir
                new_col = col
                new_row = row - 1
                if new_row == -1:
                    new_plane, new_row, new_col, new_dir = over_the_edge(planes, neighbours, plane, row, col, dir)
                if planes[new_plane][new_row, new_col] == '#':
                    break
                row = new_row
                col = new_col
                plane = new_plane
                dir = new_dir

        # Turn
        rotation = step[1]
        if rotation == 'L':
            dir = (dir + 3) % 4
        elif rotation == 'R':
            dir = (dir + 1) % 4
        else:
            print("We should be ready now")

        if plane == 0:
            idx_row = row
            idx_col = col+50
        elif plane == 1:
            idx_row = row
            idx_col = col+100
        elif plane == 2:
            idx_row = row+50
            idx_col = col+50
        elif plane == 3:
            idx_row = row+100
            idx_col = col
        elif plane == 4:
            idx_row = row+100
            idx_col = col+50
        else: # plane == 5:
            idx_row = row+150
            idx_col = col

    return 1000*(idx_row+1) + 4*(idx_col+1) + dir





def main():
    real = True
    part = 2


    # Start timer
    tic = time.perf_counter()

    if part == 1:
        if real:
            mapfn = "Day22/input_map.txt"
            trajectfn = "Day22/input_traject.txt"
        else:
            mapfn = "Day22/input_test_map.txt"
            trajectfn = "Day22/input_test_traject.txt"
        res1 = part1(mapfn, trajectfn)
        print("Part 1: ", res1)
    else:
        if real:
            mapfn = "Day22/input_map.txt"
            trajectfn = "Day22/input_traject.txt"
        else:
            mapfn = "Day22/input_test_map.txt"
            trajectfn = "Day22/input_test_traject.txt"
        res2 = part2(mapfn, trajectfn)
        print("Part 2: ", res2)

    # Stop timer
    toc = time.perf_counter()
    print(f"Time elapsed: {toc - tic:0.4f} seconds")
    return
