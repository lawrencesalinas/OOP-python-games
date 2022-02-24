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
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)


# A class to hold card objects dealt from the deck
# will be used to calculate  the value of those card using the values dictionary defined above.
# adjust values of aces
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        # card passed in 
        # from Deck.deal() ---> single Card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank]
        
        # track aces
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        # if total value > 21 and I still have an ace
        # then change ace to be a 1 instead of an 11
        while self.value > 21 and self.aces > 0:
        # change ace to 1, 11 - 10
            self.value -= 10
            self.aces -= 1 
        
# test_deck = Deck()
# test_deck.shuffle()
# Player
# test_player = Hand()
# Deak 1 card from the deck
# pulled_card = test_deck.deal()
# print(pulled_card)
# test_player.add_card(pulled_card)
# print(test_player.value)

# Chips class
# to keep track of a Player's starting chips, bets, and ongoing winnings
         

        
    
    
    
     
            
        