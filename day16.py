# Day 16, part 1: Consider the validity of the nearby tickets you scanned.# What is your ticket scanning error rate?
import re
from functools import reduce
import time,os,re,operator

all_tickets = []
other_tickets = []
corr_tickets = []
all_ranges = set()
rule_map = {}

for line in open('day16.txt', 'r').read().split('\n'):
    if 'or' in line:
        vals = list(map(int, re.findall(r'(\d+)' , line)))
        all_ranges |= set(range(vals[0] , vals[1] + 1)) | set(range(vals[2] , vals[3] + 1))
        rule_map[line[:line.find(':') ]] = set(range(vals[0] , vals[1] + 1)) | set(range(vals[2] , vals[3] + 1))
    elif ',' in line:
        all_tickets.append(list(map(int , line.split(',')))) 

my_ticket = all_tickets[0]
other_tickets = all_tickets[1:]

is_good=True
error_rate=0
for line in other_tickets:
    for j in line:
        if int(j) not in all_ranges:
            error_rate+=int(j)
            is_good=False
    if is_good: 
        corr_tickets.append(line)
    is_good=True

print('Part 1: Error rate: {} other tickets: {} corr tickets: {}'.format(error_rate, len(other_tickets), len(corr_tickets)))

# part 2: look for the six fields on your ticket that start with the word departure.
# What do you get if you multiply those six values together?

pos = { i : set(rule_map.keys()) for i in range(len(all_tickets[0])) }

for ticket in all_tickets:
    if any(val not in all_ranges for val in ticket): continue

    for idx,val in enumerate(ticket):
        for rule, value__ in rule_map.items():
            if val not in value__: pos[idx].remove(rule)

visited = [False for _ in range(len(pos))]

for _ in range(len(pos)):
    for idx, value_ in pos.items():
        if len(value_) == 1 and not visited[idx]:
            visited[idx] = True
            target_idx = idx
            target_field = [e for e in pos[idx]][0]
            break

    for idx, value in pos.items():
        if idx == target_idx : continue
        if target_field in pos[idx]:
            value.remove(target_field)

print('Part 2 multiplied:', reduce(operator.mul , [ all_tickets[0][i] for i in pos if 'departure' in pos[i].pop()]))