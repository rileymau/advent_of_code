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
    #print(counter)
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
#print(triples)

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
#print(moves)

def count_moves(move_list):
    """takes list of moves and returns total depth * horiontal moves"""
    depth = 0
    horizontal = 0

    # check if word is forward, up, down (f, u, d)
    # if it is forward, add number to horizontal
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
    #print(horizontal)
    #print(depth)
    #print(depth * horizontal)
    return depth * horizontal

count_moves(moves)
# got 1427868


## Day 2 Part 2 ##

def count_aim(move_list):
    """takes list of moves and returns total depth * horiontal moves"""
    depth = 0
    horizontal = 0
    aim = 0

    # check if word is forward, up, down (f, u, d)
    # if it is forward, add number to horizontal
    # fwd increases depth by aim * x
    for k, item in enumerate(move_list):
        if k % 2 == 0:
            num = int(move_list[k + 1])
            if item == 'forward':
                horizontal += num
                depth += (aim * num)

    # if it is up or down, add/subtract number to depth
    # depth is a positive number going down
    # down increases aim by x
    # up decreases aim by x
            if item == 'up':
                #depth -= num
                aim -= num
            if item == 'down':
                #depth += num
                aim += num
    #print(horizontal)
    #print(depth)
    #print(depth * horizontal)
    return depth * horizontal

count_aim(moves)
# got 1568138742, right answer
# 1569566610 too high
# 1566710874 too low


## Day 3 Part 1 ##

# open file and read
day3 = open('input_d3')
day3 = day3.read()

# make list of data
day3 = day3.strip().split()
#print(day3)


def find_gamma(lst):
    """find gamma and epsilon for power consumption"""
    gamma = []
    epsilon = []
    zeros = [0] * 12
    ones = [0] * 12

    #count zeros and ones for each digit and append to gamma or epsilon
    for day in lst:
        #print(day)
        for i, num in enumerate(day): 
            if num == '0':
                zeros[i] += 1
            elif num == '1':
                ones[i] += 1
    print("0's = ", zeros)
    print("1's = ", ones)

    # if ones higher, gamma gets 1 and epsilon gets 0
    # otherwise, opposite
    for i in range(12):
        if zeros[i] > ones[i]:
            epsilon.append(1)
            gamma.append(0)
        elif ones[i] > zeros[i]:
            gamma.append(1)
            epsilon.append(0)
    print("gamma = ", gamma)
    print("epsilon = ", epsilon)

    #convert gamma and epsilon from binary
    gamma1 = "".join([str(x) for x in gamma])
    print(gamma1)
    epsilon1 = "".join([str(x) for x in epsilon])
    print(epsilon1)
    gamma2 = int(gamma1, 2)
    epsilon2 = int(epsilon1, 2)
    print(gamma2, epsilon2)

    #caluclate power and return
    power = gamma2 * epsilon2
    print("power consumption is ", power)
    return power

find_gamma(day3)
# got 942, 3152 for gamma, epsilon
# got power 2972336


## Day 3 Part 2 ##