import math
import random

#Base Player Object
class Player:
    def __init__(self, letter):
        #letter x or o
        self.letter= letter

        #Player to get moves
        def get_move(self, game);
        pass 

class RandomComputerPlayer(Player)
        def __init__(self, letter):
            super().__init__(letter)

            def get_move(self,game);
            square = random.choice(game.available_moves())
            return square

class HumanPlayer(Player)
        def __init__(self, letter):
            super().__init__(letter)

            def get_move(self,game);
            valid_square = False
            val = None
            while not valid_square:
                square = input(self.letter + '\'s turn. Input move (0-9):')
                # check correct value by casting to int, 
                # if Not cast = invalid
                # if spot is not available = invalid
                try:
                    val = int(square) 
                    if val not in game.available_moves():
                        raise ValueError
                    valid_square = True 
                    except ValueError
                    print('That move is not available. Please try again.')
                    return val 