import time
def game1(cups, r):
    t0 = time.time()
    for i in range(r):
        t1 = time.time()
        dest = cups[0] - 1
        out = cups[1:4]

        if dest == 0: # loop
            dest = len(cups)

        while dest in cups[1:4]:
            dest -= 1
            if dest == 0: # loop
                dest = len(cups)

        dest_idx = cups.index(dest)-3
        cups[:dest_idx+1] = sum([cups[:1] + cups[4:]],[])[:dest_idx+1]
        cups[dest_idx+1:dest_idx+4] = out
        cups.append(cups.pop(0))

        if i % (r/10000) == 0:
            h = round( (( (r - i+1) * (time.time() - t1)) / 3600), 3) 
            print(f'{i:>8}:\t{time.time()-t1:.3f}\t{time.time()-t0:.3f}\t{h} h/left - {round( ((i+1)/r)*100, 1)}%')

    if r == 100:
        return ''.join(str(x) for x in (cups[cups.index(1)+1:] + cups[:cups.index(1)]))
    return cups[1] * cups[cups[1]]

def main(f):
    cups = [int(x) for x in f]
    print(f'{game1(cups, 100)}\n')

    cups = [int(x) for x in f]
    cups.extend((list(range(10, int(1e6) + 1))))
    print(f'{game1(cups, int(1e7))}\n')

if __name__ == '__main__':   
        main("327465189") # p1 uitkomst: 82934675