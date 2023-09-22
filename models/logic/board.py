
from models.logic.cell import Cell

class Board:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__position_spawn_other = None
        self.__position_spawn_bacterium = None
        self.__board = []		
        for _ in range(self.__rows):
            curr_row = []
            for _ in range(self.__columns):
                curr_row.append(Cell())
            self.__board.append(curr_row)

    @property
    def _rows(self):
        return self.__rows

    @property
    def _columns(self):
        return self.__columns

    def get_cell(self, row, column):
        return self.__board[row][column]
		
    def get_position_spawn_other(self):
        return self.__position_spawn_other

   
    def set_position_spawn_other(self, row, colum):
        try:
            self.__board[row][colum].set_spawn_other()
        except ValueError:
            raise ValueError(f'no se puede poner un spawn')
        self.__position_spawn_other = (row,colum)
  
    def get_position_spawn_bacterium(self):
        return self.__position_spawn_bacterium
        
    def set_position_spawn_bacterium(self, row, colum):
        try:
            self.__board[row][colum].set_spawn_bacterium()
        except ValueError:
            raise ValueError(f'no se puede poner un spawn')
        self.__position_spawn_bacterium = (row,colum)


    def is_empty(self):
        for row in range(self.__rows):
            for colum in range(self.__columns):
                if not(self.__board[row][colum].is_empty()):
                    return False
        return True





