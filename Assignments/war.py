# -*- coding: utf-8 -*-

# Name: Coty Hamilton

# Email: cotyhamilton@gmail.com

# Assignment: Homework 2 - War

# Due: 17 Feb @ 11:59 p.m.

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

        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A"]

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
            'J': CARD,
            'Q': CARD,
            'K': CARD,
            'A': CARD,
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
        self.points = str(rank).index(self.rank)
        self.ascii = self.__str__()
    
    def __str__(self):
        symbol = self.symbols[self.suit]
        trank = self.rank+symbol
        brank = symbol+self.rank
        return self.str_values[self.rank].format(trank=trank, suit=symbol,brank=brank)

# overload comparison operators for card objects

    def __lt__(self,other):
        return self.ranks.index(self.rank) < self.ranks.index(other.rank)
    def __gt__(self,other):
        return self.ranks.index(self.rank) > self.ranks.index(other.rank)
    def __eq__(self,other):
        return self.ranks.index(self.rank) == self.ranks.index(other.rank)

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
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A"]:
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
        
# random.shuffle randomizes order of objects in a list

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

# random.shuffle randomizes order of objects in a list

    def shuffle(self):
        random.shuffle(self._list)

"""
@Class Game
@Description:
    This class represents a game. 
@Methods:
    deal() - deals 26 cards to each player
    compare() - compares ranks of two cards
    emptyPot() - distributes cards from pot to winner and emptys each players temporary war hand
    tie() - adds cards to pot and temporary war hand
""" 
class Game(object):
    def __init__(self,player_name):
        self.D = Deck()
        self.D.shuffle()

        self.computer = Player("COMPUTER")
        self.player = Player(player_name)


        self.winner = None
        self.count = 0
        self.warCount = 0
        self.pot = Hand()
        self.__deal()
        self.__gameloop()
    
    def __deal(self):
        for i in range(26):
            self.computer.hand.add(self.D.pop_card())
            self.player.hand.add(self.D.pop_card())

    def __compare(self, playerCard, computerCard):
        if(playerCard > computerCard):
            self.win = self.player
        elif (playerCard < computerCard):
            self.win = self.computer
        else:
            self.win = "tie"
        return self.win

    def __emptyPot(self, winningPlayer):
        while(len(self.pot._list)):
            winningPlayer.hand.add(self.pot.pop_card())
        while(len(self.player.war._list)):
            self.player.war.pop_card()
        while(len(self.computer.war._list)):
            self.computer.war.pop_card()

    def __tie(self, p, c):
        os.system('clear')
        print("██╗    ██╗ █████╗ ██████╗\n██║    ██║██╔══██╗██╔══██╗\n██║ █╗ ██║███████║██████╔╝\n██║███╗██║██╔══██║██╔══██╗\n╚███╔███╔╝██║  ██║██║  ██║\n ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝\n")
        
        # only if there is more than one card in a player's hand
        
        # exits after popping two cards in to each players war hand and the main pot

        # game continues as normal in main game loop
        
        if(len(c.hand._list) > 1):
            c.war.add(c.hand._list[0])
            self.pot.add(c.hand.pop_card())
        if(len(c.hand._list) > 1):
            c.war.add(c.hand._list[0])
            self.pot.add(c.hand.pop_card())

        if(len(p.hand._list) > 1):
            p.war.add(p.hand._list[0])
            self.pot.add(p.hand.pop_card())
        if(len(p.hand._list) > 1):
            p.war.add(p.hand._list[0])
            self.pot.add(p.hand.pop_card())

        print(c.name + "'s hand:\n")
        print(c.war)
        print()
        print(p.name + "'s hand:")
        print(p.war)
        print()

        self.warCount = self.warCount + 1


    def __gameloop(self):
        while(len(self.computer.hand._list) and len(self.player.hand._list)):
            os.system('clear')
            print(" ██████╗  █████╗ ███╗   ███╗███████╗\n██╔════╝ ██╔══██╗████╗ ████║██╔════╝\n██║  ███╗███████║██╔████╔██║█████╗\n██║   ██║██╔══██║██║╚██╔╝██║██╔══╝ \n╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗\n ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝")
            print()
            print(self.computer.name)
            print()
            print(self.computer.hand._list[0])
            print(self.player.hand._list[0])
            print()
            print(self.player.name)
            print()

            self.winner = self.__compare(self.player.hand._list[0], self.computer.hand._list[0])
            
            if (self.winner == "tie"):
                print("██╗    ██╗ █████╗ ██████╗\n██║    ██║██╔══██╗██╔══██╗\n██║ █╗ ██║███████║██████╔╝\n██║███╗██║██╔══██║██╔══██╗\n╚███╔███╔╝██║  ██║██║  ██║\n ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝\n")
                self.__tie(self.player, self.computer)
            else:
                self.pot.add(self.player.hand.pop_card())
                self.pot.add(self.computer.hand.pop_card())
                self.__emptyPot(self.winner)
                print(self.winner.name + " wins")

            self.count = self.count + 1

            if (self.count % 26 == 0):
                self.player.hand.shuffle()
                self.computer.hand.shuffle()
            
            # time.sleep(.75)

            
class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = Hand()
        self.war = Hand()


G = Game("PLAYER")
os.system('clear')
print ("\n\n\t\t" + G.winner.name + " WINS THE GAME!!")
print ("\n\n\t\tWar occured " + str(G.warCount) + " times out of " + str(G.count) + " rounds")