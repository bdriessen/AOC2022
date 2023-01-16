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
from itertools import combinations

global BEST_PRESSURE_RELEASE, BEST_SOLUTION

# Read input file
def read_input_file(fn):
    # for each line in the file
    with open(fn, "r") as f:
        # read lines and remove newline characters
        lines = [line.rstrip() for line in f]

    nodes = []
    for line in lines:
        # Separate line into list of integer coordinates
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
        if graph.nodes[node]["rate"] == 0 and len(list(graph.neighbors(node))) == 2 and not node =='AA':
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

def solve(state, solution):

    global BEST_PRESSURE_RELEASE, BEST_SOLUTION, MAX_TIME
    graph = state["graph"]
    sh_pth_length = state["sh_pth_length"]
    maxrate = state["maxrate"]

    nodes = list(graph.nodes())

    # Try all possibilities for next node
    for node in [n for n in nodes if n not in solution]:
        # Try to add node to solution
        # Calculate path to next node
        solution_new = solution.copy()
        state_new = state.copy()

        solution_new.append(node)

        state_new["pressure_release"] += (sh_pth_length[solution[-1]][node] + 1) * state["rate"]
        state_new["rate"] += graph.nodes[node]["rate"]
        state_new["time"] += sh_pth_length[solution[-1]][node] + 1

        if state_new["time"] > MAX_TIME or \
                state_new["pressure_release"] + maxrate * (MAX_TIME - state_new["time"]) < BEST_PRESSURE_RELEASE:
            # Solution is not possible
            continue

        if len(solution_new) == len(graph.nodes()):
            # Solution is complete, calculate pressure release in remaining time
            state_new["pressure_release"] += (MAX_TIME - state_new["time"]) * state_new["rate"]
            state_new["time"] = MAX_TIME

        if state_new["pressure_release"] > BEST_PRESSURE_RELEASE:
            BEST_PRESSURE_RELEASE = state_new["pressure_release"]
            BEST_SOLUTION = solution_new
#            print("New best solution found: ", BEST_SOLUTION, "with pressure release: ", BEST_PRESSURE_RELEASE)

        solve(state_new, solution_new)

    return

def exclude_nodes(graph, nodes):
    newgraph = graph.copy()
    for node in nodes:
        newgraph.nodes[node]["rate"] = 0
#    newgraph = clean_graph(newgraph)
    return newgraph

def divide_set(nodes):
    elements = len(nodes)
    hu = []
    ol = []

    for i in range(1, elements//2 + 1):
        for subset in combinations(nodes, i):
            hu.append(list(subset))

    for subset in hu:
        subset2 = [n for n in nodes if n not in subset]
        ol.append(subset2)
#        print(subset, subset2)

    return ol, hu


def find_best_solution(graph):
    global BEST_PRESSURE_RELEASE, BEST_SOLUTION

    BEST_PRESSURE_RELEASE = 0
    BEST_SOLUTION = []

    # Find the sum of the rates of all nodes
    maxrate = 0
    for node in graph.nodes():
        maxrate += graph.nodes[node]['rate']

    # Find all shortest paths in the graph
    shortest_paths = nx.shortest_path(graph, weight='weight')

    # Find all travel times for all shortest paths
    shortest_path_length = dict(nx.shortest_path_length(graph, weight='weight'))

    state = {'graph': graph, 'sh_pth_length': shortest_path_length, 'time': 0, 'rate': 0, 'maxrate': maxrate,
             'pressure_release': 0, 'best_pressure_release': 0}

    BEST_PRESSURE_RELEASE = 0
    solution = ['AA']
    solve(state, solution)

    return BEST_PRESSURE_RELEASE, BEST_SOLUTION

def show_graph(graph):
    # Create new matplotlib figure
    fig = plt.figure()
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=False)
    node_lable = {}
    for node in graph.nodes():
        node_lable[node] = str(node) + ": " + str(graph.nodes[node]['rate'])

    nx.draw_networkx_labels(graph, pos, labels=node_lable, font_size=8)

    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.show()
    return


# Part 1
def part1(fn):

    VISU = True
    global BEST_PRESSURE_RELEASE, BEST_SOLUTION, MAX_TIME
    MAX_TIME = 30
    nodes = read_input_file(fn)
    G = nx.Graph()

    for node in nodes:
        G.add_node(node['name'], rate=node['rate'])
        for to in node['to']:
            G.add_edge(node['name'], to, weight=1)

    cleanG = clean_graph(G)

    bpr, bs = find_best_solution(cleanG)

    if (VISU):
        show_graph(cleanG)
    return BEST_PRESSURE_RELEASE


# Part 2
def part2(fn):
    VISU = False
    global BEST_PRESSURE_RELEASE, BEST_SOLUTION, MAX_TIME
    MAX_TIME = 26
    nodes = read_input_file(fn)
    G = nx.Graph()

    for node in nodes:
        G.add_node(node['name'], rate=node['rate'])
        for to in node['to']:
            G.add_edge(node['name'], to, weight=1)

    cleanG = clean_graph(G)

    nodes_to_divide = list(cleanG)
    nodes_to_divide.remove('AA')
#    print(nodes_to_divide)
    nodes_to_divide.sort()

    # divide the nodes in two groups: ol and hu
    ol, hu = divide_set(nodes_to_divide)


#    for i in range(0, len(ol)):
#        print(len(ol[i]), len(hu[i]), len(ol[i]) + len(hu[i]))
#        print(ol[i], hu[i])

    # find the best solution for each group
    best_ol = 0
    best_hu = 0
    best_ol_solution = []
    best_hu_solution = []
    best_total_pressure_release = 0
    tic = time.perf_counter()
    for i in range(len(ol)):
        if i % 100 == 0:
            print(i)

        BEST_PRESSURE_RELEASE = 0
        BEST_SOLUTION = []
        print("Ol: before exclusion: ", ol[i])
        print("Excludeing: ", hu[i])
        newGol = exclude_nodes(cleanG, hu[i])
        print("Ol: after exclusion: ", list(newGol))

        bpr_ol, bs_ol = find_best_solution(newGol)


        BEST_PRESSURE_RELEASE = 0
        BEST_SOLUTION = []
        print("Hu: before exclusion: ", hu[i])
        print("Excludeing: ", ol[i])
        newGhu = exclude_nodes(cleanG, ol[i])
        print("Hu: after exclusion: ", list(newGhu))
        bpr_hu, bs_hu = find_best_solution(newGhu)

        if bpr_ol + bpr_hu > best_total_pressure_release:
#            print("Best pressure release for ol: ", bpr_ol, "with solution: ", bs_ol)
#            print("Graph ol: ", list(newGol))
#            print("Best pressure release for hu: ", bpr_hu, "with solution: ", bs_hu)
#            print("Graph hu: ", list(newGhu))
            best_total_pressure_release = bpr_ol + bpr_hu
#            print("Best total pressure release: ", best_total_pressure_release)
#        if i==7:
#            show_graph(newGol)
#            show_graph(newGhu)

    toc = time.perf_counter()
    print(f"Found best solution in {toc - tic:0.4f} seconds")
    print("Best total pressure release: ", best_total_pressure_release)
    return best_total_pressure_release


def main(realinput):
    if realinput:
        fn = "Day16/input.txt"
    else:
        fn = "Day16/testinput.txt"

#    res1 = part1(fn)
#    print("Part 1: ", res1)
    res2 = part2(fn)
    print("Part 2: ", res2)
    return


if __name__ == "__main__":
    #    main(True)
    #    main(False)
    pass
