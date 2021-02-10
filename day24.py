def get_adj_tiles(coord_stack):

    coordinates = [ ['nw',-1,1],['ne',1,1],['sw',-1,-1],['se',1,-1],['e',2,0],['w',-2,0] ]
    coord = []
    for i, item in enumerate(coordinates):
        coord.append( [item[0], coord_stack[i][0]+item[1], coord_stack[i][1]+item[2]] )
    return coord

def p2(coord_stack):
    x = get_adj_tiles(coord_stack)
    # do stuff with x and black

    return x

def p1(f):
    black = set()
    coord = (0, 0)
    coord_stack = []
    
    for line in [line.split() for line in open(f, 'r').read().split('\n')]:
        line = str(line)

        nw = [line.count('nw') * -1, line.count('nw') * +1]
        ne = [line.count('ne') * +1, line.count('ne') * +1]
        sw = [line.count('sw') * -1, line.count('sw') * -1]
        se = [line.count('se') * +1, line.count('se') * -1]
        e  = [(line.count('e')-ne[0]-se[0]) * 2, 0]
        w  = [(line.count('w')-abs(nw[0])-abs(sw[0])) * -2, 0]

        coord =(nw[0]+ne[0]+sw[0]+se[0]+e[0]+w[0]),(nw[1]+ne[1]+sw[1]+se[1]+e[1]+w[1]) 
        black.remove(coord) if coord in black else black.add(coord)
        coord_stack+=[coord]
    
    return len(black), coord_stack

def main(f):
    x, coord_stack = p1(f)
    y = p2(coord_stack)
    print(f'\np1 {x}, p2 {y}\n')

if __name__ == '__main__':   
        main('day24.txt')