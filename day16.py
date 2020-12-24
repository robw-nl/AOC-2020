# Day 16, part 1: Consider the validity of the nearby tickets you scanned.
# What is your ticket scanning error rate?

import re

other_tickets = []
all_ranges = set()
cF=tF=0

for line in open('day16b.txt', 'r').read().split('\n'):
    if 'or' in line:
        vals = list(map(int, re.findall(r'(\d+)' , line)))
        all_ranges |= set(range(vals[0] , vals[1] + 1)) | set(range(vals[2] , vals[3] + 1))
    
    elif ',' in line : other_tickets.append(list(map(int , line.split(',')))) 

my_ticket = other_tickets[0]
other_tickets = other_tickets[1:]

for i in other_tickets:
    for j in i:
        if j not in all_ranges:
            cF+=j
            tF+=1

print('Nr', tF,'Sum', cF)

