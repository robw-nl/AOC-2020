# day 7: the shitty bags containnment problem

bags = {}
for line in open('day7.txt').read().splitlines():
    left_bag, right_bags = line.split(' contain ')
    left_bag = tuple(left_bag.split()[:2])
    bags[left_bag] = []
    if right_bags != 'no other bags.':
        for right_bag in right_bags.split(', '):
            amount, *colors, _ = right_bag.split()
            bags[left_bag].append((int(amount), tuple(colors)))

def part_1(bag_color: tuple) -> bool:
    return any(color == target or part_1(color) for _, color in bags[bag_color]) # use _ as color counter

def part_2(bag_color: tuple) -> int:
    return 1 + sum(cnt * part_2(color) for cnt, color in bags[bag_color])

target = 'shiny', 'gold'

print("Part one: sum parents of\t", sum(map(part_1, bags)))
print("Part two: total inside bags of \t", part_2(target) - 1)
