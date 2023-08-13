import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine:': 9, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

#Classes

class Card: #Creates all the cards

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + 'of ' + self.suit

class Deck: #Creates a deck of cards

    def __init__(self):
        # Empty list to store all 52 cards
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return f"The deck has: {deck_comp}"
    
    def shuffle(self): #Shuffle all the cards in the deck
        random.shuffle(self.deck)

    def deal(self): #Pick out a card from the deck
        single_card = self.deck.pop()
        return single_card

class Hand: #Show all the cards that the dealer and player has

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 #Keep track of aces
    
    def add_card(self, card): # Add a card to the player's or dealer's hand
        self.cards.append(card)
        self.value += values[card.rank]