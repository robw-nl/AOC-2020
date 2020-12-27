# Day 1: Report Repair
# # Part one: Multiply the two entries that sum to 2020
# Part two: What is the product of the three entries that sum to 2020

from itertools import combinations

l = [int(s.strip()) for s in open("day1.txt")]
s1=s2=''

for a, b, c in combinations(l, 3):
    if s1=='' and a+b==2020:
        s1=("P of {}+{} = {}".format(a, b, a+b))
    if s2=='' and a+b+c==2020: 
        s2 = ("S of {}*{}*{} = {}".format(a, b, c, a*b*c))
print(s1, s2)