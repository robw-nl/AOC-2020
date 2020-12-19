# Day 9: Encoding Error
# day nine: decypher the eXchange-Masking Addition System (XMAS) encryption of the console

# Part one: find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it
# Solution: slide with 25 numbers through the whole list (lines) and calculate the sum of all components to 25+1 until one fails

file = open('day9.txt', 'r')
lines = file.readlines()

#print(lines)
lines = [int(item.strip()) for item in lines] # remove all '\n' and conv to int

p = range(1, 150); c=0 # print switch    
next = 25 # next nr to work with
shot = 0

while next < len(lines):
    shot = lines[next]
    try_set = lines[next-25:next]
    found_match = False
    if c in p: print(try_set, '\n'); c+=1
    for num in try_set:
        if shot > num:
            try_match = shot - num
            if c in p: print(shot, num, try_match, '\n');
            if try_match in try_set:
                found_match = True
                continue
    if found_match is False:
        print("Sum outlier: %d" % lines[next])
        break
    next += 1

# Part two: find a contiguous set of at least two numbers in 'lines' which sum to part 1 outcome
# encryption weakness, add together the smallest and largest number in this contiguous range

work_set = []
for i, start_number in enumerate(lines):
    work_set = [start_number]
    shot_sum = shot
    shot_set = lines[i+1:]
    for next_num in shot_set:
        shot_sum -= next_num
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