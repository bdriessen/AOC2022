#
# Advent of code 2022: Day 20
#
# Author: Bart Driessen
# Start date: 2023-01-23
# Part 1 done:
# Part 2 done:
#

import re


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
    for line in lines:
        if line.startswith("root"):
            root = line
            break

    tokens = []
    for line in lines:
        # Split line into words using ":" or " " as separator
        words = re.split(r'[: ]', line)
        # remove '=' from first word in words
        words[0] = words[0].replace("=", "")
        tokens.append(words)

    solved = False
    while not solved:
        for formula in tokens:
            # if len (formula) == 2, then it is a value
            if len(formula) == 2 and formula[0] != "humn":
                exec(formula[0] + " = " + formula[1])
                # print(formula[0] + " = " + formula[1])
            elif len(formula) == 4:
                res = formula[0]
                op1 = formula[1]
                op = formula[2]
                op2 = formula[3]
                if res == 'root':
                    if op1 in locals():
                        exec(op2 + " = " + op1)
                    elif op2 in locals():
                        exec(op1 + " = " + op2)
                elif res in locals():
                    if op1 in locals() and op2 not in locals():
                        if op2 == '+':
                            exec(op2 + " = " + res + "-" + op1)
                        elif op2 == '*':
                            exec(op2 + " = " + res + "//" + op1)
                        elif op2 == '/':
                            exec(op2 + " = " + res + "*" + op1)
                        elif op2 == '-':
                            exec(op2 + " = " + res + "+" + op1)
                    elif op1 not in locals() and op2 in locals():
                        if op1 == '+':
                            exec(op1 + " = " + res + "-" + op2)
                        elif op1 == '*':
                            exec(op1 + " = " + res + "//" + op2)
                        elif op1 == '/':
                            exec(op1 + " = " + res + "*" + op2)
                        elif op1 == '-':
                            exec(op1 + " = " + res + "+" + op2)
                else:
                    if op1 in locals() and op2 in locals():
                        exec(res + " = " + op1 + op + op2)

        if 'humn' in locals():
            solved = True
            break
    solution = int(eval('humn'))

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
            fn = "Day21/input.txt"
        else:
            fn = "Day21/input_test.txt"
        res2 = part2(fn)
        print("Part 2: ", res2)
    return
