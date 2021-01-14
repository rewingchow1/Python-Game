"""
Author: Amarnauth (Randy) Ewing Chow

- All GameBoard classes and methods are added to the Main.py file
- A GameResults.txt file is created and is overwritten for every time the game is played; this can be easily changed to
append when 'w+' is changed to 'a'
- element_list[] holds all game elements, in which as many game elements can be added once objects are initialized
correctly
- Every GameBoard object a different set of game elements with varying parameters;
- For a Dice element, the win condition(s) and number sides need to be stated when creating the object for the GameBoard
- For a Coin element, only the win condition needs to be stated when creating the object for the GameBoard
- For a Deck element, the win condition(s) needs to be stated when creating the object for the GameBoard
- The GameBoard object is created with its game elements and output file
- The play_game method of the GameBoard object is called to start the game for the GameBoard object

"""
# Imports all classes & methods from GameBoard.py
from GameBoard import *

# Setup Output File - Pushes results to file; Overrides every time game is played
with open('GameResults.txt', 'w+') as output_file:

    # Game List - Creates a list of game elements with their parameters for the game board
    # Dice([list of winning conditions], number of sides) | Coin(winning condition) | Deck([list of winning conditions])
    dice1 = Dice([6], 6)
    coin1 = Coin('Heads')
    deck1 = Deck(['J', 'Spades', 'A', 'Diamonds'])
    element_list = [dice1, coin1, deck1]

    # Create Game Board Object - Sends list of elements for the game board and its corresponding output file
    game = GameBoard(element_list, output_file)

    # Start Game - call play_game method of the game board object
    game.play_game



