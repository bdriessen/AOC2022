#
# Advent of code 2022: Day 19
#
# Author: Bart Driessen
# Start date: 2023-01-18
# Part 1 done:
# Part 2 done:
#
import re
import copy

# Read input file
def read_input_file(fn):
    maxbots = []
    recipes = []
    maxval = [0, 0, 0]
    bp = []
    with open(fn) as f:
        lines = f.readlines()
    bps= []
    for line in lines:
        sections = re.split(r': ', line)[1].split('. ')
        recipes = []

        recipe = []
        maxval = [0, 0, 0]
        for section in sections:
            for x, y in re.findall(r'(\d+) (\w+)', section):
                y = ['ore', 'clay', 'obsidian'].index(y)
                recipe.append((int(x), y))
                maxval[y] = max(maxval[y], int(x))
            bp.append(recipe)
            recipe = []
        maxval.append(1000)
        maxbots.append(maxval)

        bps.append(bp)
        bp = []
    return bps, maxbots


def search_max_geodes(rtime, amnt, bots, bp, maxbots, cache):
    rtime -= 1
    amnt_ = copy.deepcopy(amnt)
    bots_ = copy.deepcopy(bots)

    if rtime == 0:
        return amnt[3]

    key = tuple([rtime, *amnt, *bots])
    if key in cache:
        return cache[key]

    max_geodes = amnt[3] + bots[3]

    # Five options exist to choose from:
    # 1. Do nothing
    # 2. Make a ore bot
    # 3. Make a clay bot
    # 4. Make an obsidian bot
    # 5. Make a geode bot
    # Each option recursively calls the search_max_geodes function with the new state

    for btype, recipe in enumerate(bp):
        # Production is identical for all bots
#        print(btype, recipe)
        amnt_[btype] = amnt[btype] + bots[btype]
        bots_[btype] = min(bots[btype], maxbots[btype])  ## Limit the amount of bots to the maximum amount of bots

        print("amnt", amnt_, "bots", bots_)

        # Check if we can make a bot
        can_make = True
        for x, y in recipe:
            if amnt_[y] < x:
                can_make = False
                break
        if can_make:
            # Make a bot
            bots_[btype] = bots_[btype] + 1
            amnt_[btype] = amnt_[btype] - x
        max_geodes = max(max_geodes, search_max_geodes(rtime, amnt_, bots_, bp, maxbots, cache))

    cache[key] = max_geodes
    print(max_geodes)
    return max_geodes


def parse_input():
    return

# Part 1
def part1(fn):
    bps, maxbots = read_input_file(fn)
    for nr, bp in enumerate(bps):
        maxbot = maxbots[nr]
        print(maxbot)
        max_geodes = search_max_geodes(24, [0, 0, 0, 0], [1, 0, 0, 0], bp, maxbot, {})
    return 0


# Part 2
def part2(fn):
    return 0


def main(realinput):
    if realinput:
        fn = "Day19/input.txt"
    else:
        fn = "Day19/testinput.txt"

    res1 = part1(fn)
    print("Part 1: ", res1)
#    res2 = part2(fn)
#    print("Part 2: ", res2)
    return


if __name__ == "__main__":
    #    main(True)
    #    main(False)
    pass
