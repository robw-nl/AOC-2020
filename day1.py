# Day 1: Report Repair
# # Part one: Multiply the two entries that sum to 2020
# Part two: What is the product of the three entries that sum to 2020

l=[]
for s in open("day1.txt"):
    l.append(int(s.strip()))

p1=p2=0
for a in l:
    for b in l: 
        if p1 == 0 and a+b==2020: p1=a*b; print("P of {}*{}    = {}".format(a, b, p1))
        for c in l:
            if p2 == 0 and a+b+c==2020: p2=a*b*c; print("P of {}*{}*{} = {}".format(a, b, c, p2))