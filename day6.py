# Day 6: Custom Customs
# Part one: check correctness passports
# First attemps, re-write sometime

with open('day6.txt') as f:
    questions = f.read().split('\n')
    
tot = prod = 0
qq=''

for q in questions:
    if len(q) > 0:
        qq = qq + q

    if len(q) == 0:
        
        unique = []
        for char in qq:
            if char not in unique:
                unique.append(char)

        tot+=len(unique)
        qq = ''

print("Total counts: {}".format(tot))

# Part two: for each group count nr of questions that EVERYONE answered yes and sum them
# Took a different approach here

with open("aocday6.txt", "r") as f:
    text = f.read().split("\n\n")
    text = [i.splitlines() for i in text]

#print(text)

res = 0
for group in text:
    main_set = set(group[0])
    for people in group[1:]:
        main_set = main_set.intersection(set(people))

    res += len(main_set)

print("Sum all yes's", res)