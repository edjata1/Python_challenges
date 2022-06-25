import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    # Game board length 9 for 3x3 board
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single index list rep 3x3 board
        self.current_winner = None # keep track of winner

       # print(self.board)

    # print the board
    def print_board(self):
        # splite board range for indexing len 9 list of board
        # i in range(3) which row we are indexing into 1st, 2nd, or 3rd
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            # .join(row) = joins each row into string
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def print_board_num():
        # board num: [1 | 2 | 3] indicates corresponding number on board for each row
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        # concatenation sub array string and print board
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    # what free moves left? after move is made
    def available_moves(self):
        # list comprehension return list of index
        return[i for i, spot in enumerate(self.board) if spot == ' ']
    # OR
        # expand out: 1st initialize moves to empty list
        # moves = []
        # create a list and assign tuple with index and value @ that index
        # going through tuple assigning 1st value to i and 2nd value to spot
        # for(i, spot) in enumerate(self.board):
            # [ 'x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            # if true = empty space, available to move too
            # if spot == ' ':
                # Append index i
                # moves.append(i)
        # return moves

    # check if there are empty squares on board
    def empty_squares(self):
        # self.board returns t/f bool
        return ' ' in self.board

    # this counts the number of empty spaces on board
    def num_empty_squares(self):
        # or self.board.count = also give length of list
        return self.board.count(' ')
        #or which returns: the(        return[i for i, spot in enumerate(self.board) if spot == ' ']) list of spots free
        # return len(self.available_moves())

    # this makes move
    def make_move(self, square, letter):
        # if valid move, then make the move(assign square letter)
        # then return true, if invalid return false
        if self.board[square] == ' ':
            # places letter on board
            self.board[square] = letter

            # last move before checking winner
            if self.winner(square, letter):
                # checks if letter won
                self.current_winner = letter
            return True
        return False

    # define winner
    def winner(self, square, letter):
        # 1st player getting 3 in row. row, colum, diagonal

        # check row (div by 3 round down)
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) *3]
        if all([spot == letter for spot in row]):
            return True

        # check colum (div by 3 take remainder)
        col_ind = square % 3
        colum = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in colum]):
            return True

        # check diagonals all the even space (0, 2, 4, 6, 8)
        if square % 2 == 0:
            # left to right
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            # right to left
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # if checks fail no winner
        return False
# defining a function pass in game, x_player, o_player, print_game
def play(game, x_player, o_player, print_game = True):
    # returns winner (letter) if one or none if no winner
    if print_game:
        # print number that correspond to each spot
        game.print_board_num()

    # assign starting letter
    letter = 'x'
    # while game still has empty spaces iterate
    # output of play, returns the winner & break out

    # Get move from the right player
    while game.empty_squares():
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' make a move to square{square}')
                # print new board with space taken
                game.print_board()
                print('') # empty line

            # ends game = current_winner != None
            if game.current_winner:
                if print_game:
                    print(letter + ' winner!')
                # returns letter that gave win
                return letter

            # switches players x and o
            # alternate letter after player moves
#            if letter == 'x':
#                letter = 'o'
#            else:
#                letter = 'x'
            # or alternate letter after player moves
            letter = 'o' if letter == 'x' else 'x'

        # short break in play time
        time.sleep(0.7)

    if print_game:
        print('It\'s a tie!')

# let's play game
if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer('o')
    # instance of game
    t = TicTacToe()
    # set play
    play(t, x_player, o_player, print_game=True)



# space1 = TicTacToe()
# gb_empty = ''
# gb_side_line = '|'
# gb_bottom_line = '__'

# check index[0, 2, 4] on line [1-3]
# b_top = ['__', gb_side_line, '__',  gb_side_line, '__']
# b_middle = ['__', gb_side_line, '__', gb_side_line, '__']
# b_bottom = ['  ', gb_side_line, '  ', gb_side_line, '  ']
#for item in game_board_design:
#    print(item)
# my_ttt_board = ['__', gb_side_line, '__',  gb_side_line, '__', '__', gb_side_line, '__', gb_side_line, '__', '  ', gb_side_line, '  ', gb_side_line, '  ']
# print(b_top[0] + b_top[1] + b_top[2] + b_top[3] + b_top[4])
# print(b_middle[0] + b_middle[1] + b_middle[2] + b_middle[3] + b_middle[4])
# print(b_bottom[0] + b_bottom[1] + b_bottom[2] + b_bottom[3] + b_bottom[4])

# print(my_ttt_board[0] + my_ttt_board[1] + my_ttt_board[2] + my_ttt_board[3] + my_ttt_board[4])
# print(my_ttt_board[5] + my_ttt_board[6] + my_ttt_board[7] + my_ttt_board[8] + my_ttt_board[9])
# print(my_ttt_board[10] + my_ttt_board[11] + my_ttt_board[12] + my_ttt_board[13] + my_ttt_board[14])