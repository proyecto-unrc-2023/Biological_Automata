
from models.logic.celda import Celda


class Board:


    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.position_spawn_other = None
        self.position_spawn_baterium = None
        self.board = []		
        for _ in range(self.rows):
            curr_row = []
            for _ in range(self.columns):
                curr_row.append(Celda())
            self.board.append(curr_row)


    def get_celda(self, row, column):
        return self.board[row][column]
		

    def get_position_spawn_other(self):
        return self.position_spawn_other


    def set_position_spawn_other(self, row, colum):
        x = row
        y = colum 
        self.board[x][y].create_spawn_other()
        self.position_spawn_other = (x,y)

    def get_position_spawn_bacterium(self):
        return self.position_spawn_bacterium
        

    def set_position_spawn_bacterium(self, row, colum):
        x = row
        y = colum
        self.board[x][y].create_spawn_bacterium()
        self.position_spawn_bacterium = (x,y)





