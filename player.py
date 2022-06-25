import math
import random
# This game will be split up into 2 classes (player, game)
# This is the player

# base player class
class Player:
    # initialize letter player is going to represent
    def __init__(self, letter):
        # game pieces X or O
        self.letter = letter

    # all players will get next move (all players)
    def get_move(self, game):
        pass
# inherit from based on player class to make computer player
class RandomComputerPlayer(Player):
    # initialize super class which is the player
    def __int__(self, letter):
        super().__int__(letter)
    # define moves
    def get_move(self, game):
        # gets random spot on board for next move
        square = random.choice(game.available_moves())
        return square
class HumanPlayer(Player):
    def __int__(self, letter):
        super().__int__(letter)

    # human pick spot based on user input
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # checking its valid value cast to int
            # if not invalid and if spot not free invalid
            try:
                # checks to make sure number entered
                val = int(square)
                # checks to make sure spot free
                if val not in game.available_moves():
                    raise ValueError
                # if both checks = true it's a valid move
                valid_square = True # if these are successful
            # if valid square = false error message
            except ValueError:
                print('Invalid square. Try again.')
        # once valid square is given it's returned
        return val