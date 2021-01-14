"""
Author: Amarnauth (Randy) Ewing Chow

- random.py library is imported for randint function to determine a random integer with a certain boundary
- Classes and methods from Card.py are added
- When a Deck object is created, if the win condition is not stated, it is automatically configured to predefined values
- Every deck object calls the build_deck method when a deck object is created; This builds a list of card objects in
the deck
- A tag is associated when a deck object is created with a string 'Deck'
- The win flag for the object is initialized as false
- The show_deck method prints all cards in the deck to the console (EXTRA)
- The shuffle_deck method randomly swaps card objects in the deck list to different indices
- The draw_card method pops and returns a card object at the top of the deck list
- The add_card method places the card object back on the top of the deck
- The remove_card method removes a list of cards provided from the deck object (EXTRA)
- The draw_check_win method sets the objects win flag True or False if the card object sent is equal to the
predefined win condition(s)

"""
# Imports all functions from random.py
# Imports all classes & methods from Card.py
import random
from Card import *


# Creates Deck Class
class Deck:

    # Initialize Deck Object - Sets up object conditions
    def __init__(self, win_condition=None):
        if win_condition is None or len(win_condition) == 0:
            win_condition = ['J', 'Spades', 'A', 'Diamonds']
        self.win_condition = win_condition
        self.cards = []
        self.build_deck
        self.tag = 'Deck'
        self.win_flag = False

    # Build Deck Method - Creates deck object with card objects
    @property
    def build_deck(self):
        for suit in ['Hearts', 'Diamonds', 'Spades', 'Clubs']:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(value, suit))

    # Show Deck Method - Prints all card objects in the deck
    @property
    def show_deck(self):
        for card in self.cards:
            card.print_card

    # Shuffle Deck Method - Randomly rearranges card objects in the deck
    @property
    def shuffle_deck(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[r], self.cards[i] = self.cards[i], self.cards[r]

    # Draw Card Method - Draw a card object from top of the deck
    @property
    def draw_card(self):
        return self.cards.pop()

    # Add Card Method - Adds Card to the top of the deck
    def add_card(self, card):
        self.cards.append(card)

    # Remove Card Method - Removes card object from the deck with specified value and suit
    def remove_cards(self, remove_cards):
        stop = int(len(remove_cards) / 2)
        for i in range(0, stop, 1):
            rm_value = remove_cards[2 * i]
            rm_suit = remove_cards[2 * i + 1]
            for card in self.cards:
                value, suit = card.show_card
                if value == rm_value and suit == rm_suit:
                    self.cards.remove(card)
                    break

    # Draw Check Win Method - Check to see if drawn card object fits the predetermined winning condition
    def draw_check_win(self, card):
        value, suit = card.show_card
        stop = int(len(self.win_condition) / 2)
        for i in range(0, stop, 1):
            win_value = self.win_condition[2 * i]
            win_suit = self.win_condition[2 * i + 1]
            if value == win_value and suit == win_suit:
                self.win_flag = True
                break
            else:
                self.win_flag = False
