from random import randint



class Board(object):
    board = []

    def __init__(self, board_width, ):
        self.board_width = board_width
        board = []
    
    #creates a board of "O"s in a size determined by the user
    def create_board(self):
        for x in range(0, self.board_width):
           self.board.append(["O"] * self.board_width)

    #prints the board to the screen
    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    #chooses a random row of the board
    def random_row(self):
        return randint(0, len(self.board) - 1)
    
    #chooses a random colomn of the board
    def random_col(self):
        return randint(0, len(self.board[0]) - 1)
    
    