"""advent of code"""

## Day 1 Part 1 ##

#from https://adventofcode.com/2021/day/1/input
#get data

# open file and read
txt = open('input.txt')
txt = txt.read()

# make list of data
txt2 = txt.strip().split()
txt3 = [int(x) for x in txt2]
#print(txt3)

def make_counter(lst):
    """count increases line to line in input.txt"""
    counter = 0
    i = 0

    # loop through 0 to length of txt2 - 1,
    # compare item with next item, counter counts number of increases.
    while i < (len(lst) - 1):
        if lst[i] < lst[i + 1]:
            counter += 1
        i += 1
    print(counter)
    return counter

make_counter(txt3)

# got 1233


## Day 1 Part 2 ##

# make new list of triples
# append first item, first + second item, - don't need
# then all triples until end
# append last + second to last, last - don't need

triples = []
# triples.append(txt3[0])
# triples.append(txt3[0] + txt3[1])

j = 0
while j < (len(txt3) - 2):
    triples.append(txt3[j] + txt3[j + 1] + txt3[j + 2])
    j += 1

# triples.append(txt3[-2] + txt3[-1])
# triples.append(txt3[-1])
print(triples)

# update make_counter function to take a lst
# check list for increeases as in part 1

make_counter(triples)

# got 1275


## Day 2 Part 1 ##

# open file and read
moves = open('moves.txt')
moves = moves.read()

# make list of data
moves = moves.strip().split()
print(moves)

def count_moves(move_list):
    """takes list of moves and returns total depth * horiontal moves"""
    depth = 0
    horizontal = 0

    # check if word is forward, up, down (f, u, d)
    #if it is forward, add number to horizontal
    for k, item in enumerate(move_list):
        if k % 2 == 0:
            if item == 'forward':
                horizontal += int(move_list[k + 1])
                # will not go out of range, will always have number after last diretion
            
    # if it is up or down, add/subtract number to depth
    # depth is a positive number going down
            if item == 'up':
                depth -= int(move_list[k + 1])
            if item == 'down':
                depth += int(move_list[k + 1])
    print(horizontal)
    print(depth)
    print(depth * horizontal)
    return(depth * horizontal)

count_moves(moves)
# got 1427868


## Day 2 Part 2 ##
