directions = [ ['NW',0,-1],['NE',1,-1],['SW',-1,1],['SE',0,1],['e',1,0],['w',-1,0] ]

def find_adj_tiles(stack, tile):
    x = []
    for item in directions:
        x.append([tile[0] + item[1], tile[1] + item[2], tile[2]])
        for t in stack:
            if x[-1][:2] == t[:2]:
                x[-1][2] = t[2]
                break
            else:
                x[-1][2] = False
    return sum(t[2] for t in x), x

def get_coord(tile):
    c1 = c2 = 0
    for item in directions:
        c1+=tile.count(item[0])*item[1]
        c2+=tile.count(item[0])*item[2]

    return [c1, c2, False]

def p2(stack):
    import time
    t0 = time.time()

    for c, _ in enumerate(range(100), start=1):
        to_flip = []

        for tile in stack:
            c_black, adj_tiles = find_adj_tiles(stack, tile)            
            stack.extend([item for item in adj_tiles if tile[2] and item not in stack])

            if tile[2] and (c_black == 0 or c_black > 2) or (not tile[2] and c_black == 2):
                to_flip.append(tile)

        stack.extend([item for item in adj_tiles if tile[2] and item not in stack])
        for tile in stack:
            if tile in to_flip:
                tile[2] = not tile[2]

        print(f'{c} \t{len(stack)} \t{time.time()-t0:.1f}')
    return sum(tile[2] for tile in stack)

def p1(tiles):
    black = []
    stack = []

    for tile in tiles:
        stack += [get_coord(str(tile))]
        black.remove(stack[-1]) if stack[-1] in black else black.append(stack[-1])        

    for tile in stack:
        tile[2] = tile in black
    
    return black

def main(f):
    tiles = [tile.split() for tile in open(f, 'r').read().split('\n')]

    black = p1(tiles)   
    print(f'\np1 {len(black)}, p2 {p2(black)}\n')

if __name__ == '__main__':   
        main('day24.txt')