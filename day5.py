# Day 5: Binary Boarding
# Part 1: find the highest seat number

with open('day5.txt') as f:
    lines = f.read().split('\n')

max_id = 0
seats = []

prt = 0

for line in lines:
    row_low = 0
    row_high = 127 # nr of rows +1

    col_low = 0
    col_high = 7 # nr of seats +1
    
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