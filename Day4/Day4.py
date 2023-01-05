# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re

def read_input_file():
    input_file = []
    with open('input.txt', 'r') as file:
        for line in file:
#            str_line = "".join([char for char in line if char != '\n'])
            # split str_line into parts separated by dash or comma
            parts = re.split(r'[-,]', line)
            # remove the newline character  from the last part
            parts[-1] = parts[-1].replace('\n', '')
            # convert the parts to integers
            parts = [int(part) for part in parts]
            input_file.append(parts)  # This returns a list of strings
        return input_file  # This returns a list of strings

def check_full_containment(pair):
    #Firs check if pair[0:1] contains pair[2:]
    if pair[0] <= pair[2] and pair[1] >= pair[3]:
        return True
    # Now check if pair[2:] contains pair[0:1]
    if pair[2] <= pair[0] and pair[3] >= pair[1]:
        return True
    return False

def check_partial_containment(pair):
    # Check if pair[0:1] contains pair[2:]
    if pair[0] <= pair[2] and pair[1] >= pair[2]:
        return True
    # Check if pair[2:] contains pair[0:1]
    if pair[2] <= pair[0] and pair[3] >= pair[0]:
        return True
    return False

# main program
#Part A
numberOfOverlaps = 0
fileinput = read_input_file()
for pair in fileinput:
    print(pair)
    if check_full_containment(pair):
        numberOfOverlaps += 1
print(numberOfOverlaps)

#Part B
numberOfOverlaps = 0
for pair in fileinput:
    if check_partial_containment(pair):
        numberOfOverlaps += 1
print(numberOfOverlaps)

