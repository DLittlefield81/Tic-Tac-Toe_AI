from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = ['' for _ in range(9)] #we will use a single list to rep 3x3 baord
        self.current_winner = None #keep track of winner!
        
        def print_board(self)
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print ('| ' + ' | '.join(row) + ' |')
            
            
            @staticmethod
            def print_board_nums( ):
                #tells us which num correspons to which box
                num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
                for row in num_board:
                    print('| ' + ' | '.join(row) + ' |')
                    
                    def available_moves(self):
                        return[i for i, spot in enumerate(self.board) if spot == ' ']
                    
                    def empty_squares(self)
                    return ' ' in self.board
                
                def num_empty_squares(self)
                    return self.board.count(' ')
                
                def make_move(self, square, letter)
                #if valid move = assign to spot
                #if invalid return false
                if self.board[square] == ' ':
                    self.board[square] = letter
                    if self.winner(square,letter):
                        self.current_winner = letter
                        return True
                    return False
                
                    
                    def play(game, x_player, o_player, print_game=True):
                        if print_game:
                            game.print_board_nums()
                     letter = 'x' #starting Letter       
                      #itterate while board still has space left
                      while game.empty_squares():
                          #get current player move
                          if letter == 'O':
                              square = o_player.get_move(game)
                          else:
                              square = x_player.get_move(game)
                     # Define move function
                     if game.make_move(square, letter):
                         if print_game:
                             print(letter + f' makes a  move to {square}' )       
                            game.print_board()
                            print('')#print empty line
                            
                            #alternate letters
                            letter = 'O' if letter == 'X' else 'X' #Switch Player
                            
                            if print_game:
                                print('It\'s a tie!')
                            
                            if __name__ =='__main__':
                                x_player = HumanPlayer('X')
                                o_player = RandomComputerPlayer('O')
                            t = TicTacToe()
                            play(t, x_player, o_player, print_game=True)