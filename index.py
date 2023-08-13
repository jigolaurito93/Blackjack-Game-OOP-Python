import random

deck = []
# Array of Numbers
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
# Array of Suits
suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']


# Dealers Hand

for i in ranks:
    for j in suits:
        deck.append([i,j])

rand_card = random.choice(deck)
print(f"Your card is: {rand_card[0]} of {rand_card[1]}")
