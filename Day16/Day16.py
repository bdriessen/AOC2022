#
# Advent of code 2022: Day 16
#
# Author: Bart Driessen
# Date: 2022-01-10
#

import re
import networkx as nx
import matplotlib.pyplot as plt
import time

global BEST_PRESSURE_RELEASE, BEST_SOLUTION

# Read input file
def read_input_file(fn):
    # for each line in the file
    with open(fn, "r") as f:
        # read lines and remove newline characters
        lines = [line.rstrip() for line in f]

    nodes = []
    for line in lines:
        # Seperate line into list of integer coordinates
        tokens = re.split("[ ,=;]", line)
        # Remove empty strings
        tokens = list(filter(None, tokens))
        node = {'name': tokens[1], 'rate': int(tokens[5]), 'to': tokens[10:]}
        nodes.append(node)
    #    for node in nodes:
    #        print(node)

    return nodes


def parse_input():
    return 0


def clean_graph(graph):
    # remove all nodes with 2 negihbors and a rate of 0
    newgraph = graph.copy()
    #    print("Now checking: ", list(graph.nodes(data=True)))
    nodes_to_remove = []
    for node in graph.nodes():
        if graph.nodes[node]["rate"] == 0 and len(list(graph.neighbors(node))) == 2:
            nodes_to_remove.append(node)
    #            print("Found node to remove: ", node)

    #    print("Nodes to remove: ", nodes_to_remove)
    for node in nodes_to_remove:
        neighbors = list(newgraph.neighbors(node))
        newweight = newgraph.get_edge_data(neighbors[0], node)['weight'] + newgraph.get_edge_data(neighbors[1], node)[
            'weight']
        newgraph.add_edge(neighbors[0], neighbors[1], weight=newweight)
        newgraph.remove_node(node)
    return newgraph


def score(solution, sh_pth_length, graph):
    time = 0
    total_release = 0
    rate = 0
    last_node = solution[0]
    for node in solution[1:]:
        dtime = sh_pth_length[last_node][node]
        total_release += dtime * rate
        time += dtime

        # Open valve
        time += 1
        total_release += rate
        rate += graph.nodes[node]['rate']
        last_node = node

    # If solution complete, add release until end of time
    if len(solution) == len(graph.nodes()):
        # Solution is complete, calculate pressure release in remaining time
        dtime = 30 - time
        time += dtime
        total_release += dtime * rate
    return total_release, rate, time


def solve(state, solution):

    global BEST_PRESSURE_RELEASE, BEST_SOLUTION
    graph = state["graph"]
    sh_pth_length = state["sh_pth_length"]
    maxrate = state["maxrate"]
    pressure_release = state["pressure_release"]
    best_pressure_release = state["best_pressure_release"]

    nodes = list(graph.nodes())

#    if pressure_release > BEST_PRESSURE_RELEASE and len(solution) == len(graph.nodes()):
    if pressure_release > BEST_PRESSURE_RELEASE:
        BEST_PRESSURE_RELEASE = pressure_release
        BEST_SOLUTION = solution

        print("New best solution found: ", solution, "with pressure release: ", pressure_release)
        return

    # If solution not complete, extend solution
    solution_new = solution.copy()

    # Try all possibilities for next node
    for node in [n for n in nodes if n not in solution]:
        # Try to add node to solution
        # Calculate path to next node
        solution_new.append(node)

        new_pressure_release, new_rate, new_time = score(solution_new, sh_pth_length, graph)

        if new_time > 30:
            # Solution is not possible
            solution_new.pop()
            continue

        state_new = {'graph': graph, 'sh_pth_length': sh_pth_length,
                     'time': new_time, 'rate': new_rate, 'maxrate': maxrate,
                     'pressure_release': new_pressure_release,
                     'best_pressure_release': best_pressure_release}

        solve(state_new, solution_new)

        # Remove node from solution
        solution_new.pop()

    return


# Part 1
def part1(fn):

    VISU = False
    global BEST_PRESSURE_RELEASE, BEST_SOLUTION
    nodes = read_input_file(fn)
    G = nx.Graph()

    for node in nodes:
        G.add_node(node['name'], rate=node['rate'])
        for to in node['to']:
            G.add_edge(node['name'], to, weight=1)

    cleanG = clean_graph(G)

    # Find the sum of the rates of all nodes
    maxrate = 0
    for node in cleanG.nodes():
        maxrate += cleanG.nodes[node]['rate']

    # Find all shortest paths in the graph
    tic = time.perf_counter()
    shortest_paths = nx.shortest_path(cleanG, weight='weight')
    toc = time.perf_counter()
    print(f"Finding all shortest paths took {toc - tic:0.4f} seconds")

    # Find all travel times for all shortest paths
    tic = time.perf_counter()
    shortest_path_length = dict(nx.shortest_path_length(cleanG, weight='weight'))
    toc = time.perf_counter()
    print(f"Finding all shortest path lengths took {toc - tic:0.4f} seconds")

    state = {'graph': cleanG, 'sh_pth_length': shortest_path_length, 'time': 0, 'rate': 0, 'maxrate': maxrate,
             'pressure_release': 0, 'best_pressure_release': 0}

    BEST_PRESSURE_RELEASE = 0
    solution = ['AA']
    tic = time.perf_counter()
    solve(state, solution)
    toc = time.perf_counter()
    print(f"Found best solution in {toc - tic:0.4f} seconds")

    if (VISU):
        pos = nx.spring_layout(cleanG)
        nx.draw(cleanG, pos, with_labels=False)
        node_lable = {}
        for node in cleanG.nodes():
            node_lable[node] = str(node) + ": " + str(cleanG.nodes[node]['rate'])

        nx.draw_networkx_labels(cleanG, pos, labels=node_lable, font_size=8)

        edge_labels = nx.get_edge_attributes(cleanG, 'weight')
        nx.draw_networkx_edge_labels(cleanG, pos, edge_labels=edge_labels)

        plt.show()

    return 0


# Part 2
def part2(fn):
    return 0


def main(realinput):
    if realinput:
        fn = "Day16/input.txt"
    else:
        fn = "Day16/testinput.txt"

    res1 = part1(fn)
    print("Part 1: ", res1)
    #    res2 = part2(fn)
    #    print("Part 2: ", res2)
    return


if __name__ == "__main__":
    #    main(True)
    #    main(False)
    pass
