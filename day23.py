def game1(cups, r):
    for _ in range(r):
        out = cups[1:4]
        dest = cups[0] - 1

        if dest == 0: # loop
            dest = len(cups)

        while dest in out:
            dest -= 1
            if dest == 0: # loop
                dest = len(cups)

        without = cups[:1] + cups[4:]
        dest_index = without.index(dest)
        
        without = without[:dest_index+1] + out + without[dest_index+1:]
        cups = without[1:] + without[:1]
    
    return ''.join(str(x) for x in (cups[cups.index(1)+1:] + cups[:cups.index(1)]))


def main(f, r):
    cups = [int(x) for x in f]

    print(f"\nGame 1: {game1(cups, r)}\n")

if __name__ == '__main__':   
        main("389125467", 10000000)
