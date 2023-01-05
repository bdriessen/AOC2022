#
# Day 7 of Advent of Code 2022
#

import networkx as nx
import matplotlib.pyplot as plt

def read_input(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse_input(lines, G):
    # root always exists
    G.add_node('/', labels=True, label='/', files = [])
    cwd = '/'
    for line in lines:
        line = line.split(' ')

        if line[0] == '$': # process a command
            listing = False
            if line[1] == 'cd':
                if line[2] == '..':
                    # select parent node in G
                    # remove last element from cwd excluding the '/'
                    cwd = cwd[:cwd.rfind('/')]
                    cwd = cwd[:cwd.rfind('/')] + '/'

                elif line[2] == '/':
                    cwd = '/'
                else:
                    cwd = cwd + line[2] + '/'
            elif line[1] == 'ls':
                listing = True
        else:
            # process a listing
            if line[0]=='dir':
                # create a directory if it does not exist
                newdir = cwd + line[1] + '/'
                for n in G.nodes:
                    if n == newdir: break # directory already exists
                G.add_node(newdir, labels=True, label=line[1], color='red', files=[])
                G.add_edge(cwd, newdir)
            elif line[0]!='':
                # attach file to current working directory
                files = G.nodes[cwd]['files']
                files.append([line[0], line[1]])
                print(files)
                G.nodes[cwd]['files'] = files
    return

def dir_size(G, node):
    dir_fs = 0

    for f in G.nodes[node]['files']:
        dir_fs += int(f[0])

    for subdir in G.successors(node):

        dir_fs += dir_size(G, subdir)

    return dir_fs




def main():
    lines = read_input('input.txt')
    G = nx.DiGraph()
    parse_input(lines, G)

    total_fs = 0
    for n in G.nodes():
 #       print(n)
 #       print(G.nodes[n]['files'])
        ds = dir_size(G, n)
        if ds <= 100000: total_fs += ds

    print("The answer is: ", total_fs)


#    nx.draw(G, with_labels=True)
#    plt.show()


    # Part B
    NeededSpace = 30000000
    TotalDiskSpace = 70000000

    disk_usage = dir_size(G, '/')
    space_needed = NeededSpace - (TotalDiskSpace - disk_usage)
    dir_options = []
    for n in G.nodes():
        ds = dir_size(G, n)
        if ds >= space_needed:
            dir_options.append(ds)

    dir_options.sort()
    print("The answer is: ", dir_options[0])
    return

if __name__ == '__main__':
    main()
