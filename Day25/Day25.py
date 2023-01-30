#
# Advent of code 2022: Day 25
#
# Author: Bart Driessen
# Date: xxxx-xx-xx
#

import time
import math

# Read input file
def read_input_file(fn):
    with open(fn, "r") as file:
        lines = file.readlines()
        # remove trailing \n
        lines = [line.rstrip() for line in lines]
        return lines

# Parse input file
def parse_input_file(input_file):
    return


def snafu2dec(snafu):
    base = 5
    exp = len(snafu) - 1
    dec = int(snafu[0]) * base ** exp
    for i in range(1,len(snafu)):
        exp = len(snafu) - i - 1
        c = snafu[i]
        if c == "-":
            dec = dec - base ** exp
        elif c == "=":
            dec = dec - 2 * base ** exp
        else:
            dec = dec + int(c) * base ** exp
    return dec

def dec2snafu(dec):
    base = 5
    base5 = []
    q = dec // base
    r = dec - q * base
    base5.append(r)
    while q > 0:
        r = q % base
        q = q // base
        base5.append(r)
    base5.reverse()
    print(base5)
    snafu = ""

    carry = 0
    new_num = []
    for i in range(len(base5)-1, -1, -1):
        a_k = base5[i]+carry
        if a_k >=3:
            a_k = a_k - 5
            carry = 1
        else:
            carry = 0
        new_num.append(a_k)
    if carry == 1:
        new_num.append(1)
    new_num.reverse()

    for i in range(len(new_num)):
        if new_num[i] == 0:
            snafu = snafu + "0"
        elif new_num[i] == 1:
            snafu = snafu + "1"
        elif new_num[i] == 2:
            snafu = snafu + "2"
        elif new_num[i] == -1:
            snafu = snafu + "-"
        elif new_num[i] == -2:
            snafu = snafu + "="
    return snafu



# Part 1
def part1(fn):
    print(snafu2dec("1"))
    print(snafu2dec("2"))
    print(snafu2dec("1="))
    print(snafu2dec("1-"))
    print(snafu2dec("10"))
    print(snafu2dec("11"))
    print(snafu2dec("12"))
    print(snafu2dec("2="))
    print(snafu2dec("2-"))
    print(snafu2dec("20"))
    print(snafu2dec("1=0"))
    print(snafu2dec("1-0"))
    print(snafu2dec("1=11-2"))
    print(snafu2dec("1-0---0"))
    print(snafu2dec("1121-1110-1=0"))

    snafu = dec2snafu(1747)
    print(snafu)
    print(snafu2dec(snafu))

    lines = read_input_file(fn)
    print(lines)
    sum = 0
    for line in lines:
        sum = sum + snafu2dec(line)
    print(sum)
    snafu = dec2snafu(sum)
    print(snafu)

    return 0

# Part 2
def part2(fn):
    input = read_input_file(fn)

    return 0

def main():
    real = True   # True = real input, False = test input
    part = 1
    day = 25

    # Start timer
    tic = time.perf_counter()
    if real:
        fn = "Day" + str(day) + "/input.txt"
    else:
        fn = "Day" + str(day) + "/input_test.txt"

    if part == 1:
        res1 = part1(fn)
        print("Part 1: ", res1)
    else:
        res2 = part2(fn)
        print("Part 2: ", res2)
    toc = time.perf_counter()
    print(f"Time elapsed: {toc - tic:0.4f} seconds")

    return
