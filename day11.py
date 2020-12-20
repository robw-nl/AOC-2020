# Day 11: Seating System. Simulate your seating area by applying the seating
# rules repeatedly until no seats change state. How many seats end up occupied?

with open('/home/rob/Notebooks/AOC2020/day11.txt') as fh:
    empty_chart_text = fh.read()
    
def text2chart(txt):
    D = {}
    for i, row in enumerate(txt.split()):
        for  j, val in enumerate(row):
            D[complex(i, j)] = val
    return D

def run_till_stabilized(part, chart):
    if part == 1:
        nc = nextchart(chart)
        while nc != chart:
            chart, nc = nc, nextchart(nc)
    else:
        nc = nextchart2(chart)
        while nc != chart:
            chart, nc = nc, nextchart2(nc)
    return nc

# Part 1

def changeseat(chart, seatkey):
    seat = chart[seatkey]
    if seat == '.':
        return seat
    occupied = sum(
        chart.get(seatkey + drxn) == '#'
        for drxn in [-1, -1 + 1j, 1j, 1 + 1j, 1, 1 - 1j, -1j, -1 - 1j]
    )

    if seat == 'L' and occupied == 0:
        return '#'
    if seat == '#' and occupied > 3:
        return 'L'
    return seat

def nextchart(chart):
    return {key: changeseat(chart, key) for key in chart}

def count_occupied(chart):
    return [list(chart.values()).count('#')]

# Part 2: given the new visibility method and rule change for occupied
# seats becoming # empty, how many seats end up occupied?

def changeseat2(chart, seatkey):
    seat = chart[seatkey]
    if seat == '.':
        return seat
    occupied = 0
    for drxn in [-1, -1+1j, 1j, 1+1j, 1, 1-1j, -1j, -1-1j]:
        neighbor = '.'
        scale = 0
        while neighbor == '.':
            scale += 1
            neighbor = chart.get((scale * drxn) + seatkey)
        if neighbor == '#':
            occupied += 1
    if seat == 'L' and occupied == 0:
        return '#'
    if seat == '#' and occupied > 4:
        return 'L'
    return seat

def nextchart2(chart):
    return {key: changeseat2(chart, key) for key in chart}


empty_chart = text2chart(empty_chart_text)
stabilized = run_till_stabilized(1, empty_chart)
part_1 = count_occupied(stabilized)

#print(stabilized)
print(part_1, '\n')

stabilized2 = run_till_stabilized(2, empty_chart)
part_2 = count_occupied(stabilized2)

#print(stabilized2)
print(part_2)