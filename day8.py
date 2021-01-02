# Day 8: Handheld Haltin
# part one: fix the infinite loop, determine the accumulator value

lines = open("day8.txt").readlines()

def part1(lines):
    p = range(1, 15)
    acc = line_num = 0
    repeat = set()
    while True:
        if line_num in repeat:
            return False, acc
        line = lines[line_num].strip().split()

        instr = line[0]
        num = int(line[1])
        repeat.add(line_num)
        if instr == 'acc':
            acc += num
        line_num += num if instr == 'jmp' else 1
        if line_num >= len(lines):
            return True, acc


print("Accumalator value:",'\t', part1(lines)[1])


# part two: accumulator value after programm fix

p = range(1, 15)
state = False
value = 0

for mem_exp, line in enumerate(lines):
    if 'acc' in line:
        continue
    if 'nop' in line: # per instruction replace both with each other
        lines[mem_exp] = line.replace('nop', 'jmp')
    else:
        lines[mem_exp] = line.replace('jmp', 'nop')
        state, value = part1(lines)
    if state:
        break
    lines[mem_exp] = line

print("Fixed accumalator value:", value)
