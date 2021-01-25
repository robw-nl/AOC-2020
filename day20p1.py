# code inspired byhiggsmass2020 who did exactly what I wanted to do. I
# already built most of the functions, but got stuck with some grid transformations.
# I took a few lines of his work to validate mine, thanks for that ;) P2 is all mine

import itertools as it
import collections as co
import functools as ft
import operator as op


def match_edges10(edge):
    til = co.defaultdict(list)
    # a all pairs of tiles
    for i in it.permutations(edge.keys(), 2):
        # match each pair (rotate if necessary)
        #print ('matching', i)
        for m,u in enumerate(edge[i[0]]):
            for n,v in enumerate(edge[i[1]]):
                ## x = rev(u), y = rev(v)
                ## compare (u,v), (u,y), (v,x) (x,y)
                x, y = u[::-1], v[::-1]
                if (u == v):
                    #print (u,v,m,n, 'uvmn')
                    til[i[0]].append(i[1])
                elif (u == y):
                    #print (u,y,m,-n, 'uym-n')
                    til[i[0]].append(i[1])
                elif (x == v):
                    #print (x,v,-m,n, 'xv-mn')
                    til[i[0]].append(i[1])
                elif (x == y):
                    #print (x,y,-m,-n, 'xy-m-n')
                    til[i[0]].append(i[1])

    ## corners have two tiles adjacent to them. rest have > 2
    return (ft.reduce ( op.mul, [int(a) for a in til if len(til[a]) == 2] ))


def grids10(data, edges10):
    grid10 = []
    for b in data:
        b = b.split()
        if b == []:
            continue

        # build edges: 1st = top bottom, 2nd left, 3rd right
        edge10 = [b [2], b [-1],
            ''.join(b [i] [0] for i in range(2, len(b) )),
            ''.join(b [i] [-1] for i in range(2, len(b) )) ]

        edges10[b[1][:-1]] = edge10
        grid10+=[b]

    return grid10, edges10

def main():
    data = open('day20p1.txt').read().split('\n\n')

    edges10 = co.defaultdict(list)
    edges8 = co.defaultdict(list)
    grid10 = grid8 = []

    grid10, edges10 = grids10(data, edges10)
    print ('part 1:', match_edges10(edges10))

if __name__ == '__main__':   
    main()
