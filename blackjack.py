import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':11}

playing = True
# Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit} "
    
# Deck Class
# instantiate a new deck
# 52 card objects, shuffle deck, pop method from cards list
class Deck:
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.deck.append(Card(suit,rank))
                
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "the deck has:" + deck_comp
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal_one(self):
        single_card = self.deck.pop()
        return single_card
    
# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)
        
     
            
        