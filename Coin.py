"""
Author: Amarnauth (Randy) Ewing Chow

- random.py library is imported for randint function to determine a random integer with a certain boundary
- When a Coin object is created, if the win condition is not stated, is it automatically configured to predefined values
- Every coin object's facing up side is preset to 'Heads'
- A tag is associated when a coin object is created with a string 'Coin'
- The win flag for the coin object is initialized as false
- The flip_coin method finds a random integer between the 0 and 1 and sets the random value to the facing up side, with
0 being 'Heads' and 1 being 'Tail'
- The get_side method returns the facing up side of the coin object
- The flip_check_win method sets the objects win flag True or False if the current side is equal to the predefined win
condition
- The set_side method sets the facing up side manually if need be (EXTRA)

"""
# Imports all functions from random.py
import random


# Creates Coin Class
class Coin:

    # Initialize Coin Object - Sets up object conditions
    def __init__(self, win_condition=None):
        if win_condition is None or len(win_condition) == 0:
            win_condition = 'Heads'
        self.win_condition = win_condition
        self.side = 'Heads'
        self.tag = 'Coin'
        self.win_flag = False

    # Flip Coin Method - Determines random integer from 0 to 1 for heads or tails side of the coin object
    @property
    def flip_coin(self):
        if random.randint(0, 1) == 0:
            self.side = 'Heads'
        else:
            self.side = 'Tails'

    # Get Side Method - Returns random side of the coin object
    @property
    def get_side(self):
        return self.side

    # Flip Check Win Method - Check to see if coin object flipped its predetermined winning condition
    @property
    def flip_check_win(self):
        if self.get_side == self.win_condition:
            self.win_flag = True
        else:
            self.win_flag = False

    # Set Side Method - Sets side of the coin object
    def set_side(self, side):
        self.side = side
