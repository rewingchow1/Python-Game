"""
Author: Amarnauth (Randy) Ewing Chow

- When a Card object is created, the value and suit are passed to create the object
- The show_card method returns the value and suit of the card object
- The print_card method prints the card object value and suit to the console (EXTRA - used for show_deck method in the
deck class)

"""


# Creates Card Class
class Card:

    # Initialize Card Object - A card object will have a value and a suit
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # Show Card Method - Returns the value and suit of the card object
    @property
    def show_card(self):
        return self.value, self.suit

    # Print Card Method - Prints card value and suit to the console
    @property
    def print_card(self):
        print(self.value + ' of ' + self.suit)

