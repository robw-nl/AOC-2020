# Day 10: Adapter Array
# day ten: What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

with open("day10.txt","r") as f:
    lines = [int(item.strip()) for item in f]

lines += [0, max(lines) + 3] # add the missing 0 and last number + 3
lines.sort()

c = c1 = c3 = 0
for i in range( (len(lines)-1), -1, -1): # count back
    c=lines[i] - lines[i-1]
    if c == 1: c1+=1
    if c == 3: c3+=1

print('Method one - product of 1 and 3 differences:', c1*c3)

# I saw how to do it better after having solved it:
res = [lines[n] - lines[n - 1] for n in range(1, len(lines))]
print('Method two - product of 1 and 3 counts:', res.count(1) * res .count(3))


# day two: What is the number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
 
p = range(1, 50); c=0 # print switch   
combinations = [1] * len(lines)

for i in range(1, len(lines)):
    combinations[i] = combinations[i - 1]
    if c in p: print('ONE', i, combinations[i], '\n'); c+=1
    if i > 1 and lines[i] - lines[i - 2] <= 3:
        combinations[i] += combinations[i - 2]
        if c in p: print('TWO', i, combinations[i], '\n'); c+=1
    if i > 2 and lines[i] - lines[ i - 3] <= 3:
        combinations[i] += combinations[i - 3]
        if c in p: print('THREE', i, combinations[i], '\n'); c+=1
    
print("Product of all adaptor combinations: ", combinations[-1])