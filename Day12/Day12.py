#
# Advent of code Day 12
#
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def read_input(fn):
    with open(fn) as f:
        # Read lines and store each line in a list of characters in a numpy array
        input = np.array([list(line.strip()) for line in f])
    return input

def parse_input(input, G):
    # For each line in the input
    # Store coordinates of the input where characeter equals 'S'
    start = np.argwhere(input == 'S')
    input[start[0][0], start[0][1]] = 'a'
#    print("Start: ", start)
#    nodename = "({},{})".format(start[0][0], start[0][1])
#    G.add_node(nodename)

    # Store coordinates of the input where characeter equals 'E'
    end = np.argwhere(input == 'E')
    input[end[0][0], end[0][1]] = 'z'
#    print("End: ", end)
#    nodename = "({},{})".format(end[0][0], end[0][1])
#    G.add_node(nodename, node_color='tab:red')

    nrows, ncols = input.shape
#    print(input)
    for i in range(nrows):
        # For each character in the line
        for j in range(ncols):
            nodename = "({},{})".format(i,j)
            G.add_node(nodename)
    # Now create edges between nodes: left to right
    for i in range(nrows):
        for j in range(ncols-1):
            node = "({},{})".format(i,j)
            nextnode = "({},{})".format(i,j+1)
            if ord(input[i,j+1])-1 <= ord(input[i,j]):
                G.add_edge(node, nextnode)

    # Now create edges between nodes: right to left
    for i in range(nrows):
        for j in range(ncols-1, 0, -1):
            node = "({},{})".format(i,j)
            nextnode = "({},{})".format(i,j-1)
            if ord(input[i,j-1])-1 <= ord(input[i,j]):
                G.add_edge(node, nextnode)

    # Now create edges between nodes: top to bottom
    for col in range(ncols):
        for row in range(nrows-1):
            node = "({},{})".format(row,col)
            nextnode = "({},{})".format(row+1,col)
            if ord(input[row+1,col])-1 <= ord(input[row,col]):
                G.add_edge(node, nextnode)

    # Now create edges between nodes: bottom to top
    for col in range(ncols):
        for row in range(nrows-1, 0, -1):
            node = "({},{})".format(row,col)
            nextnode = "({},{})".format(row-1,col)
            if ord(input[row-1,col])-1 <= ord(input[row,col]):
                G.add_edge(node, nextnode)

    return G, start, end

def part1(fn):
    input = read_input(fn)
    G = nx.DiGraph()
    G, start, end = parse_input(input, G)
#    nx.draw(G, with_labels=True)
#    plt.show()
    source = "({},{})".format(start[0][0], start[0][1])
    target = "({},{})".format(end[0][0], end[0][1])
#    print("From: ", source, " to: ", target)
    sp = nx.shortest_path(G, source, target)
#    print("Shortest path: ", sp)
    print("Part 1: Length of shortest path: ", len(sp)-1)


    return 0

def part2(fn):
    input = read_input(fn)
    G = nx.DiGraph()
    G, start, end = parse_input(input, G)
    #    nx.draw(G, with_labels=True)
    #    plt.show()

    # Find index of all 'a' or 'S' in the input
    alocations = np.argwhere(input == 'a')
    len_sps = []
    for a in alocations:
        source = "({},{})".format(a[0], a[1])
        target = "({},{})".format(end[0][0], end[0][1])
#        print("From: ", source, " to: ", target)
        if nx.has_path(G, source, target):
            sp = nx.shortest_path(G, source, target)
#            print("Shortest path length investigate: ", len(sp)-1)
            len_sps.append(len(sp)-1)
    len_sps.sort()
    print("Part 2: Length of shortest path: ", len_sps[0])

    return 0


if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")

