"""advent of code"""

## Day 1 Part 1 ##

#from https://adventofcode.com/2021/day/1/input
#get data

# open file and read
txt = open('input.txt')
txt = txt.read()

# make list of data
txt2 = txt.strip().split()
print(txt2)


def make_counter():
    """count increases line to line in input.txt"""
    counter = 0
    i = 0

    # loop through 0 to length of txt2 - 1, 
    # compare item with next item, counter counts number of increases.
    while i < len(txt2) - 1:
        if int(txt2[i]) < int(txt2[i + 1]):
            counter += 1
        i += 1
    print(counter)
    return counter

make_counter()

# got 1233


## Day 1 Part 2 ##

