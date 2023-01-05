# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def read_input_file():
    strategy = []
    with open('input.txt', 'r') as file:
        for line in file:
            strategy.append(line.split())
        return strategy  # This returns a string

def isWinningMove(move):
    if move[0] == 'A' and move[1] == 'Y': return True
    if move[0] == 'B' and move[1] == 'Z': return True
    if move[0] == 'C' and move[1] == 'X': return True
    return False

def isLosingMove(move):
    if move[0] == 'A' and move[1] == 'Z': return True
    if move[0] == 'B' and move[1] == 'X': return True
    if move[0] == 'C' and move[1] == 'Y': return True
    return False

def isTieMove(move):
    if move[0] == 'A' and move[1] == 'X': return True
    if move[0] == 'B' and move[1] == 'Y': return True
    if move[0] == 'C' and move[1] == 'Z': return True
    return False

def bonus(move):
    if move[1] == 'X': return 1
    if move[1] == 'Y': return 2
    if move[1] == 'Z': return 3
    return 0

# main program
strategy = read_input_file()
#  print(strategy)
totalscore = 0
for move in strategy:
    if isWinningMove(move):
        score = 6 + bonus(move)
    elif isLosingMove(move):
        score = 0 + bonus(move)
    elif isTieMove(move):
        score = 3 + bonus(move)
    else:
        print("Invalid move")
    totalscore += score

print(totalscore)

planB = {
    'X': {'A': 'C', 'B': 'A', 'C': 'B'},
    'Y': {'A': 'A', 'B': 'B', 'C': 'C'},
    'Z': {'A': 'B', 'B': 'C', 'C': 'A'}
}
print(planB)
totalscore = 0
for move in strategy:
    newmove = planB[move[1]][move[0]]


    if newmove[1] == 'A': newmove[1] = 'X'
    if newmove[1] == 'B': newmove[1] = 'Y'
    if newmove[1] == 'C': newmove[1] = 'Z'

    print(newmove)
    if isWinningMove(newmove):
        score = 6 + bonus(newmove)
    elif isLosingMove(newmove):
        score = 0 + bonus(newmove)
    elif isTieMove(newmove):
        score = 3 + bonus(newmove)
    else:
        print("Invalid move")
    totalscore += score

print(totalscore)
