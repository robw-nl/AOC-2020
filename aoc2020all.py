#!/usr/bin/env python
# coding: utf-8

# # --- Day 1: Report Repair ---

# In[1]:


# ------------------------------------------------------------------------------------------------
# Part one: Multiply the two entries that sum to 2020
# Part two: What is the product of the three entries that sum to 2020

l=[]
for s in open("aocday1.txt"):
    l.append(int(s.strip()))

p1=p2=0
for a in l:
    for b in l: 
        if p1 == 0 and a+b==2020: p1=a*b; print("Part one: P of {}*{}    = {}".format(a, b, p1))
        for c in l:
            if p2 == 0 and a+b+c==2020: p2=a*b*c; print("Part two: P of {}*{}*{} = {}".format(a, b, c, p2))


# # --- Day 2: Password Philosophy ---

# In[22]:


# ------------------------------------------------------------------------------------------------
# part one: How many passwords are valid according to policies?
# part two: Check if the assigned characters are in the right position
# in the password. Same file, same data, other rules


col1_2 = []
c1 = c2 = 0
result = 0

for lines in open('aocday2.txt').read().splitlines():
    lines = lines.split(' ')
 
    col1_2 = lines[0].rsplit('-', 1)
    count = lines[2].count(lines[1][0])

    if int(count) >= int(col1_2[0]) and int(count) <= int(col1_2[1]):
        c1+=1

    if len(lines[2]) > int(col1_2[0]):
        if lines[1][0] == lines[2][int(col1_2[0])-1] and lines[1][0] == lines[2][int(col1_2[1])-1]:
            result=result
        elif lines[1][0] == lines[2][int(col1_2[0])-1] or lines[1][0] == lines[2][int(col1_2[1])-1]:
            result+=1
        else:
             result=result
    else:
        result=result
    c2+=1
    
print("Part one: Occurences: {}".format(c1))
print("Part two: All cases: {} Good cases: {}".format(c2, result))    


# # --- Day 3: Password Philosophy ---

# In[4]:


# ------------------------------------------------------------------------------------------------
# Part one

count=0
with open('aocday3.txt') as input:
	grid = [line.rstrip() for line in input]

i = 0
c = 0
for x in grid:
    l = len(x)
    if i >= l:
        i -= l
    if (x[i] == '#'):
        c += 1
    i += 3

print("Trees encountered: {}".format(c))

# Part two

lst = [(1,1), (3,1), (5, 1), (7, 1), (1, 2)]
l = len(grid)

total = 1
for steps in lst:
    i = 0
    n = 0
    c = 0
    while n < l:
        if i >= len(grid[n]):
            i -= len(grid[n])
        if (grid[n][i] == '#'):
            c += 1
        i += steps[0]
        n += steps[1]
    total *= c

print("Number of trees on listed slopes: ", total)


# # --- Day 4: Passport Processing ---

# In[5]:


# ------------------------------------------------------------------------------------------------
# Part one: check correctness passports

with open('aocday4.txt') as f:
    data = f.read().split('\n\n')
    
fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
tot = 0

for p in data:
    check = [f in p for f in fields]
    if all(check):
        tot += 1

print("Correct passports: {}".format(tot))

# Part two: check correctness of passports format
import re
tot = 0

for p in data:
    check = [f in p for f in fields]
    if all(check):
        p = {x.split(':')[0] : x.split(':')[1] for x in re.split('\n| ', p) if ':' in x}

        if ((1920 <= int(p['byr']) <= 2002) and
            (2010 <= int(p['iyr']) <= 2020) and
            (2020 <= int(p['eyr']) <= 2030) and
            (((p['hgt'][-2:] == 'cm') and (150 <= int(p['hgt'][:-2]) <= 193)) or
            ((p['hgt'][-2:] == 'in') and (59 <= int(p['hgt'][:-2]) <= 76))) and
            (p['hcl'][0] == '#' and all([x.isalnum() for x in p['hcl'][1:]])) and
            (p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and
            (len(p['pid']) == 9 and all([x.isdigit() for x in p['pid']]))):
            tot += 1

print("Passports with correct formats: {}".format(tot))


# # --- Day 5: Binary Boarding ---

# In[7]:


# ------------------------------------------------------------------------------------------------
# Part 1: find the highest seat number

with open('aocday5.txt') as f:
    lines = f.read().split('\n')

max_id = 0
seats = []

prt = 0

for line in lines:
    row_low = 0
    row_high = 127 # nr of rows (+1)

    col_low = 0
    col_high = 7 # nr of seats (+1)
    
    for letter in line:
        if letter == "F":
            row_high = (row_high+ row_low) // 2
            if prt==1: print("high: {}".format(row_high))
        if letter == "B":
            row_low = (row_high + row_low) // 2
            if prt==1: print("low: {}".format(row_low))
        if letter == "R":
            col_low = (col_high + col_low) // 2
            if prt==1: print("low: {}".format(row_low))
        if letter == "L":
            col_high = (col_high + col_low) // 2
            if prt==1: print("high: {}".format(col_high))

    seat_id = (row_low + 1) * 8 + col_high
    max_id = max(seat_id, max_id)
    seats.append(seat_id)

print("Highest seat nr: {}".format(max_id))


# part 2: find the id of my seat

sorted_seats = sorted(seats)

if prt==1: print(sorted_searts)

# find seat where only 1 number is missing!
for i in range(1, len(seats)-1):
    if sorted_seats[i+1] != sorted_seats[i] + 1:
        print("My seat nr: {}".format(sorted_seats[i]+1))


# # --- Day 6: Custom Customs ---

# In[8]:


# ------------------------------------------------------------------------------------------------
# Part one: check correctness passports
# First attemps, re-write sometime

with open('aocday6.txt') as f:
    questions = f.read().split('\n')
    
tot = 0
prod = 0
qq=''

for q in questions:
    if len(q) > 0:
        qq = qq + q

    if len(q) == 0:
        
        unique = []
        for char in qq:
            if char not in unique:
                unique.append(char)

        tot+=len(unique)
        qq = ''

print("Total counts: {}".format(tot))

# Part two: for each group count nr of questions that EVERYONE answered yes and sum them
# Took a different approach here

with open("aocday6.txt", "r") as f:
    text = f.read().split("\n\n")
    text = [i.splitlines() for i in text]

#print(text)

res = 0
for group in text:
    main_set = set(group[0])
    for people in group[1:]:
        main_set = main_set.intersection(set(people))

    res += len(main_set)

print("Sum all yes's", res)


# # --- Day 7: Handy Haversacks ---

# In[23]:


# --------------------------------------------------------------------------------
# Part one:
# This is a tricky one. I think either a tree or graph problem. (....) It's a graph problem. Zero experience
# with this so I will to build a 'graph' with a tuple, dict with a list that holds the bags containing other bags

bags = dict()
p=1 # print switch

for line in open('aocday7.txt').read().splitlines():
    left_bag, right_bags = line.split(' contain ')
    
    if p in range(10): print(left_bag, right_bags);
        
    left_bag = tuple(left_bag.split()[:2])
    if p in range(10): print(left_bag)
    
    bags[left_bag] = list()
    if right_bags != 'no other bags.':
        for right_bag in right_bags.split(', '):
            amount, *colors, _ = right_bag.split()
            bags[left_bag].append((int(amount), tuple(colors)))
            
    if p in range(10): print(bags[left_bag], amount, '\n');  p+=1
        
        
def part_1(bag_color: tuple) -> bool:
    return any(color == target or part_1(color) for _, color in bags[bag_color]) # use _ as color counter

def part_2(bag_color: tuple) -> int:
    return 1 + sum(cnt * part_2(color) for cnt, color in bags[bag_color])


target = 'shiny', 'gold'

print("Part one: sum parents of\t", sum(map(part_1, bags)))
print("Part two: total inside bags of \t", part_2(target) - 1)


# # --- Day 8: Handheld Halting ---

# In[13]:


# ------------------------------------------------------------------------------------------------
# part one: fix the infinite loop, determine the accumulator value

f = open("aocday8.txt").readlines()

def part1(lines):
    p = range(1, 15); c=0 # print switch
    acc = 0
    line_num = 0
    repeat = set()
    while True:
        if line_num in repeat:
            return False, acc
        line = lines[line_num].strip().split()
        
        if c in p: print(line); c+=1 

        instr = line[0]
        num = int(line[1])
        repeat.add(line_num)
        if instr == 'acc':
            acc += num
        if instr == 'jmp':
            line_num += num
        else:
            line_num += 1
        if line_num >= len(lines):
            return True, acc


print("Accumalator value:",'\t', part1(f)[1])


# part two: accumulator value after programm fix

p = range(1, 15); c=0 # print switch
state = False
value = 0

for index, line in enumerate(f):
    if 'acc' in line:
        continue
    if 'nop' in line: # per instruction replace both with each other
        f[index] = line.replace('nop', 'jmp')
    else:
        f[index] = line.replace('jmp', 'nop')
        state, value = part1(f)
    if state:
        break
    else:
        f[index] = line
        if c in p:  c+=1; print(f[index], state, value);

print("Fixed accumalator value:", value)


# # --- Day 9: Encoding Error ---

# In[24]:


# ------------------------------------------------------------------------------------------------
# day nine: decypher the eXchange-Masking Addition System (XMAS) encryption of the console

# Part one: find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it
# Solution: slide with 25 numbers through the whole list (lines) and calculate the sum of all components to 25+1 until one fails

file = open('aocday9.txt', 'r')
lines = file.readlines()

#print(lines)
lines = [int(item.strip()) for item in lines] # remove all '\n' and conv to int

p = range(1, 150); c=0 # print switch    
next = 25 # next nr to work with
shot = 0

while next < len(lines):
    shot = lines[next]
    try_set = lines[next-25:next]
    found_match = False
    if c in p: print(try_set, '\n'); c+=1
    for num in try_set:
        if shot > num:
            try_match = shot - num
            if c in p: print(shot, num, try_match, '\n');
            if try_match in try_set:
                found_match = True
                continue
    if found_match is False:
        print("Sum outlier: %d" % lines[next])
        break
    next += 1

# Part two: find a contiguous set of at least two numbers in 'lines' which sum to part 1 outcome
# encryption weakness, add together the smallest and largest number in this contiguous range

work_set = []
for i, start_number in enumerate(lines):
    work_set = [start_number]
    shot_sum = shot
    shot_set = lines[i+1:]
    for next_num in shot_set:
        shot_sum -= next_num
        if shot_sum < 0:
            continue
        elif shot_sum == 0:
            work_set.append(next_num)
            break
        elif shot_sum > 0:
            work_set.append(next_num)
    if shot_sum == 0:
        break

print("Contiguous min {}, max {}, sum {}". format(min(work_set), max(work_set), max(work_set) + min(work_set)))


# # --- Day 10: Adapter Array ---

# In[16]:


# ------------------------------------------------------------------------------------------------
# day ten: What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

with open("aocday10.txt","r") as f:
    lines = [int(item.strip()) for item in f]

lines += [0, max(lines) + 3] # add the missing 0 and last number + 3
lines.sort()

c=c1=c3=0
for i in range( (len(lines)-1), -1, -1): # count back
    c=lines[i] - lines[i-1]
    if c == 1: c1+=1
    if c == 3: c3+=1

print('Method one - product of 1 and 3 differences:', c1*c3)

# I saw how to do it better after having solved it:
res = [lines[n] - lines[n - 1] for n in range(1, len(lines))]
print('Method two - product of 1 and 3 counts:', res.count(1) * res .count(3))


# day two: What is the number of distinct ways you can arrange the adapters to connect the charging outlet to your device?

p = range(1, 50); c=0 # print switch   
combinations = [1] * len(lines)

for i in range(1, len(lines)):
    combinations[i] = combinations[i - 1]
    if c in p: print('ONE', i, combinations[i], '\n'); c+=1
    if i > 1 and lines[i] - lines[i - 2] <= 3:
        combinations[i] += combinations[i - 2]
        if c in p: print('TWO', i, combinations[i], '\n'); c+=1
    if i > 2 and lines[i] - lines[ i - 3] <= 3:
        combinations[i] += combinations[i - 3]
        if c in p: print('THREE', i, combinations[i], '\n'); c+=1
    
print("Product of all adaptor combinations: ", combinations[-1])


# # --- Day 11: Seating System ---

# In[25]:


# ------------------------------------------------------------------------------------------------
with open("aocday11.txt","r") as f:
    lines = [item.strip() for item in f]
    
# for i in range(20): print(lines[i])
print(' Do this one later')


# # --- Day 12: Rain Risk ---

# In[27]:


# --------------------------------------------------------------------------------
# # Day one: Calculate Manhattan distance between starting and end position
# The Man.dist between two vectors is = to the one-norm of the distance between the vectors

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.

lines = [[f.strip()[0], int(f.strip()[1:])] for f in open('aocday12.txt', 'r')]

# for i in range(10): print(lines[i])
# print('\n')

dist = {'E':0, 'S':0, 'W': 0, 'N':0}
dirs = 'ESWN'
curr_dir = dirs[0]

p = range(1, 50); c=0 # print switch 
q = range(1, 50); c=0 # print switch 

def change_dir(turn: str, angle: int):
    if turn == 'L':
        if c in p: print('change_dir: L: ', angle, -angle//90)
        return -angle//90 # - reverse direction; use the remainder as value to move (1)
    if turn == 'R':
        if c in p: print('change_dir: R: ', angle, angle//90)
        return angle//90

for instr in lines:
    if c in q: print('for instr in lines', instr)
    if instr[0] in ['L', 'R']:
        curr_dir = dirs[(dirs.find(curr_dir) + change_dir(instr[0],instr[1]))%4]
        if c in q: print('for Left: ', curr_dir)
    elif instr[0] == 'F':
        dist[curr_dir] += instr[1]
        if c in q: print('for Forward: ', dist[curr_dir])
    else:
        dist[instr[0]] += instr[1]
        if c in q: print('for else N: ', dist[instr[0]])


# calculate manhattan distance between 2 vectors with abs()
print('N', dist['N'], 'S', dist['S'], 'E', dist['E'], 'W', dist['W'])
print("Manhattan distance = ", abs(dist['N'] - dist['S']) + abs(dist['E'] - dist['W']))
