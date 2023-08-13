import random

# Empty Deck
deck = []
# Array of Ranks
ranks = ['A', "2", "3", "4", "5", "6", "7", "8", "9", "10", 'J', 'Q', 'K']
# Array of Suits
suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']

for rank in ranks:
        for suit in suits:
                deck.append([rank, suit])


# Deal cards
def deal():
    card = random.choice(deck)
    return card



playerHand = []
dealerHand = []

playerScore = 0
dealerScore = 0


       


def dealPlayer():
        card = deal()
        playerHand.append(card)
        

def dealDealer():
        card = deal()
        dealerHand.append(card)

dealPlayer()
dealPlayer()
dealDealer()
dealDealer()

# Show cards
print(f"\nPlayer has: {playerHand[0][0]} of {playerHand[0][1]} & {playerHand[1][0]} of {playerHand[1][1]}\n")
print(f"Dealer has: {dealerHand[0][0]} of {dealerHand[0][1]}")

# Calculate total of cards

# check for winner

# game loop