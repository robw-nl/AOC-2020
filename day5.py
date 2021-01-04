# Day 5: Binary Boarding part 1: What is the highest seat ID on a boarding pass?
with open('day5.txt') as f:
    lines = f.read().split('\n')

max_id = 0
seats = []

for line in lines:
    row_low = 0
    row_high = 127 # nr of rows +1

    col_low = 0
    col_high = 7 # nr of seats +1
    
    for letter in line:
        if letter == "F":
            row_high = (row_high+ row_low) // 2
        if letter == "B":
            row_low = (row_high + row_low) // 2
        if letter == "R":
            col_low = (col_high + col_low) // 2
        if letter == "L":
            col_high = (col_high + col_low) // 2

    seat_id = (row_low + 1) * 8 + col_high
    max_id = max(seat_id, max_id)
    seats.append(seat_id)

print("Highest seat nr: {}".format(max_id))

# part 2: What is the ID of your seat?
sorted_seats = sorted(seats)

for i in range(1, len(seats)-1):
    if sorted_seats[i+1] != sorted_seats[i] + 1:
        print("My seat nr: {}".format(sorted_seats[i]+1))