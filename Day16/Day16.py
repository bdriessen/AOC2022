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
        newweight = newgraph.get_edge_data(neighbors[0], node)['weight'] + newgraph.get_edge_data(neighbors[1], node)['weight']
        newgraph.add_edge(neighbors[0], neighbors[1], weight=newweight)
        newgraph.remove_node(node)
    return newgraph



# Part 1
def part1(fn):
    nodes = read_input_file(fn)
    G = nx.Graph()

    for node in nodes:
        G.add_node(node['name'], rate=node['rate'])
        for to in node['to']:
            G.add_edge(node['name'], to, weight=1)

    cleanG = clean_graph(G)

    pos = nx.spring_layout(cleanG)
    pos2 = nx.spring_layout(G)


    nx.draw(cleanG, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(cleanG, 'weight')
    nx.draw_networkx_edge_labels(cleanG, pos, edge_labels=edge_labels)

    # for k, v in pos2.items():
    #     # Shift the x values of every node by 10 to the right
    #     v[0] = v[0] + 10
    # nx.draw(G, pos2, with_labels=True)
    # edge_labels = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_edge_labels(G, pos2, edge_labels=edge_labels)


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
