dirs = { 'NW':[0,-1], 'NE':[1,-1], 'SW':[-1,1], 'SE':[0,1],'e':[1,0], 'w':[-1,0] }

def find_adj_tiles(tile):
    return {(tile[0] + dir[0], tile[1] + dir[1]) for dir in dirs.values()}

def get_coord(tile):
    c1 = c2 = 0
    for key, val in dirs.items():
        c1+=tile.count(key)*val[0]
        c2+=tile.count(key)*val[1]
    return (c1, c2)

def p2(stack):
    import time
    t0 = time.time()

    for c, _ in enumerate(range(100), start=1):
        adj = set()
        new_stack = set()

        for tile in stack:
            adj.update( find_adj_tiles(tile) )

        for tile in adj:
            cnt = sum(
                tuple(a + b for a, b in zip(tile, d)) in stack
                for d in dirs.values()
            )

            if (tile in stack and 0 < cnt <= 2) or (
                tile not in stack and cnt == 2
            ):
                new_stack.add(tile)
        stack = new_stack

    print(f'\n{c} \t{len(stack)} \t{time.time()-t0:.1f}')
    return stack

def p1(tiles):
    black = set()
    for tile in tiles:
        coord = get_coord(str(tile))
        if coord in black:
            black.remove(coord)
        else:
            black.add(coord)
    return black

def main(f):
    tiles = [tile.split() for tile in open(f, 'r').read().split('\n')]
    black = p1(tiles)   
    print(f'\nReal input\np1 {len(black)}, p2 {len(p2(black))}\n')

if __name__ == '__main__':   
        main('day24.txt')
