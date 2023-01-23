#
# Advent of code 2022: Day 20
#
# Author: Bart Driessen
# Start date: 2023-01-23
# Part 1 done:
# Part 2 done:
#



# Read input file
def read_input_file(fn):
    with open(fn) as f:
        lines = f.readlines()
        # remove \n and empty strings
        lines = [x.strip() for x in lines if x.strip()]
        # replace colon with equal sing
        lines = [x.replace(":", "=") for x in lines]
    return lines

def parse_input():
    return


# Part 1
def part1(fn):
    lines = read_input_file(fn)
    solved = False
    while not solved:
        for line in lines:
            try:
                exec(line)
            except NameError:
                pass
            if 'root' in locals():
                solved = True
                break
    solution = int(eval('root'))

    return solution

# Part 2
def part2(fn):
    lines = read_input_file(fn)
    # find line starting with "root"
    idx_humn = 0
    for idx, line in enumerate(lines):
        if line.startswith("humn"):
            idx_humn = idx
            break

    solved = False
    human = 0
    while not solved:
        human_str = "humn = " + str(human)
        print(human_str)
        name_error_exist = True
        while name_error_exist:
            name_error_exist = False
            for line in lines:
                try:
                    if line.startswith("humn"):
                        exec(human_str)
                    else:
                        exec(line)
                except NameError:
                    name_error_exist = True
            if 'root' in locals():
                print("human: ", human, "root: ", eval('root'))
                if eval('root') == True:
                    solved = True
                    break
                else:
                    human += 1
                    break
    solution = human
    print(eval('pppw'))
    print(eval('sjmn'))


    return solution


def main():
    real = False
    part = 2



    if part == 1:
        if real:
            fn = "Day21/input.txt"
        else:
            fn = "Day21/input_test.txt"
        res1 = part1(fn)
        print("Part 1: ", res1)
    else:
        if real:
            fn = "Day21/input2.txt"
        else:
            fn = "Day21/input_test2.txt"
        res2 = part2(fn)
        print("Part 2: ", res2)
    return
