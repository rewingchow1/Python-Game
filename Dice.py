"""
Author: Amarnauth (Randy) Ewing Chow

- random.py library is imported for randint function to determine a random integer with a certain boundary
- When a Dice object is created, if either win condition and number of sides are not stated, they are
automatically configured to predefined values
- Every dice object's facing up number is preset to 1
- A tag is associated when a dice object is created with a string 'Dice'
- The win flag for the dice object is initialized as false
- The roll_dice method finds a random integer between the 1 and the number of sides specified when the object was
created and sets the random value to the facing up number
- The get_number method returns the facing up number of the dice object
- The roll_check_win method sets the objects win flag True or False if the current number is equal to the predefined win
condition(s)
- The set_number method sets the facing up number manually if need be (EXTRA)

"""
# Imports all functions from random.py
import random


# Creates Dice Class
class Dice:

    # Initialize Dice Object - Sets up object conditions
    def __init__(self, win_condition=None, number_of_sides=None):
        if win_condition is None or len(win_condition) == 0:
            win_condition = [6]
        if number_of_sides is None:
            number_of_sides = 6
        self.win_condition = win_condition
        self.number_of_sides = number_of_sides
        self.number = 1
        self.tag = 'Dice'
        self.win_flag = False

    # Roll Dice Method - Determines random integer from 1 to the number of sides of the dice object
    @property
    def roll_dice(self):
        self.number = random.randint(1, self.number_of_sides)

    # Get Number Method - Returns number on the dice object
    @property
    def get_number(self):
        return self.number

    # Roll Check Win Method - Checks to see if dice object rolled its predetermined winning condition
    @property
    def roll_check_win(self):
        if self.get_number in self.win_condition:
            self.win_flag = True
        else:
            self.win_flag = False

    # Set Number Method - Sets number on the dice object
    def set_number(self, number):
        self.number = number
