# Day 21: Allergen Assessment
def main(filename: str) -> None:
    allergens_map = {}
    safe_map = {}

    for line in [line.strip(')\n') for line in open(filename).readlines()]:
        ingredients, allergens = line.split("(contains ")
    
        for ingredient in ingredients.split():
            safe_map[ingredient] = safe_map.get(ingredient, 0) + 1
    
        for allergen in allergens.split(', '):
            if allergen not in allergens_map:
                allergens_map[allergen] = set(ingredients.split())
            else:
                allergens_map[allergen] = allergens_map[allergen].intersection(set(ingredients.split()))

    for possible in (possible for allergen in allergens_map for possible in allergens_map[allergen]):
        if possible in safe_map:
            del safe_map[possible]

    print(f"\nPart 1: {sum(safe_map.values())}")

    while False in [len(x) == 1 for x in allergens_map.values()]:
        for a1 in [a for a in allergens_map if len(allergens_map[a]) == 1]:
            for a2 in [a for a in allergens_map if len(allergens_map[a]) > 1]:
                allergens_map[a2] = allergens_map[a2].difference(allergens_map[a1])

    print(
        "Part 2 answer:",
        ','.join( list(allergens_map[allergen])[0]
            for allergen in sorted(allergens_map.keys())), '\n',
    )


if __name__ == "__main__":
    main("day21.txt")