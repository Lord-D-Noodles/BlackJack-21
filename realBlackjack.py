import random

# Deck of cards, hands, bets
deck = [2,3,4,5,6,7,8,9,10,'A','J','Q','K',
        2,3,4,5,6,7,8,9,10,'A','J','Q','K',
        2,3,4,5,6,7,8,9,10,'A','J','Q','K',
        2,3,4,5,6,7,8,9,10,'A','J','Q','K']
player = []
house = []
gameover = False
wallet = 100
betPool = 0

#Game sential value
game = True

# Drawing a card from the deck
def draw(hand):
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

# Calculate the total in a hand
def total(hand):
    total = 0
    for card in hand:
        if card in range(1,11):
            total+= card
        if card in ['J','Q','K']:
            total+= 10
        if card == 'A':
            if total + 11 > 21:
                total += 1
            else:
                total+=11
    return total

def bust(hand):
    if total(hand) > 21:
        return True

def toString(hand):
    print(hand)
    print("Total: " + str(total(hand)))

# Betting
def bet(number: int, wallet, betPool):
        return wallet - number, betPool + number

#payout
def pay(wallet, betpool):
        return  wallet + 2*betpool

# replay
def replay():
    loop = input("Continue? (y/n)")
    if loop.lower() == 'y':
        return True
    else: return False

# Game Loop
print("welcome to Blackjack")
print()

while game:
    #reseting game variables
    betPool = 0
    player.clear()
    house.clear()
    gameover = False
    
    #Chekcing for broke boys
    if(wallet < 20):
        print("Insufficient  funds for buy in")
        break

    #Getting initial bet
    print("Enter bet (20$ minimum)")
    user = int(input())
    while wallet - user < 0 or user < 20:
        if wallet - user < 0:
            print("Insufficient  funds. Try again")
        elif  user < 20:
            print("Minimum bet is 20. Try agian: ")
        user = int(input())
    wallet, betPool = bet(user, wallet, betPool)
    
    #Adding 2 card to each hand
    for i in range(2):
        draw(player)
        draw(house)
    print("Player: " + str(player) + " House: " + str(house[0]))
    print("Total: " + str(total(player)))
    
    #gameplay
    #User turn
    turn = True
    while turn:
        print("1.Hit 2.Stand 3.Double Down 4.Split ")
        print()
        action = input()
        match action:
            #hit
            case '1':
                draw(player)
                toString(player)
                if bust(player):
                    gameover = True
                    break
            #fold
            case '2':
                turn = False
            #double down
            case '3':
                if wallet - betPool > 0:
                    wallet, betPool = bet(betPool, wallet, betPool)
                    draw(player)
                    toString(player)
                    print("Bet: " + str(betPool))
                    turn = False
                    gameover = bust(player)
            #split
            case '4':
                user = int(input("Enter additional bet: "))
                if wallet - user > 0:
                    wallet, betPool = bet(user, wallet, betPool)
                    #removing one of the dublicate cards
                    for x in range(len(player)-1):
                        for y in range(x+1,len(player)):
                            if player[x] == player[y]:
                                player.remove(player[y])
                    toString(player)
                    print("Bet: " + str(betPool))   
                else:
                    print("Insufficient  funds. Try again")
            #reset
            case _:
                print("Invalid input")
    #User bust
    if gameover:
        gameover = False
        print()
        print("Bust!! House wins")
        print("wallet: " + str(wallet))
    #CPU turn 
    else:
        print()
        print("House: " + str(house))
        print("Total: " + str(total(house)))
        while total(house) < 17:
            draw(house)
            print(house)
            print("Total: " + str(total(house)))
            print()
            if bust(house):
                break
        if gameover:
            gameover = False
            print("Bust!! You win!")
        else:
            if total(player) == 21 and total(house) !=21:
                print("Winner is: Player")
                wallet = wallet + pay(wallet,betPool)
            elif total(player) == total(house):
                print("It's a tie")
                wallet = wallet + betPool
            elif total(player) > total(house):
                print("Winner is: Player")
                wallet = pay(wallet,betPool)
            else:
                print("The house wins")
    print("Wallet:" + str(wallet))
    game = replay()
    print()
    
    









