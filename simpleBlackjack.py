import random

#initializing variables
play = 'Y'
player = []
dealer = []

# deal cards

def hit(hand):
    hand.append(random.randint(1,13))

# calculate hand total
def handTotal(hand):
    total = 0
    for i in hand:
        total += i
    return total

def bust(hand):
    if handTotal(hand) > 21:
        return True
    
# check for winner
def checkWinner():
    if handTotal(player) == 21 and handTotal(dealer) !=21:
        print("Winner is: Player")
    elif handTotal(player) == 21 and dealer == 21:
        print("It's a tie")
    elif handTotal(player) > handTotal(dealer) and bust(player) == False:
        print("Winner is: Player")
    else:
        print("The house wins")

#desplay the deck values
def score():
    print("Player: " + str(handTotal(player)) + " Dealer: " + str(handTotal(dealer)))
    print()

#game loop
print("Welcome to Blackjack")
print()
while play == "Y":
    
    #reseting decks
    player.clear()
    dealer.clear()
    gameover = False

    #giving the player and dealer 2 cards
    for i in range(2):
        hit(player)
        hit(dealer)
    score()

    #player adds cards till he's satified or bust
    Hit = input("Hit? (Y/N)")
    while Hit == 'Y':
        hit(player)
        if bust(player):
            gameover = True
            break
        score()
        Hit = input("Hit? (Y/N)")
    if gameover:
        score()
        print("Bust!! The House wins")
    else:
        while handTotal(dealer) < handTotal(player)  and handTotal(dealer) != 21:
            hit(dealer)
            if bust(dealer):
                gameover = True
                break
            score()
        if gameover:
            score()
            print("Bust!! The player wins")
        else:
            checkWinner()
    play = input("Play again? (Y/N)")
    




        

    
    
