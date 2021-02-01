def game(player1, player2):
    while player1 and player2:
        card1, card2 = player1.pop(0), player2.pop(0)
        if card1 > card2:
            player1.extend( [card1] )
            player1.extend( [card2] )
        else:
            player2.extend( [card2] )
            player2.extend( [card1] )

    winner = player1 or player2 # haha, how does this work Gido?
    return sum((len(winner) - i) * winner[i] for i in range(len(winner)))

def r_game(player1, player2, seen):
    while player1 and player2:
        if (tuple(player1), tuple(player2)) in seen:
            return 1, player1
        seen.add((tuple(player1), tuple(player2)))

        card1, card2 = player1.pop(0), player2.pop(0)
        if len(player1) >= card1 and len(player2) >= card2:
            winner, _ = r_game(player1[:card1], player2[:card2], set())
        else:
            winner = 1 if card1 > card2 else 0

        if winner:
            player1.extend( [card1] )
            player1.extend( [card2] )
        else:
            player2.extend( [card2] )
            player2.extend( [card1] )
        
    return (1, player1) if len(player1) + 0 else (0, player2)

def main(f):
    player1, player2 = [[int(n) for n in i.splitlines()[1:]] for i in open(f).read().split('\n\n')]
    p1, p2 = player1.copy(), player2.copy()
    
    print('\np1: ', game(player1, player2))
    print('\np2: ', sum((x + 1) * y for x, y in enumerate(r_game(p1, p2, set()) [1] [::-1] )), '\n')
    
if __name__ == '__main__':   
        main('day22.txt')