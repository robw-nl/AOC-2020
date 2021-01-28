player1, player2 = [[int(n) for n in i.splitlines()[1:]] for i in open('day22.txt').read().split('\n\n')]

def draw(player1, player2):
    if player1 > player2:
        return player1, ()
    return (), player2

while len(player1) > 0 and len(player2) > 0:
    card1, card2 = draw(player1[0], player2[0])
    if card1:
        player1.extend([card1]) 
        del player2[0]
    else:
        player2.extend([card2])
        del player1[0]

winner = player1 if len(player1) > len(player2) else player2
total = 0
while len(winner) > 0:
    m = len(winner)
    total += m * winner.pop(0)

print('\nWinning score: ', total, '\n')