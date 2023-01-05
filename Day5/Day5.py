# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import re


def read_input_file():
    input_file = []
    with open('input.txt', 'r') as file:
        # read lines from file until empty line
        lines = file.readlines()
        # remove the newline character from all lines
        lines = [line.replace('\n', '') for line in lines]

        # Build stacks
        stacks = []
        for stacknr in range(0, 9):
            # check if stack contains letter
            stack = []
            for linenr in range(7, -1, -1):
                line = lines[linenr]
                if line[stacknr * 4 + 1] != ' ':
                    stack.append(line[stacknr * 4 + 1])
            stacks.append(stack)




        # Build moves
        moves = []
        nr_of_moves = len(lines) - 10
        print(nr_of_moves)
        for linenr in range(10, nr_of_moves + 10):
            line = lines[linenr]
            move = line.split()
            move_matrix = []
            for i in range(0, len(move)):
                if move[i].isdigit():
                    move_matrix.append(int(move[i]))
            moves.append(move_matrix)


        return stacks, moves  # This returns a list of strings

def restack(stacks, move):
    for i in range(0, move[0]):
#        print("Removing box from index: ", move[1]-1, " and placing it on index: ", move[2]-1)
        # remove box from stack defined by move[1]
        box = stacks[move[1]-1].pop()
#        print("box: ", box)
        # add box to stack defined by move[2]
        stacks[move[2]-1].append(box)
    return stacks

def restackB(stacks, move):
    #        print("Removing box from index: ", move[1]-1, " and placing it on index: ", move[2]-1)
    # remove box from stack defined by move[1]
    idx = len(stacks[move[1]-1]) - move[0]
    boxes = stacks[move[1] - 1][idx:]
    print("boxes: ", boxes)

    # remove boxes from stack
    if idx > 0:
        stacks[move[1] - 1] = stacks[move[1] - 1][0:idx]
    else:
        stacks[move[1] - 1] = []

    #        print("box: ", box)
    # add box to stack defined by move[2]
    stacks[move[2] - 1] = stacks[move[2] - 1] + boxes
    return stacks

# main program
# Part A
stacks, moves = read_input_file()
#print(stacks)
print(moves[-10:])

for move in moves:
#    print(move)
    stacks = restack(stacks, move)

for stack in stacks:
    if len(stack) > 0:
        print(stack[len(stack)-1])

# Part B
stacks, moves = read_input_file()
for move in moves:
    stacks = restackB(stacks, move)

for stack in stacks:
    if len(stack) > 0:
        print(stack[len(stack)-1])
