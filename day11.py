# Day 11: Seating System. Simulate your seating area by applying the seating
# rules repeatedly until no seats change state. How many seats end up occupied?

def part1():
    with open("day11.txt", "r") as file:
        data = file.read()
    data = data.split("\n")

    old_layout = {}
    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            old_layout[i, j] = seat

    layout = {}
    while True:
        for (row, col), seat in old_layout.items():
            if seat == "#":
                neighbors = ""
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == j == 0:
                            continue
                        neighbors += old_layout.get((row - i, col - j), ".")
                occupied = neighbors.count("#")

                if occupied >= 4:
                    layout[row, col] = "L"

            elif seat == ".":
                layout[row, col] = "."
            elif seat == "L":
                neighbors = ""
                for i in range(-1, 2):
                    for j in range(-1,2):
                        if i == j == 0:
                            continue
                        neighbors += old_layout.get((row-i, col-j), ".")
                occupied = neighbors.count("#")

                if not occupied:
                    layout[row, col] = "#"

        if layout == old_layout:
            break
        old_layout = {key: value for key, value in layout.items()}

    return list(layout.values()).count("#")

print(part1())


# Given the new visibility method and rule change for occupied
# seats becoming # empty, how many seats end up occupied?

def part2():
    with open("day11.txt", "r") as file:
        data = file.read()
    data = data.split("\n")
 
    old_layout = {}
    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            old_layout[i, j] = seat
 
    def is_occupied(r, c, direction):
        while True:
            r = r + direction[0]
            c = c + direction[1]
 
            try:
                if old_layout[r, c] == "#":
                    return 1
                elif old_layout[r, c] == "L":
                    return 0
            except KeyError:
                return 0
 
    layout = {}
    while True:
        for (row, col), seat in old_layout.items():
            if seat == ".":
                layout[row, col] = "."
            elif seat == "L":
                occupied = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == j == 0:
                            continue
                        occupied += is_occupied(row, col, (i, j))
 
                if not occupied:
                    layout[row, col] = "#"
 
            elif seat == "#":
                occupied = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == j == 0:
                            continue
                        occupied += is_occupied(row, col, (i, j))
 
                if occupied >= 5:
                    layout[row, col] = "L"
 
        if layout == old_layout:
            break
        old_layout = {key: value for key, value in layout.items()}
 
    count = 0
    for v in layout.values():
        if v == "#":
            count += 1
 
    return count

print(part2())
