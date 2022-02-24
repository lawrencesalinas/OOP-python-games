import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# Card class
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    
# Deck Class
# instantiate a new deck
# 52 card objects, shuffle deck, pop method from cards list
class Deck:
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
                
    def shuffle(self):
         # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()

new_deck = Deck()
print(new_deck.shuffle)
# print(new_deck.all_cards)
                
# Player Class
# a player should be able to hold instances of Cards 
# they should also be able to remove and add them from their hand. 
# We want the Player class to be flexible enough to add one card, or many cards 
# so we'll use a simple if check to keep it all in the same method.

class Player:
    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.all_cards = []
    
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        # if we're receving a list of cards we use the mothod extend
        # if we're only receiving one card we use the append method
        if type([]) == type(new_cards):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"

# jose = Player("Jose")
# print(jose)

# War game logic

player_one = Player("One")
player_two = Player("Two")
# Setup new game
new_deck = Deck()
new_deck.shuffle()

# print(new_deck.all_cards)
# for card in new_deck.all_cards:
#     print(card)


# split deck between two players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
# check if cards are distributed
# print(len(player_one.all_cards))

game_on = True

round_num = 0
while game_on:
    round_num += 1
    print(f"Round {round_num}")
    
    if len(player_one.all_cards) == 0:
        print("Player One, out of cards!, Player Two Wins!")
        game_on = False
        break
    
    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards!, Player One Wins!")
        game_on = False
        break
    
    # Start a new round
    
    # current cards in play  
    player_one_cards = []
    # remove one from player 1 cards and append it to player 1's cards in play
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_one_cards.append(player_two.remove_one())
    
    
    
    




        
    
        
        
    
# SUIT, RANK, VALUE

 # DECK 
 
 # PLAYER