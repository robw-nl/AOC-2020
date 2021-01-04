# Day 16, part 1: What is your ticket scanning error rate?
# RE-WRITE SOMETIME, VERY MESSY NOW

from functools import reduce
import re,operator
from itertools import combinations

all_tickets = []
all_ranges: set = set()
rules_map = {}

def get_ranges(x, y):
    y |= set(range(x[0] , x[1] + 1)) | set(range(x[2] , x[3] + 1))
    return y

for line in open('day16.txt', 'r').read().splitlines():
    if 'or' in line:
        vals = list(map(int, re.findall(r'(\d+)' , line)))
        all_ranges = get_ranges(vals, all_ranges)
        rules_map[line[:line.find(':') ]] = set(range(vals[0], vals[1] + 1)) | set(range(vals[2] , vals[3] + 1))
    elif ',' in line:
        all_tickets.append(list(map(int , line.split(',')))) 

def part1():
    errors=[0, 0]
    for line in all_tickets[1:]:
        for j in line:
            if int(j) not in all_ranges:
                errors[0]+=int(j)
                errors[1]+=1

    return 'Part 1 Error rate: {} other tickets: {} false tickets: {}'.format(errors[0], len(all_tickets[1:]), errors[1])

# part 2: look for the six fields on your ticket that start with the word departure.
# What do you get if you multiply those six values together?

def part2():
    pos = { i : set(rules_map.keys()) for i in range(len(all_tickets[0])) }
    for ticket in all_tickets:
        if any(val not in all_ranges for val in ticket): continue

        for index,val in enumerate(ticket):
            for rule, value__ in rules_map.items():
                if val not in value__: pos[index].remove(rule)

    visited = [False for _ in range(len(pos))]

    for _ in range(len(pos)):
        for index, value_ in pos.items():
            if len(value_) == 1 and not visited[index]:
                visited[index] = True
                target_index = index
                target_field = [e for e in pos[index]][0]
                break

        for index, value in pos.items():
            if index != target_index and target_field in pos[index]:
                value.remove(target_field)

    return 'Part 2 multiplied: {}'.format(reduce(operator.mul, [ all_tickets[0][i] for i in pos if 'departure' in pos[i].pop()]))

def main():
    print(part1())
    print(part2())

main()