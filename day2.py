# Day 2: Password Philosophy
# part one: How many passwords are valid according to policies?
# part two: Check if the assigned characters are in the right position
# in the password. Same file, same data, other rules

col1_2 = []
c1 = c2 = 0
result = 0

for lines in open('day2.txt').read().splitlines():
    lines = lines.split(' ')
 
    col1_2 = lines[0].rsplit('-', 1)
    count = lines[2].count(lines[1][0])

    if int(count) >= int(col1_2[0]) and int(count) <= int(col1_2[1]):
        c1+=1

    if len(lines[2]) > int(col1_2[0]):
        if lines[1][0] == lines[2][int(col1_2[0])-1] and lines[1][0] == lines[2][int(col1_2[1])-1]:
            result=result
        elif lines[1][0] == lines[2][int(col1_2[0])-1] or lines[1][0] == lines[2][int(col1_2[1])-1]:
            result+=1
        else:
             result=result
    else:
        result=result
    c2+=1
    
print("Part one: Occurences: {}".format(c1))
print("Part two: All cases: {} Good cases: {}".format(c2, result))    