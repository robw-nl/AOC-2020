# Day 11: Seating System
# day one: Simulate your seating area by applying the seating rules repeatedly
# until no seats change state. How many seats end up occupied?

with open("day11.txt","r") as file:
    lines = file.readlines()
    lines = [ list(line.strip()) for line in lines ]

print(lines, '\n') 

line = [ list(line.strip()) for line in open('day11.txt').readlines() ]

print(line) 

# day one: Simulate your seating area by applying the seating rules repeatedly
# until no seats change state. How many seats end up occupied?

line = [ list(line.strip()) for line in open('day11.txt').readlines() ]
for i in range(len(line)):
    print(line[i])