#
# Advent of code 2022: Day 16
#
# Author: Bart Driessen
# Date: 2022-01-10
#

import re
import networkx as nx
import matplotlib.pyplot as plt


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
    print("Now checking: ", list(graph.nodes(data=True)))
    nodes_to_remove = []
    for node in graph.nodes():
        print("Investigating node: ", node, "with rate: ", newgraph.nodes[node]['rate'])
        if graph.nodes[node]["rate"] == 0 and len(list(graph.neighbors(node))) == 2:
            nodes_to_remove.append(node)
            print("Found node to remove: ", node)
    #            neighbors = list(graph.neighbors(node))
    #            newgraph.add_edge(neighbors[0], neighbors[1], weight=1)

    print("Nodes to remove: ", nodes_to_remove)
    for node in nodes_to_remove:
        neighbors = list(newgraph.neighbors(node))
        newweight = newgraph.get_edge_data(neighbors[0], node)['weight'] + newgraph.get_edge_data(neighbors[1], node)[
            'weight']
        newgraph.add_edge(neighbors[0], neighbors[1], weight=newweight)
        newgraph.remove_node(node)
    return newgraph


def solution_possible(time, maxrate, pressure_release, best_pressure_release):
    if pressure_release + (30 - time) * maxrate < best_pressure_release:
        # This solution cannot be better than the best solution found so far
        return False
    else:
        return True


def solve(state, solution):
    graph = state.graph
    sh_pths = state.sh_pths
    time = state.time
    rate = state.rate
    maxrate = state.maxrate
    pressure_release = state.pressure_release
    best_pressure_release = state.best_pressure_release

    nodes = list(graph.nodes())
    nodes.sort()
    old_time = time
    old_pressure_release = pressure_release
    old_rate = rate

    # Extend solution
    last_node = solution[-1]
    for node in nodes:
        if node not in solution:
            # Try to add node to solution
            # Calculate path to next node
            path = state.sh_pths[last_node][node]

            # Calculate time to next node
            last_path_node = path[0]
            delta_time = 0
            for path_node in path[1:]:
                delta_time += graph.get_edge_data(last_path_node, path_node)['weight']
                last_path_node = path_node
            new_time = time + delta_time
            new_pressure_release = pressure_release + delta_time * rate
            # This is the pressure release after we reached the new location

            # Open the valve if we are at the end of the path
            new_time += 1
            new_pressure_release += rate
            # Note that the new rate will only become effective after the valve has been opened
            new_rate = rate + graph.nodes[node]['rate']

            # Check if this solution can result in a better solution
            if solution_possible(new_time, maxrate, pressure_release, best_pressure_release):
                solution.append(node)
                state_new = {'graph': graph, 'sh_pths': sh_pths,
                             'time': new_time, 'rate': new_rate, 'maxrate': maxrate,
                             'pressure_release': new_pressure_release,
                             'best_pressure_release': best_pressure_release}
                state_res, solution = solve(state_new, solution)

                # If solution is complete, check if it is better than the best solution found so far
                if len(solution) == len(graph.nodes()):
                    if state_res["pressure_release"] > state_res["best_pressure_release"]:
                        state_res["best_pressure_release"] = state_res["pressure_release"]
                        print("New best solution found: ", solution, "with pressure release: ",
                              state_res["best_pressure_release"])

            else:
                pass

    # We have found a solution
    if len(solution) == len(graph.nodes()):  # I guess this is not necessary

        # Calculate the pressure release
        if pressure_release > best_pressure_release:
            best_pressure_release = pressure_release
            print("Found a new best solution: ", solution, "with pressure release: ", pressure_release)

    return best_pressure_release, solution


# Part 1
def part1(fn):
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
    shortest_paths = nx.shortest_path(cleanG, weight='weight')
    #    print("A shortest paths: ", shortest_paths['AA']['HH'])

    state = {'graph': cleanG, 'sh_pths': shortest_paths, 'time': 0, 'rate': 0, 'maxrate': maxrate, 'pressure_release': 0, 'best_pressure_release': 0}

    solution = ['AA']
    state, solution = solve(state, solution)

    pos = nx.spring_layout(cleanG)

    nx.draw(cleanG, pos, with_labels=True)
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
