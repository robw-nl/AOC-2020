# Day 7: Handy Haversacks
# Part one:
# This is a tricky one. I think either a tree or graph problem. (....) It's a graph problem. Zero experience
# with this so I will to build a 'graph' with a tuple, dict with a list that holds the bags containing other bags

bags = dict()
p=0 # print switch & counter

for line in open('day7.txt').read().splitlines():
    left_bag, right_bags = line.split(' contain ')
    
    if p in range(1,10): print(left_bag, right_bags);
        
    left_bag = tuple(left_bag.split()[:2])
    if p in range(1,10): print(left_bag)
    
    bags[left_bag] = list()
    if right_bags != 'no other bags.':
        for right_bag in right_bags.split(', '):
            amount, *colors, _ = right_bag.split()
            bags[left_bag].append((int(amount), tuple(colors)))
            
    if p in range(1,10): print(bags[left_bag], amount, '\n');  p+=1
        
        
def part_1(bag_color: tuple) -> bool:
    return any(color == target or part_1(color) for _, color in bags[bag_color]) # use _ as color counter

def part_2(bag_color: tuple) -> int:
    return 1 + sum(cnt * part_2(color) for cnt, color in bags[bag_color])


target = 'shiny', 'gold'

print("Part one: sum parents of\t", sum(map(part_1, bags)))
print("Part two: total inside bags of \t", part_2(target) - 1)
