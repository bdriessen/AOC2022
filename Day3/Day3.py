## This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def read_input_file():
    input_file = []
    with open('input.txt', 'r') as file:
        for line in file:
            str_line = "".join([char for char in line if char != '\n'])
            input_file.append(str_line)
        return input_file  # This returns a list of strings

def find_score(common_letters):
    score = 0
    for letter in common_letters:
        if letter.islower():
            score += ord(letter) - ord('a') + 1
        else:
            score += ord(letter) - ord('A') + 27
    return score

# main program
ac_input = read_input_file()
print(ac_input)
totalscore = 0
for string in ac_input:
    # split the line into 2 strings
    part1, part2 = string[:len(string)//2], string[len(string)//2:]
    #  print("original: ", string, "Part1:", part1, "Part2:", part2)
    # find common characters
    common = [char for char in part1 if char in part2]
    # remove duplicates
    for char in common:
        if common.count(char) > 1:
            common.remove(char)

    print("common: ", common)
    # find the score
    score = find_score(common)
    # print score
    print("Score: ", str(score))
    totalscore += score

print(totalscore)

# start of partB
# Convert string list into groups of 3
grouped = []
totalscore = 0
for i in range(0, len(ac_input), 3):
    grouped.append(ac_input[i:i+3])
for group in grouped:
    # find common characters
    common = [char for char in group[0] if char in group[1] and char in group[2]]
    # remove duplicates
    for char in common:
        if common.count(char) > 1:
            common.remove(char)

    print("common: ", common)
    # find the score
    score = find_score(common)
    # print score
    print("Score: ", str(score))
    totalscore += score
print(totalscore)


