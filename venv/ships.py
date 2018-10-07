


class Ship(object):
    
    def __init__(self):
        pass
    
    
    #picks a random row for the ship to spawn in
    def row(self, board):
        ship_row = board.random_row()
        
        return ship_row
    
    #picks a random colomn of that row to spawn in
    def col(self, board):
        ship_col = board.random_col()
        return ship_col

    #prints out flavor text describing the ship
    def describe(self):
        print("This is a ship!")