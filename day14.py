# Day 11: part 1 Seating System. Simulate your seating area by applying the seating
# rules repeatedly until no seats change state. How many seats end up occupied?

lines = open('day14.txt').read().split('\n')
d = {}

def f1(x):
    for i in range(36): # flip the bits
        if mask[36 - 1 - i] == '0':
            x &= (~(1 << i))
        if mask[36 - 1 -  i] == '1':
            x |= (1 << i)
    return x

for line in lines:
    if line.startswith('mask'):
        mask = line[len('mask = '):]
    else:    
        a, b = line.split(' = ')
        a = a[a.find('[')+1: a.find(']')]
        d[a] = f1(int(b))

s = sum(d[key] for key in d)
print(s) 

# Part 2: Execute the initialization program using an emulator for a 'floating bit'
# version 2 decoder chip. What is the sum of all values left in memory after it completes?

d = {}

def f2(x, i):
    if i == 36:
        return [0]
    result = f2(x, i + 1)
    n = len(result)
    results = []
    for y in result:
        if mask[36 - 1 - i] == '0':
            results.append(y | (x & (1 << i)))
        elif mask[36 - 1 - i] == '1':
            results.append(y | (1 << i))
        elif mask[36 - 1 - i] == 'X': # the floating bit
            results.append(y)
            results.append(y | (1 << i))
    return results

for line in lines:
    if line.startswith('mask'):
        mask = line[len('mask = '):]
    else:
        a, b = line.split(' = ')
        a = int(a [a.find('[')+1: a.find(']') ])
        for x in f2(a, 0):
            d[x] = int(b)

s = sum(d[key] for key in d)
print(s)
