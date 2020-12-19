# Day 12: Rain Risk
# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.
# Part one: Calculate Manhattan distance between starting and end position
# The Manhattan distance between two vectors is equal to the one-norm of the distance between the vectors

axes = [ [1,0], [0,-1], [-1,0], [0,1] ]
curr_pos = [0, 0]
direction = 0
ship_ew = 0
ship_ns = 0
way_ew = 10
way_ns = 1


# need to rewrite sometime but now it works at least *** 

for line in open('day12.txt').read().splitlines():

    instr = line[0]
    val = int(line[1:])

# Part one: Calculate Manhattan distance between starting and end position

    if instr == 'N':
        curr_pos[1] += val
    elif instr == 'S':
        curr_pos[1] -= val
    elif instr == 'E':
        curr_pos[0] += val
    elif instr == 'W':
        curr_pos[0] -= val
    elif instr == 'F':
        curr_pos[0] += (val * axes[direction][0])
        curr_pos[1] += (val * axes[direction][1])
    else:
        if instr == 'R':
            direction += (val // 90)
        else:
            direction -= (val // 90)
        direction %= 4

# Part two: Where do the new navigation instructions lead and what is
# the Manhattan distance between that location and the starting position?

    if instr in {'N', 'S', 'E', 'W'}:
        way_ew -= val
    elif instr == 'F':
        ship_ns += (way_ns * val)
        ship_ew += (way_ew * val) 

    elif instr == 'L' and val == 90 or instr == 'R' and val == 270:
        way_ns, way_ew = way_ew, -way_ns
    elif instr == 'L' and val == 270 or instr == 'R' and val ==90:
        way_ns, way_ew = -way_ew, way_ns
    elif instr == 'L' and val == 180 or instr == 'R' and val == 180:
        way_ns = -way_ns
        way_ew = -way_ew

print('Manhattan distance 1:', abs(curr_pos[0]) + abs(curr_pos[1]))
print('Manhattan Distance 2:', abs(ship_ns) + abs(ship_ew))