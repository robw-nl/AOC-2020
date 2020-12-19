# Day 3: Toboggan Trajectory
# Part one

with open('day3.txt') as input:
	grid = [line.rstrip() for line in input]

i = c = count = 0
for x in grid:
    l = len(x)
    if i >= l:
        i -= l
    if (x[i] == '#'):
        c += 1
    i += 3

print('Trees encountered: ', '\t', c)

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

print("Trees on listed slopes: ", total)