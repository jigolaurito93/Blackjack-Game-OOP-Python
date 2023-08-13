import random

# Empty Deck
deck = []
# Array of Ranks
ranks = ['A', "2", "3", "4", "5", "6", "7", "8", "9", "10", 'J', 'Q', 'K']
# Array of Suits
suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']

# For loop to generate random card
for rank in ranks:
    for suit in suits:
        deck.append([rank, suit])


# Create function to shuffle the deck
def shuffle():
    random.shuffle(deck)

# Create a function that removes the last item on the deck (array) to deal the cards
def deal():
    random_card = deck.pop()
    return random_card

shuffle()
random_card = deal()
print(f"Your card is: {random_card[0]} of {random_card[1]}")
