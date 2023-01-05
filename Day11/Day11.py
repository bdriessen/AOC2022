#
# Advent of Code 2022 Day 11
#
import re

class Monkey:
    common_divisor = 1
    relief_factor = 1

    def __init__(self, id):
        self.id = id
        self.items = []
        self.operation = ""
        self.divisiontest = 1
        self.throwto = [-1, -1] # [0]: Monkey ID if divisiontest passes, [1]: Monkey ID if divisiontest fails
        self.inspections = 0

    def print(self):
        print(f"Monkey {self.id}")
        print(f"             Items: {self.items}")
        print(f"             Operation: {self.operation}")
        print(f"             Divisiontest: {self.divisiontest}")
        print(f"             Throw: {self.throwto}")
        return

    def gooi(self, monkeylist):
        for item in self.items:
            self.inspections += 1
            # Execute operation defined in self.operation
            item = eval(self.operation, {"old": item})
            # Divide item by 3 and round down to nearest integer
            item = item // Monkey.relief_factor
            # If item is divisible by self.divisiontest, throw to monkey in self.throw[0]
            if item % self.divisiontest == 0:
                target = self.throwto[0]
                newitemvalue = item % Monkey.common_divisor
                monkeylist[self.throwto[0]].items.append(newitemvalue)
            # Else throw to monkey in self.throwto[1]
            else:
                target = self.throwto[1]
                newitemvalue = item % Monkey.common_divisor
                monkeylist[self.throwto[1]].items.append(newitemvalue)
        self.items = []
        return

def read_input(fn):
    with open(fn) as f:
        lines = f.read().splitlines()
        cmds = []
        for line in lines:
            # Split the command into a list of strings
            cmd = re.split(" |,|:", line)
            # Remove empty strings
            cmd = list(filter(None, cmd))
#            print(cmd)
            if len(cmd) != 0: cmds.append(cmd)
        return cmds

def parse_input(input):
    currentmonkey = -1
    monkeylist = []

    for cmd in input:
#        print(cmd)
        if cmd[0] == "Monkey":
            currentmonkey = int(cmd[1])
            monkeylist.append(Monkey(currentmonkey))
        elif cmd[0] == "Starting":
            monkey = monkeylist[currentmonkey]
            # Convert of cmd[2:] to int
            monkey.items = [int(i) for i in cmd[2:]]
        elif cmd[0] == "Operation":
            monkey = monkeylist[currentmonkey]
            operation = cmd[3:]
            # covert list of strings to single string
            operation = " ".join(operation)
            monkey.operation = operation
        elif cmd[0] == "Test":
            monkey = monkeylist[currentmonkey]
            monkey.divisiontest = int(cmd[3])
        elif cmd[1] == "true":
            monkey = monkeylist[currentmonkey]
            monkey.throwto[0] = int(cmd[5])
        elif cmd[1] == "false":
            monkey = monkeylist[currentmonkey]
            monkey.throwto[1] = int(cmd[5])
        else:
            pass
    return monkeylist

def print_monkeylist(monkeylist):
    for monkey in monkeylist:
        monkey.print()
    return

def print_monkeylist_items(monkeylist):
    for monkey in monkeylist:
        print("Monkey: ", monkey.id, " Items: ", monkey.items, " Inspections: ", monkey.inspections)
    return

def part1(input):
    input = read_input(input)
    #    print(input)
    monkeylist = parse_input(input)
#    print_monkeylist_items(monkeylist)

    Monkey.relief_factor = 3
    for i in range(len(monkeylist)):
        Monkey.common_divisor *= monkeylist[i].divisiontest
#    print("Common divisor: ", Monkey.common_divisor)

    for rnd in range(1, 21):
#        print(f"**********************Round {rnd}")
        for monkey in monkeylist:
            monkey.gooi(monkeylist)
#        print_monkeylist_items(monkeylist)

    businesslist = []
    for monkey in monkeylist:
        businesslist.append(monkey.inspections)
    businesslist.sort()
    mb = businesslist[-1]*businesslist[-2]
    print("Part 1: ", mb)

    return 0

def part2(input):
    input = read_input(input)
    #    print(input)
    monkeylist = parse_input(input)
#    print_monkeylist_items(monkeylist)

    Monkey.relief_factor = 1

    for i in range(len(monkeylist)):
        Monkey.common_divisor *= monkeylist[i].divisiontest
#    print("Common divisor: ", Monkey.common_divisor)

    for rnd in range(1, 10001):
        #        print(f"**********************Round {rnd}")
        for monkey in monkeylist:
            monkey.gooi(monkeylist)
    #        print_monkeylist_items(monkeylist)

    businesslist = []
    for monkey in monkeylist:
        businesslist.append(monkey.inspections)
    businesslist.sort()
    mb = businesslist[-1] * businesslist[-2]
    print("Part 2: ", mb)

    return 0

if __name__ == '__main__':
    part1("input.txt")
    part2("input.txt")
