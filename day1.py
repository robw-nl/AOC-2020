# Day 1: Report Repair
# # Part one: Multiply the two entries that sum to 2020
# Part two: What is the product of the three entries that sum to 2020

from itertools import combinations

l = [int(s.strip()) for s in open("day1.txt")]
go = [True, True]

for a, b, c in combinations(l, 3):
    if go[0] and a+b==2020:
        print("P of {}+{} = {}".format(a, b, a+b))
        go[0]=False
    if go[1] and a+b+c==2020: 
        print("S of {}*{}*{} = {}".format(a, b, c, a*b*c))
        go[1]=False
    

