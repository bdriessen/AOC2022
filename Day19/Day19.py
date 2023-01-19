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
#    print("rtime: ", rtime, "amnt: ", amnt, "bots: ", bots, "maxbots: ", maxbots)

    search_option = ["nothing", "other"]    # if we can build a geode, do it

    if rtime == 0:
        return amnt[3]

    key = tuple([rtime, *amnt, *bots])
    if key in cache:
        return cache[key]

    rtime_ = rtime - 1
    amnt_ = amnt.copy()
    bots_ = bots.copy()

    max_geodes = amnt[3] + bots[3] * rtime # This is the amount we have at the end, but maybe we can do better

    for option in search_option:
        if option == "nothing":
            for btype in range(4):
                amnt_[btype] += bots[btype]
                if amnt_[btype] > maxbots[btype]*rtime_ and btype != 3:
                    amnt_[btype] = maxbots[btype]*rtime_

            max_geodes = max(max_geodes, search_max_geodes(rtime_, amnt_, bots_, bp, maxbots, cache))
        else:
            for btype, recipe in enumerate(bp):
                added = False
                amnt_ = amnt.copy()
                for bot in range(4):
                    amnt_[bot] += bots[bot]
                bots_ = bots.copy()
                # Check if we can make a bot, but only if it is useful
                if bots[btype] < maxbots[btype]:
                    can_make = True
                    for cost, botcoin in recipe:
                        if amnt[botcoin] < cost:
                            can_make = False
                            break
                    if can_make:   # We can make a bot
                        # Make a bot of type btype
                        for cost, botcoin in recipe:
                            amnt_[botcoin] -= cost
                        bots_[btype] = bots[btype] + 1
                        added = True
                for res in range(4):
                    if amnt_[res] > maxbots[res]*rtime_ and btype != 3:
                        amnt_[res] = maxbots[res]*rtime_

                if added:
                    max_geodes = max(max_geodes, search_max_geodes(rtime_, amnt_, bots_, bp, maxbots, cache))

    cache[key] = max_geodes
    return max_geodes


def parse_input():
    return

# Part 1
def part1(fn):
    v = 0
    bps, maxbots = read_input_file(fn)
    for nr, bp in enumerate(bps):
        maxbot = maxbots[bps.index(bp)]
        print("maxbot: ", maxbot, "bp: ", bp)
        max_geodes = search_max_geodes(24, [0, 0, 0, 0], [1, 0, 0, 0], bp, maxbot, {})
        print("max_geodes: ", max_geodes)
        v += max_geodes * (nr+1)
    return v


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
