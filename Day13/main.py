#
# Advent of code 2022: Day xx
#
# Author: Bart Driessen
# Date: xxxx-xx-xx
#


# Read input file
def read_input_file(fn):
    pairs = []
    # read all linnes from input file

    with open(fn, "r") as file:
        # read all lines from input file and remove trailing newline
        lines = [line.rstrip() for line in file]
        linenum = 0
        for i in range(len(lines)//3 + 1):
            line = lines[linenum]
            left = eval(line)
            linenum += 1
            line = lines[linenum]
            right = eval(line)
            linenum += 2
            pairs.append((left, right))
            print((left, right))
    return pairs

# Parse input file
def parse_input_file(input_file):
    return

def index_exists_left(index, base_left):

    if index is None:
        return False
    try:
        tst = base_left[index[0]]
    except IndexError:
        return False

    try:
        for i in range(1, len(index)):
            if type(tst) is list:
                tst = tst[index[i]]
            else:
                return False
    except IndexError:
        return False

    return True

def index_exists_right(index, base_right):

    if index is None:
        return False

    try:
        tst = base_right[index[0]]
    except IndexError:
        return False

    try:
        for i in range(1, len(index)):
            if type(tst) is list:
                tst = tst[index[i]]
            else:
                return False

    except IndexError:
        return False

    return True

def get_next_index(index, base_left):

    nextindex = index.copy()
#    print("Index: ", nextindex)
    for i in range(len(index)-1, -1, -1):
#        print("i (in get_next_index): ", i)
        nextindex[i] = nextindex[i] + 1
#        print("nextindex: ", nextindex)
        if index_exists_left(nextindex, base_left):
            return nextindex
        else:
            # remove last element of nextindex
            if len(nextindex) > 1:
                nextindex.pop()
            else:
                return nextindex
#            print("nextindex after pop: ", nextindex)
    # Otherwise, no next index exists
    return None

def get_value_left(index, base_left):
    # get value from nested list l at index stored in array index
#    print("Index in function get_value_left():", index, "baseleft: ", base_left)
    if index is None:
        return None
    val = base_left[index[0]]
#    print(val)
    for i in range(1, len(index)):
        val = val[index[i]]
#        print(val)
#    print("Value returned: ", val)
    return val

def get_value_right(index, base_right):
    # get value from nested list l at index stored in array index
    print("Index in function get_value_right():", index, "baseright: ", base_right)
    if index == None:
        return None
    val = base_right[index[0]]
#    print(val)
    for i in range(1, len(index)):
        val = val[index[i]]
#        print(val)
#    print("Value returned: ", val)
    return val


def set_left_value_basepair(index, val, base_left):
    s = ""
    nbl = base_left.copy()
    for i in range(0, len(index)):
        s += "["+str(index[i])+"]"
    cmd = "nbl"+s+" = "+str(val)
#    print("Command: ", cmd)
#    print("base_left before left value update: ", nbl)
    exec(cmd)
#    print("base_left na left value update: ", nbl)
    return nbl

def set_right_value_basepair(index, val, base_right):

    s = ""
    nbr = base_right.copy()
    for i in range(0, len(index)):
        s += "["+str(index[i])+"]"
    cmd = "nbr"+s+" = "+str(val)
#    print("Command: ", cmd)
#    print("base_right before right value update: ", nbr)
    exec(cmd)
#    print("base_right na right value update: ", nbr)
    return nbr

# Check pair
def check_pair(left, right, index, base_left, base_right):

    nextindex = index

    print("Checking: Left: ", left, "Right: ", right, " at Index: ", index)

#    if isinstance(left, list) and left == []:
#        print("Left is empty list")
#        if isinstance(right, list) and right != []:
#            print("Right is empty list")
#            return "OK", base_left, base_right
#        print("*************************************************************")

    ########################
    # Case 1: Two integers
    ########################

    if isinstance(left, int) and isinstance(right, int):
        print("Left and right are integers: ", left, right)
        if left < right:
            return "OK", base_left, base_right
        if left > right:
            return "NOK", base_left, base_right
        return "NEXT", base_left, base_right

    ########################
    # Case 2: List + integers
    ########################
    if isinstance(left, list) and isinstance(right, int):
        print("Left is list, right is integer: ", left, right, " Updating base_right to ", [right])
        # convert right to list
        nextright = [right]
        nextleft = left
        # update global base_pair
        base_right = set_right_value_basepair(index, nextright, base_right)
        nextleft = get_value_left(index, base_left)
        nextright = get_value_right(index, base_right)
        return check_pair(nextleft, nextright, index, base_left, base_right)

    if isinstance(left, int) and isinstance(right, list):
        print("Left is int, right is list: ", left, right, " Updating base_left to ", [left])

        # convert right to list
        nextleft = [left]
        nextright = right
        # update global base_pair
        base_left = set_left_value_basepair(index, nextleft, base_left)

        nextleft = get_value_left(index, base_left)
        nextright = get_value_right(index, base_right)
        return check_pair(nextleft, nextright, index, base_left, base_right)


    ########################
    # Case 3: Two lists
    ########################

    # check if left is empty list

    if left == [] and right != []:
        print("Left is empty list")
        return "OK", base_left, base_right
    elif right == [] and left != []:
        print("Right is empty list")
        return "NOK", base_left, base_right
    elif left == [] and right == []:

        print("Both lists are empty, trying to fetch next pair")
        print("Len index: ", len(index))
        nextindex = get_next_index(index, base_left)
        print("Next index: ", nextindex)
        left_exists = index_exists_left(nextindex, base_left)
        right_exists = index_exists_right(nextindex, base_right)
#        nextleft = get_value_left(nextindex, base_left)
#        nextright = get_value_right(nextindex, base_right)
        if not left_exists and right_exists:
            print("Next left is None, next right is not None")
            return "OK", base_left, base_right
#        if (nextleft is None) and not (nextright is None):
#            print("Next left is None, next right is not None")
#            return "OK", base_left, base_right
        if left_exists and not right_exists:
            print("Next left is not None, next right is None")
            return "NOK", base_left, base_right

#        if (nextright is None) and not (nextleft is None):
#            print("Next right is None, next left is not None")
#            return "NOK", base_left, base_right

        nextleft = get_value_left(nextindex, base_left)
        nextright = get_value_right(nextindex, base_right)

        return check_pair(nextleft, nextright, nextindex, base_left, base_right)

    else:

        # Check next value in list
        print("Left and right are lists. Left: ", left, " Right: ", right, " Index: ", index, " Fetching list values")

        nextindex = index.copy()

        for i in range(len(left)):
            # check all elements in list
            if i == 0:
                # Dive into the list
                nextindex.append(0)
            else:
                # Get next index
                nextindex[-1] = i
#               print("Next index in for loop: ", nextindex)
            print("Next index: Voor ", nextindex)
            if not index_exists_right(nextindex, base_right):
                # No right pairs left
                return "NOK", base_left, base_right

            nextleft = get_value_left(nextindex, base_left)
            nextright = get_value_right(nextindex, base_right)
            print("Next pair from list iteration: Left: ", nextleft, " Right: ", nextright, " at index: ", nextindex)
            res, base_left, base_right = check_pair(nextleft, nextright, nextindex, base_left, base_right)
            if res == "OK" or res == "NOK":
                return res, base_left, base_right
        nextindex[-1] += 1
        if index_exists_right(nextindex, base_right):
            # Right pairs left
            return "OK", base_left, base_right

    return "NEXT", base_left, base_right
#        # We reached the end of the list
#        # Check if there are more pairs left
#
#        print("Next index check for 4 - before: ", nextindex)
#        nextindex = get_next_index(nextindex, base_left)
#        print("Next index check for 4 - after: ", nextindex)
#        if index_exists_left(nextindex, base_left):
#            if not index_exists_right(nextindex, base_right):
#                # No right pairs left
#                return "NOK", base_left, base_right
#            nextleft = get_value_left(nextindex, base_left)
#            nextright = get_value_right(nextindex, base_right)
#            return check_pair(nextleft, nextright, nextindex, base_left, base_right)
#
#        else:
#            if index_exists_right(nextindex, base_right):
#                return "OK", base_left, base_right
#        return "DONE", base_left, base_right

def bubbleSort(arr):
    n = len(arr)
    index = []
    # For loop to traverse through all
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):

            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            # is greater than the adjacent element
            left = base_left = arr[j]
            right = base_right = arr[j + 1]
            res, base_left, base_right = check_pair(left, right, index, base_left, base_right)
            if res == "NOK":
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Part 1
def part1(fn):
    pairs = read_input_file(fn)
    index = []
    pair_nr = 1
    sum_of_pair_numbers = 0
    oks = []
    noks = []
    others = []

    for pair in pairs:
        base_left = left = pair[0]
        base_right = right = pair[1]

        res, base_left, base_right = check_pair(left, right, index, base_left, base_right)
        print("*************************************************************")
        print("                                            Pair: ", pair, "Result: ", res)
        print("*************************************************************")
        if res == "OK":
            oks.append(pair_nr)
            sum_of_pair_numbers += pair_nr
        elif res == "NOK":
            noks.append(pair_nr)
        else:
            others.append(pair_nr)
        pair_nr += 1
    print("OK pairs: ", oks)
    print("NOK pairs: ", noks)
    print("Other pairs: ", others)
    print("Part 1: ", sum_of_pair_numbers)

    return 0

# Part 2
def part2(fn):
    pairs = read_input_file(fn)
    index = []
    pair_nr = 1
    sum_of_pair_numbers = 0
    oks = []
    noks = []
    others = []

    msgs = []
    msgs.append([[2]])
    for pair in pairs:
        msgs.append(pair[0])
        msgs.append(pair[1])

    msgs.append([[6]])

    msgs = bubbleSort(msgs)

    for i in range(len(msgs)):
        print("Part 2: i = ", i, "msg: ", msgs[i])

#    for i in range(len(msgs)):
#        if msgs[i] == [[[2]]]:
#            x = i+1
#        if msgs[i] == [[[6]]]:
#            x = (i+1)*x
    return 0


if __name__ == "__main__":

    testrun = True
    testrun = False

    if testrun:
        res1 = part1("testinput.txt")
        print("Part 1: ", res1)
        res2 = part2("testinput.txt")
        print("Part 2: ", res2)
    else:
        res1 = part1("input.txt")
        print("Part 1: ", res1)
        res2 = part2("input.txt")
        print("Part 2: ", res2)


