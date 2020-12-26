# Day 15: Rambunctious Recitation
# What will be the 2020th number spoken?


def spoken_num(n):
    spoken=[9,19,1,6,0,5,4]
    spoken={spoken[i]:i+1 for i in range(len(spoken))} # keep track of how often
    a=0
    for i in range(len(spoken)+1,n):
        spoken[a],a = (i, i-spoken[a]) if a in spoken else (i, 0)
    return a

print('part1',spoken_num(2020))
print('part2',spoken_num(30000000))
