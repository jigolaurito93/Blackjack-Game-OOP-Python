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
# Given the parameter, loop through how many times the card has to be dealt
def deal(number):
    cards_dealt = []
    for i in range(number):
        random_card = deck.pop()
        cards_dealt.append(random_card)
    return cards_dealt

# Call shuffle function
shuffle()

cards_dealt = deal(2)
card = cards_dealt[0]
rank = card[0]


# Conditional statement to determine the value of each card
if rank == "A":
    value = 11
elif rank == "J" or rank == "Q" or rank == "K":
    value = 10
else:
    value = int(rank)

rank_dict = {"rank": rank, "value": value}
print(rank_dict)

# print(f"Your card is: {random_card[0]} of {random_card[1]}")
