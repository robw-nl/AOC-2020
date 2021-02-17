directions = [ [0,-1, 'NW'],[1,-1, 'NE'],[-1,1, 'SW'],[0,1, 'SE'],[1,0, 'e'],[-1,0, 'w'] ]

def add_adj_tiles(stack, tile):
    adj = [[tile[0] + item[0], tile[1] + item[1], tile[2]] for item in directions]
    adj.sort()
    stack.sort()
    cnt=0
    for a in adj:
        a[2] = False
        for s in stack:
            if a[:2] == s[:2]:
                a[2] = s[2]
                break               
        cnt += a[2]
        if tile[2] and a not in stack:
            stack.insert(0, a)
    return cnt

def get_coord(tile):
    c1 = c2 = 0
    for item in directions:
        c1+=tile.count(item[2])*item[0]
        c2+=tile.count(item[2])*item[1]
    return [c1, c2, True]

def p2(stack):
    import time
    t0 = time.time()
    for c, _ in enumerate(range(100), start=1):
        to_flip = []
        for tile in stack:            
            cnt = add_adj_tiles(stack, tile)             
            if tile[2] and (cnt == 0 or cnt > 2) or (not tile[2] and cnt == 2):
                to_flip.append(tile)
        
        to_flip.sort()
        stack.sort()
        for tile in to_flip:
            if tile in stack:
                tile[2] = not tile[2]
         
        print(f'{c} \t{len(stack)} \t{time.time()-t0:.1f}')
    return sum(tile[2] for tile in stack)

def p1(tiles):
    black = []
    for tile in tiles:
        x = get_coord(str(tile))
        black.remove(x) if x in black else black.append(x)
    return black

def main(f):
    tiles = [tile.split() for tile in open(f, 'r').read().split('\n')]
    black = p1(tiles)   
    print(f'\np1 {len(black)}, p2 {p2(black)}\n')

if __name__ == '__main__':   
        main('day24ex.txt')
