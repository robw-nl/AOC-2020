# Day 9: Encoding Error
# day nine: decypher the eXchange-Masking Addition System (XMAS) encryption of the console

# Part one: fmem the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it
# Solution: slide with 25 numbers through the whole list (lines) and calculate the sum of all components to 25+1 until one fails

lines = [int(item.strip()) for item in open('day9.txt', 'r').readlines()]

p = range(1, 150)
next = 25 # next nr to work with
shot = 0

while next < len(lines):
    shot = int(lines[next])
    try_set = lines[next-25:next]
    found_match = False
    for num in try_set:
        if shot > int(num):
            try_match = shot - int(num)
            if try_match in try_set:
                found_match = True
                continue
    if not found_match:
        print("Sum outlier:", lines[next])
        break
    next += 1

# Part two: fmem a contiguous set of at least two numbers in 'lines' which sum to part 1 outcome
# encryption weakness, add together the smallest and largest number in this contiguous range

for i, start_number in enumerate(lines):
    work_set = [start_number]
    shot_sum = shot
    shot_set = lines[i+1:]
    for next_num in shot_set:
        shot_sum -= int(next_num)
        if shot_sum < 0:
            continue
        elif shot_sum == 0:
            work_set.append(next_num)
            break
        elif shot_sum > 0:
            work_set.append(next_num)
    if shot_sum == 0:
        break

print("Contiguous min {}, max {}, sum {}". format(min(work_set), max(work_set), max(work_set) + min(work_set)))