# Advent of code Day 9
import numpy as np

def read_file(filename):
    # Read input file data
    with open(filename, "r") as f:
        data = f.read().splitlines()
        # convert 2nd token to int
        for i in range(len(data)):
            data[i] = data[i].split(" ")
            data[i][1] = int(data[i][1])
    return data

def move_head(direction, head):
    if direction == "R":
        return head[0] + 1, head[1]
    elif direction == "L":
        return head[0] - 1, head[1]
    elif direction == "U":
        return head[0], head[1] + 1
    elif direction == "D":
        return head[0], head[1] - 1
    return head

def move_tail(tail, head):
    # Check if tail needs to be moved if distance between head and tail is greater than 1
    if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1:
        # If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction.
        if head[0] - tail[0] == 2 and head[1] == tail[1]:
            return tail[0] + 1, tail[1]
        elif head[0] - tail[0] == -2 and head[1] == tail[1]:
            return tail[0] - 1, tail[1]
        elif head[1] - tail[1] == 2 and head[0] == tail[0]:
            return tail[0], tail[1] + 1
        elif head[1] - tail[1] == -2 and head[0] == tail[0]:
            return tail[0], tail[1] - 1
        else:
            # if the head and tail aren't in the same row or column, the tail always moves one step diagonally
            if head[0] != tail[0] and head[1] != tail[1]:
                if head[0] > tail[0] and head[1] > tail[1]:
                    return tail[0] + 1, tail[1] + 1
                elif head[0] > tail[0] and head[1] < tail[1]:
                    return tail[0] + 1, tail[1] - 1
                elif head[0] < tail[0] and head[1] > tail[1]:
                    return tail[0] - 1, tail[1] + 1
                elif head[0] < tail[0] and head[1] < tail[1]:
                    return tail[0] - 1, tail[1] - 1

    return tail

def partA():
    data = read_file("input.txt")
    head = (0, 0)
    tail = (0, 0)

    # cycle through data
    tails = [tail]
    for i in range(len(data)):
        for j in range(data[i][1]):
            head = move_head(data[i][0], head)
            tail = move_tail(tail, head)
            tails.append(tail)

    print("Antwoord deel A: ", len(set(tails)))

    return

def partB():
    data = read_file("input.txt")
    rope = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    newrope = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

    head = (0, 0)
    tail = (0, 0)

    # cycle through data
    tails = [tail]
    for i in range(len(data)):
        for j in range(data[i][1]):
            head = move_head(data[i][0], rope[0])
            newrope[0] = head
            # Check if rope has tension and if so, update the first tension occurance
            for knot in range(1,len(rope)):
                head = newrope[knot-1]
                tail = rope[knot]
                newrope[knot] = move_tail(tail, head)

            rope = newrope.copy()
            tails.append(rope[len(rope)-1])
 #           print("Rope: ", rope)

    print("Antwoord deel B: ", len(set(tails)))

    return

if __name__ == "__main__":
    partA()
    partB()

