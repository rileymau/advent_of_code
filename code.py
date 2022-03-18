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

# oxygen, keep most common in that position, or 1 if equal.
# scrubber, keep least common in that position, or 0 if equal.
# life support is decimal of oxygen multiplied by decimal of scrubber.

# from part 1, 0 most common in first postion: 
# gamma =  [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
# epsilon =  [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]

def find_life_support(lst):
    """take day3 list and find oxygen and scrubber numbers, return life support number"""
    oxygen = []
    scrubber = []

    # get oxygen number
    new = []
    for day in lst:
        if day[0] == '0':
            new.append(day)
    #print("new ", new)

    def find_oxygen(new, num):
        """recursive, find oxygen number"""

        # return if on last index
        if num == 11:
            print("final new is ", new[0])
            return(new[0])

        # return if only one number left
        if len(new) == 1:
            print("final new is ", new[0])
            return(new[0])

        zero = 0
        one = 0
        for day in new:
            if day[num] == '0':
                zero += 1
            elif day[num] == '1':
                one += 1
        #print("zero is ", zero)
        #print("one is ", one)

        # get most common number in the spot
        # or 1 if equal
        # make a new list with that number
        if zero > one:  #number of zeros to ones
            new = [x for x in new if x[num] == '0']
        elif one > zero: 
            new = [x for x in new if x[num] == '1']
        elif one == zero:  #number of zeros to ones
            new = [x for x in new if x[num] == '1']

        # repeat until 1 number left or index == 11
        #print("new is ", new)
        return find_oxygen(new, num + 1)

    num = 1
    oxygen = find_oxygen(new, num)
    #print(oxygen)

    # get scrubber number
    def find_scrubber(newS, numS):
        """recursive, find scrubber number"""

        # return if on last index
        if numS == 11:
            print("final new scrubber is ", newS[0])
            return(newS[0])

        # return if only one number left
        if len(newS) == 1:
            print("final new scrubber is ", newS[0])
            return(newS[0])

        zeroS = 0
        oneS = 0
        for day in newS:
            if day[numS] == '0':
                zeroS += 1
            elif day[numS] == '1':
                oneS += 1
        #print("zeroS is ", zeroS)
        #print("oneS is ", oneS)

        # get least common number in the spot
        # or 0 if equal
        # make a new list with that number
        if zeroS < oneS:  
            newS = [x for x in newS if x[numS] == '0']
        elif oneS < zeroS: #number of zeros to ones
            newS = [x for x in newS if x[numS] == '1']
        elif oneS == zeroS:  #number of zeros to ones
            newS = [x for x in newS if x[numS] == '0']

        # repeat until 1 number left or index == 11
        #print("newS is ", newS)
        return find_scrubber(newS, numS + 1)

    numS = 0
    newS = lst
    scrubber = find_scrubber(newS, numS)
    print(scrubber)
    

    #convert oxygen and scrubber to binary
    oxygen = int(oxygen, 2)
    scrubber = int(scrubber, 2)
    print("oxygen, scrubber is ", oxygen, scrubber)

    #caluclate life support and return
    life = oxygen * scrubber
    print("life support is ", life)
    return life

find_life_support(day3)
# got 931, 3618 for oxygen, scrubber
# got life support 3368358


## Day 4 Part 1 ##

print('day 4 pt 1')

#import data
day4 = open('inputBingo.txt')
day4 = day4.read()

#assign list to called numbers
bingo_list = ((day4.split())[0]).split(',')
winning_num = 0
print(bingo_list)

# split boards on empty line or line numbers by 5's
board_list = (day4.splitlines())[2:]

# Make a board dictionary
# boards are matrices 5x5
# boards rows are named b0011, x012, x013, x014, x015 is board 1
def create_dict(lst):
    all_boards = {}
    n = 0
    for i in range(0, int((len(lst) + 1)/6)):
        all_boards[i]=[]
    # while n < len(lst):
    for row in lst:
        if len(all_boards[n]) < 6:
            all_boards[n].append(row)
            pass
        else:
            n = n + 1
            all_boards[n].append(row)
            pass
    
    for key in all_boards:
        if len(all_boards[key]) < 6:
            all_boards[key].append('')
    print(all_boards)
    return all_boards

create_dict(board_list)





# the function needs to call each number one at a time, and keep track of boards scores.
# replace number with number$, and look for $ in each item in each row and column

def bingo_game(all_boards):
    for num in bingo_list:
        for board in all_boards:
            if num in all_boards[board]:
                pass
                #replace num with (num + '$')
        #win_check(all_boards)


def win_check(all_boards):
    for board in all_boards:
        # check each row
        # check each column
        pass

# find bingo card that wins
# sum numbers in row or column
# multiply by winning number

## Day 4 Part 2 ##