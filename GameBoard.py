"""
Author: Amarnauth (Randy) Ewing Chow

- All Dice, Coin & Deck classes and methods are added to the GameBoard.py file
- When a GameBoard object is created in Main.py, if either game elements and output file are not stated, they are
automatically configured to predefined values
- The GameBoard object also has its attempt counter to count the number of attempts and win flag to see if a win has
been met
- When play_game method is called in the Main.py for a GameBoard object, this is when the game starts; The game looks
for a 'p' typed input to start, if not typed or anything else other than 'p' is inputted, a "Wrong Input" message will
be shown and the request for 'p' will show up again
- When 'p' is typed, the game_engine method starts and looks for through the list of game elements and see what type of
game element it is, as each element has its own tag; If a dice tag is found, the dice is rolled and a win is checked
for that object, the result is then printed on the console and in the GameResult.txt file; If a coin tag is found, the
coin is flipped and a win is checked for that object, the result is then printed on the console and in the
GameResult.txt; If a deck tag is found, the deck is shuffled, a card is drawn, a win is checked for that card and it is
added to the top of the deck, the result is then printed on the console and in the GameResult.txt; If a game is added
with neither tag, the message "Game Does Not Exist" is printed
- After the game_engine has run and all objects have been checked for a win, the GameBoard checks for a game win in
game_win_check; This counts for the number of wins for all game elements and checks if all element flags are True to
trigger the GameBoard object win flag
- If a win is met, the game is over, otherwise, game loops until GameBoard object win flag is True
- Output method is used to print lines to the console and in the output file created for the GameBoard object in Main.py

"""
# Imports all classes & methods from Dice.py, Coin.py and Deck.py
from Dice import *
from Coin import *
from Deck import *


# Creates GameBoard Class
class GameBoard:

    # Initialize Game Board Object - Sets up object conditions
    def __init__(self, game_elements=None, output_file=None):
        if game_elements is None or len(game_elements) == 0:
            game_elements = [Dice([6], 6), Coin('Heads'), Deck(['J', 'Spades', 'A', 'Diamonds'])]
        if output_file is None:
            output_file = open('GameResults.txt', 'w+')
        self.game_elements = game_elements
        self.output_file = output_file
        self.attempts = 0
        self.win_flag = False

    # Game Play Method - Type 'p' to play; Game loops until all objects meet their winning conditions
    @property
    def play_game(self):
        flag = False
        while not flag:
            start_game = input('Type "p" to play: ')
            if start_game == 'p':
                self.game_engine
                self.game_win_check
                self.attempts += 1
                if self.win_flag:
                    flag = True
                else:
                    lose_line = 'YOU LOSE! attempt: ' + str(self.attempts) + '\n\n'
                    self.output(lose_line)
            else:
                print('Wrong Input\n\n')
        win_line = 'YOU WIN! attempt: ' + str(self.attempts) + '\n\n'
        self.output(win_line)
        input('Press Enter to Continue')

    # Game Engine Method - For dice, coin or deck tag, the correct operations will be done for corresponding object type
    @property
    def game_engine(self):
        for game_element in self.game_elements:
            if game_element.tag == 'Dice':
                game_element.roll_dice
                game_element.roll_check_win
                roll_result = 'You rolled a ' + str(game_element.get_number)
                self.output(roll_result)
            elif game_element.tag == 'Coin':
                game_element.flip_coin
                game_element.flip_check_win
                flip_result = 'You flipped a ' + game_element.get_side
                self.output(flip_result)
            elif game_element.tag == 'Deck':
                game_element.shuffle_deck
                card = game_element.draw_card
                card_value, card_suit = card.show_card
                Deck.draw_check_win(game_element, card)
                Deck.add_card(game_element, card)
                draw_result = 'You drew a ' + card_value + ' of ' + card_suit
                self.output(draw_result)
            else:
                print('Game Does Not Exist')
                break

    # Game Win Check Method - check if all game objects meet their predetermined game win condition
    @property
    def game_win_check(self):
        win_count = 0
        for game_element in self.game_elements:
            if game_element.win_flag:
                win_count += 1
            else:
                break
            if win_count == len(self.game_elements):
                self.win_flag = True

    # Output Method - Pushes results to console and output file
    def output(self, line):
        print(line)
        self.output_file.writelines(line + '\n')
        self.output_file.flush()
