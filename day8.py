# Day 8: Handheld Haltin
# part one: fix the infinite loop, determine the accumulator value

f = open("day8.txt").readlines()

def part1(lines):
    p = range(1, 15); c=0 # print switch
    acc = line_num = 0
    repeat = set()
    while True:
        if line_num in repeat:
            return False, acc
        line = lines[line_num].strip().split()
        
        if c in p: print(line); c+=1 

        instr = line[0]
        num = int(line[1])
        repeat.add(line_num)
        if instr == 'acc':
            acc += num
        if instr == 'jmp':
            line_num += num
        else:
            line_num += 1
        if line_num >= len(lines):
            return True, acc


print("Accumalator value:",'\t', part1(f)[1])


# part two: accumulator value after programm fix

p = range(1, 15); c=0 # print switch
state = False
value = 0

for index, line in enumerate(f):
    if 'acc' in line:
        continue
    if 'nop' in line: # per instruction replace both with each other
        f[index] = line.replace('nop', 'jmp')
    else:
        f[index] = line.replace('jmp', 'nop')
        state, value = part1(f)
    if state:
        break
    else:
        f[index] = line
        if c in p:  c+=1; print(f[index], state, value);

print("Fixed accumalator value:", value)
