# -*- coding: utf-8 -*-
import os
import random
import time

#Source: http://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards

CARD = """\
┌───────┐
│{}     │
│       │
│   {}  │
│       │
│     {}│
└───────┘
""".format('{trank:^2}', '{suit: <2}', '{brank:^2}')

TEN = """\
┌───────┐
│{}    │
│       │
│   {}  │
│       │
│    {}│
└───────┘
""".format('{trank:^3}', '{suit: <2}', '{brank:^3}')

HIDDEN_CARD = """\
┌───────┐
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
└───────┘
"""

class Card(object):
    
    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """

        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]



        self.card_values = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 11,
            'Queen': 12,
            'King': 13,
            'Ace': 14,  # value of the ace is high until it needs to be low
        }

        self.str_values = {
            '2': CARD,
            '3': CARD,
            '4': CARD,
            '5': CARD,
            '6': CARD,
            '7': CARD,
            '8': CARD,
            '9': CARD,
            '10': TEN,
            'Jack': CARD,
            'Queen': CARD,
            'King': CARD,
            'Ace': CARD,
        }

        self.suits = ['Spades','Hearts','Diamonds','Clubs']

        self.symbols = {
            'Spades':   '♠',
            'Diamonds': '♦',
            'Hearts':   '♥',
            'Clubs':    '♣',
        }


        if type(suit) is int:
            self.suit = self.suits[suit]
        else:
            self.suit = suit.capitalize()
        self.rank = str(rank)
        self.symbol = self.symbols[self.suit]
        self.points = self.card_values[str(rank)]
        self.ascii = self.__str__()
    

    def __str__(self):
        symbol = self.symbols[self.suit]
        trank = self.rank[0]+symbol
        brank = symbol+self.rank[0]
        return self.str_values[self.rank].format(trank=trank, suit=symbol,brank=brank)
           
    def __cmp__(self,other):
        
        return self.ranks.index(self.rank) < self.ranks.index(other.rank) 
   
    # Python3 wasn't liking the __cmp__ to sort the cards, so 
    # documentation told me to use the __lt__ (less than) 
    # method.
    def __lt__(self,other):
        return self.__cmp__(other)

"""
@Class Deck 
@Description:
    This class represents a deck of cards. 
@Methods:
    pop_cards() - removes a card from top of deck
    add_card(card) - adds a card to bottom of deck
    shuffle() - shuffles deck
    sort() - sorts the deck based on value, not suit (could probaly be improved based on need)
"""       
class Deck(list):
    def __init__(self):
        #assume top of deck = 0th element
        self.cards = []
        for suit in range(4):
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]:
                self.cards.append(Card(suit,rank))
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "".join(res)
    
    def pop_card(self):
        return self.cards.pop(0)
        
    def add_card(self,card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards = sorted(self.cards)

class Hand(list):
    def __init__(self, cards=None):
        """Initialize the class"""
        super().__init__()
        if (cards is not None):
            self._list = list(cards)
        else:
            self._list = []
    
    def __str__(self):
        return self.join_lines()

    def join_lines(self):
        """
        Stack strings horizontally.
        This doesn't keep lines aligned unless the preceding lines have the same length.
        :param strings: Strings to stack
        :return: String consisting of the horizontally stacked input
        """
        liness = [card.ascii.splitlines() for card in self._list]
        return '\n'.join(''.join(lines) for lines in zip(*liness))
        
    def add(self,card):
        self._list.append(card)
        
    def sort(self):
        self._list = sorted(self._list)
    
    def pop_card(self):
        return self._list.pop(0)
    
    def __getitem__(self,key):
        return self._list[key]

class Game(object):
    def __init__(self,player_name):
        self.D = Deck()
        self.D.shuffle()
        self.D.shuffle()
        self.computer = {"name": "Computer", "hand":Hand()}
        self.player1 = {"name": player_name, "hand":Hand()}
        self.winner = None
        self.pot = Hand()
        self.__deal()
        self.__gameloop()
    
    def __deal(self):
        for i in range(4):
            self.computer["hand"].add(self.D.pop_card())
            self.player1["hand"].add(self.D.pop_card())

    # def __cmp__(self):
    #     return self.computer["hand"][0] < self.player1["hand"][0]
    
    # def __lt__(self):
    #     return self.__cmp__()

    def __gameloop(self):
        while(len(self.computer["hand"]._list) and len(self.player1["hand"]._list)):
            print(self.computer["hand"]._list[0])
            print(self.player1["hand"]._list[0])


            if(self.player1["hand"]._list[0] < self.computer["hand"]._list[0]):
                self.winner = "player1"
            elif (self.player1["hand"]._list[0] > self.computer["hand"]._list[0]):
                self.winner = "computer"
            else:
                self.winner = "tie"
                print("tie")
            self.pot.add(self.player1["hand"].pop_card())
            self.pot.add(self.computer["hand"].pop_card())

            if(self.winner == "player1"):
                while(len(self.pot._list)):
                    self.player1["hand"].add(self.pot.pop_card())
                print("player 1 wins")
            elif(self.winner == "computer"):
                while(len(self.pot._list)):
                    self.computer["hand"].add(self.pot.pop_card())
                print("computer wins")

            print("p1 hand:")
            print(self.player1["hand"])
            print("computer hand:")
            print(self.computer["hand"])
            time.sleep(2)

            



class Player(object):
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    

# H = Hand()
# D = Deck()
# D.shuffle()
# for i in range(5):
#     H.add(D.pop_card())
# H.sort()
# print(H)

G = Game("Coty")
# print(G.computer["hand"])
# print(G.player1["hand"])



