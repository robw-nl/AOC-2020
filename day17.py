# print("Number of cubes after 6 iterations:",len(gd))
 
# At every integer 3-dimensional coordinate (x,y,z), there 
# exists a single cube which is either active or inactive

# 8x8 grid
# 26 cubes (#)

# #.##.##.
# .##..#..
# ....#..#
# .##....#
# #..##...
# .###..#.
# ..#.#..#
# .....#..

# rewrite sometime with 1 function for 3d and 4d

def cubes3d(active):
    for _ in range(6):
        to_check = set()
        next_active = set()

        for x, y, z in active: # current cube
            active_count = 0
            for xo in range(-1, 2):
                for yo in range(-1, 2):
                    for zo in range(-1, 2):
                        if (x+xo, y+yo, z+zo) in active: # active cubes remain active
                            active_count += 1
                        else:
                            to_check.add((x+xo, y+yo, z+zo)) # flag for next round

            if 2 < active_count < 5:
                next_active.add((x, y, z))

        for x, y, z in to_check:  # neighbour cubes
            active_count = 0
            for xo in range(-1, 2):
                for yo in range(-1, 2):
                    for zo in range(-1, 2):
                        if (x+xo, y+yo, z+zo) in active: # turn neighbours active
                            active_count += 1

            if active_count == 3:
                next_active.add((x, y, z))

        active = next_active
    
    return len(active)


def cubes4d(active):
    for _ in range(6):
        to_check = set()
        next_active = set()

        for x, y, z, w in active: # current cube
            active_count = 0
            for xo in range(-1, 2):
                for yo in range(-1, 2):
                    for zo in range(-1, 2):
                        for wo in range(-1, 2):
                            if (x+xo, y+yo, z+zo, w+wo) in active: # active cubes remain active
                                active_count += 1
                            else:
                                to_check.add((x+xo, y+yo, z+zo, w+wo)) # flag for next round

            if 2 < active_count < 5:
                next_active.add((x, y, z, w))

        for x, y, z, w in to_check:  # neighbour cubes
            active_count = 0
            for xo in range(-1, 2):
                for yo in range(-1, 2):
                    for zo in range(-1, 2):
                        for wo in range(-1, 2):
                            if (x+xo, y+yo, z+zo, w+wo) in active: # turn neighbour cubes active?
                                active_count += 1

            if active_count == 3:
                next_active.add((x, y, z, w))

        active = next_active
    
    return len(active)


def main():
    active3d = set()
    active4d = set()

    with open("day17.txt", "r") as file:
        for x, line in enumerate(file.readlines()):
            for y, cube in enumerate(line.strip()):
                if cube == '#':
                    active3d.add((x, y, 0))
                    active4d.add((x, y, 0, 0))

    print(cubes3d(active3d))
    print(cubes4d(active4d))

if __name__ == "__main__":
    main()
