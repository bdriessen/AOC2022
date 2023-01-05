# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def read_input(filename):
    f = open(filename, "r")
    cmds = list()
    cmnds = []  # This will hold the commands
    for line in f:
        # Split the line into a list of words and remove the newline character
        tokens = line.split()

        if tokens[0] == 'noop':
            tokens.append('0')  # deltaX
            tokens.append('1')  # duration in cycles
        else:
            tokens.append('2')  # duration in cycles

        # Cast tokens[1] and tokens[2] to integers
        tokens[1] = int(tokens[1])
        tokens[2] = int(tokens[2])

#        print("This line consists of the following tokens: " + str(tokens))
        # Put the tokens in a dictionary
        cmnds.append(tokens)
    return cmnds

def parse_input(cmnds, screen):
    triggers = [20, 60, 100, 140, 180, 220]

    # PARSE FIRST COMMAND
    cmnd_ptr = 0
    cmd = cmnds[cmnd_ptr]

    X = 1

    cycle_start = 1  # Cycle nr at the start of the cmd
    cycle_end = cycle_start + cmd[2]  # Cycle nr after the cmd has finished, ie. cycle nr at the start of next command
    solution = 0

    for c in range(1,240):
        # Calculate SS during this cycle
        if c >= cycle_end:
            # Parse new command
            cmnd_ptr = cmnd_ptr + 1
            cmd = cmnds[cmnd_ptr]
            cycle_start = cycle_end
            cycle_end = cycle_start + cmd[2]

            # Calculate new X during this cmd
            X = X + cmnds[cmnd_ptr - 1][1]
        print("Cycle: ", c, "X: ", X, "cmd: ", cmd, "cycle_start: ", cycle_start, "cycle_end: ", cycle_end)

        if (c + 1) in triggers:
            solution = solution + (c + 1) * X
            print("Triggering: ", c + 1 , " Solution for part A so far: ", solution)

        # Refresh screen
        screen = refresh_screen(screen, c, X)
    return solution, screen

def print_screen(screen):
    # reshape screen to 6 rows of 40 elements
    screen = [screen[i:i + 40] for i in range(0, len(screen), 40)]
    for line in screen:
        print(''.join(line))
    return

def refresh_screen(screen, c, X):
    # Refresh screen
    pixel = c-1
    # relpix is remainder of pixel divided by 40
    relpix = (c % 40) - 1

    if relpix in range(X-1, X+2):
        screen[pixel] = '#'
    return screen

def main():
    # Part A
    screen = ['.' for x in range(240)]
    cmds = read_input("input.txt")
    print(cmds)
    solution, screen = parse_input(cmds, screen)
    print("Solution: ", solution)

    # Part B
    # Create array of 240 elements filled with dots with name screen

    print("Screen: ", screen)
    print_screen(screen)

    return


if __name__ == "__main__":
    main()


