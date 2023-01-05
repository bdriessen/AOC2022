# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
maxi: int = 0
# read input file into a list of lists of numbers separated by blank lines
def read_input_file():
    global maxi
    with open("input.txt") as f:
        lines = f.read().split("\n\n")
        sumlist = []
        for l in lines:
            if len(l) > 0:
                numl = []

                for x in l.split("\n"):
                    if len(x) > 0:
                        numl.append(int(x)) # convert to int
                suml = sum(numl)
                sumlist.append(suml)
                maxi = max(maxi, suml)
                print(maxi)
        #sort sumlist
        sumlist.sort()
        # Print sum of maximum 3 elements
        print("Sum of maximum 3 elements is", sum(sumlist[-3:]))



    # find the maximum of one list of numbers
def find_max(numbers):
    if len(numbers) == 0: return 0
    return max(numbers)

# main program
def main():
    # read the input file
    input = read_input_file()
    # initialize the sum to 0


    # print the sum
    print(maxi)

# start main program
main()


