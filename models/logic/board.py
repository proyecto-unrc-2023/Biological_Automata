import random

from models.logic.cell import Cell

from models.logic.Bacterium import *

from models.logic.Bacteriophage import Bacteriophage

from models.logic.Antibiotic import *

class Board:

    def __init__(self, rows, columns):
        self.__position = []
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

    @staticmethod
    def from_string(board_str):
        rows = board_str.split('\n')
        n_rows = len(rows)
        if n_rows <= 1:
            raise ValueError(f'Invalid number of rows: {n_rows}')
        matrix = [row.split('|') for row in rows]
        n_cols = len(matrix[0])
        if n_cols <= 1:
            raise ValueError(f'Invalid number of columns: {n_cols}')
        for row in range(n_rows):
            row_len = len(matrix[row])
            if row_len != n_cols:
                raise ValueError(f'Invalid number of columns: {row_len}')

        return Board._from_string_matrix(n_rows, n_cols, matrix)

    @staticmethod
    def _from_string_matrix(rows, cols, matrix):
        new_board = Board(rows, cols)
        for row in range(rows):
            for col in range(cols):
                for i in matrix[row][col].__str__():
                    curr_cell = i
                    new_board.put_celda(row, col, Cell.from_string(curr_cell))
        return new_board

    @staticmethod
    def _row_to_string(row):
        res = ''
        columns = len(row)
        for col in range(columns):
            res += row[col].__str__()
            if col < columns - 1:
                res += '|'
        return res

    def __str__(self):
        res = ''
        for row_num in range(self._rows):
            res += Board._row_to_string(self.__board[row_num])
            if row_num < self._rows - 1:
                res += '\n'
        return res

    @property
    def _rows(self):
        return self.__rows

    @property
    def _board(self):
        return self.__board

    @property
    def _columns(self):
        return self.__columns

    def put_celda(self, row, column, cell):
        self.__board[row][column] = cell

    def get_cell(self, row, column):
        return self.__board[row][column]


    def get_position_spawn_other(self):
        return self.__position_spawn_other

    def get_eficientr(self):
        return self.__position
    
    def set_eficiente(self):
        pass


    def set_position_spawn_other(self, position):
        try:
            self.__board[position[0]][position[1]].set_spawn_other()
        except ValueError:
            raise ValueError(f'no se puede poner un spawn')
        self.__position_spawn_other = position

    def get_position_spawn_bacterium(self):
        return self.__position_spawn_bacterium

    def set_position_spawn_bacterium(self, position):
        try:
            self.__board[position[0]][position[1]].set_spawn_bacterium()
        except ValueError:
            raise ValueError(f'no se puede poner un spawn')
        self.__position_spawn_bacterium = position

    def is_empty(self):
        for row in range(self.__rows):
            for colum in range(self.__columns):
                if not(self.__board[row][colum].is_empty()):
                    return False
        return True

    def set_bacterium(self, row, colum, bacterium:Bacterium):
        self.__board[row][colum]._bacterium = bacterium
        bacterium.set_pos(row, colum)
        self.__position.append(bacterium)


    def set_antibiotics(self, row, colum, cant: int): 
        for i in range(cant):
            antibiotic = Antibiotic()
            antibiotic.set_pos(row, colum)
            self.__board[row][colum].add_antibiotic(antibiotic)
            self.__position.append(antibiotic)

        

    def add_antibiotic(self, row, colum, antibiotic: Antibiotic):
        antibiotic.set_pos(row, colum)  
        self.__board[row][colum].add_antibiotic(antibiotic)     
        self.__position.append(antibiotic)

    def set_bacteriophage(self, row, colum, bacteriophage:Bacteriophage):
        self.__board[row][colum]._bacteriophages = bacteriophage
        bacteriophage.set_pos(row,colum)
        self.__position.append(bacteriophage)
        

    def __eq__(self, other):
        if self.__rows == other.__rows and self.__columns == other.__columns and self.__position_spawn_bacterium == other.__position_spawn_bacterium and self.__position_spawn_other == other.__position_spawn_other:
            for row in range(self.__rows):
                for colum in range(self.__columns):
                    if not(self.__board[row][colum].__eq__(other.__board[row][colum])):
                        return False
            return True
        else:
            return False

    #new
    def get_random_move (self, i, j):
        possible_moves = self.get_possible_moves(i,j)
        if possible_moves:
            random_move = random.choice(possible_moves)
            return random_move
        else:
            return None

    def get_possible_moves(self, i,j):
        moves = []
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                if (x,y) != (i, j):
                    if 0 <= x < self.__rows and 0 <= y < self.__columns:
                        if not self.__board[x][y].is_spawn():
                            moves.append((x, y))
        return moves


    def move_all_entities(self):
        new_board = Board(self.__rows, self.__columns)
        new_board.set_position_spawn_other(self.__position_spawn_other)
        new_board.set_position_spawn_bacterium(self.__position_spawn_bacterium)
        for i in range(len(self.__position)):
                pos = self.__position[i].get_pos()
                if pos != None:
                    new_board = self.move_entities(pos[0],pos[1], new_board)
       
        return new_board

    def crossing_board(self):
        for row in range(self._rows):
            for column in range(self._columns):
               self.__board[row][column].update_cell()
               self.__position.extend(self.__board[row][column]._bacteria)
               self.__position.extend(self.__board[row][column]._bacteriophages)
               self.__position.extend(self.__board[row][column].get_antibiotics())
   

    # def move_entities(self, x, y):
    #     new_board = Board(self.__rows, self.__columns)
    def move_entities(self, x, y, new_board):
        new_x = None
        new_y = None
        for bacterium in self.__board[x][y]._bacteria:
            resultMoves = self.get_random_move(x, y)
            if resultMoves != None:
                new_x, new_y = resultMoves
                bacterium.add_move()
                new_board.get_cell(new_x,new_y)._bacterium = bacterium

        for antibiotic in self.__board[x][y].get_antibiotics():
            resultMoves = self.get_random_move(x, y)
            if resultMoves != None:
                new_x, new_y = resultMoves
                new_board.get_cell(new_x,new_y).add_antibiotic(antibiotic)

        for bacteriophage in self.__board[x][y]._bacteriophages:
            resultMoves = self.get_random_move(x, y)
            if resultMoves != None:
                new_x, new_y = resultMoves
                bacteriophage.add_move()
                new_board.get_cell(new_x,new_y).add_bacteriophage(bacteriophage.infection-1)

        return new_board


    def move_entity(self, new_x,new_y, x,y, board, entity: Entity):
        if isinstance(entity,Bacterium):
                    entity.add_move()
                    board.get_cell(new_x,new_y)._bacterium = entity
                    board.get_cell(x,y)._bacteria.remove(entity)
        elif isinstance(entity,Bacteriophage):
            entity.add_move()
            board.get_cell(new_x,new_y)._bacteriophages = entity
            board.get_cell(x,y)._bacteriophages.remove(entity)
        else:
            board.get_cell(new_x,new_y).add_antibiotic(entity)
            board.get_cell(x,y).get_antibiotics().remove(entity)
    
        return board

    def where_are_entities(self):
        occupied_cells = []
        for row in range(self.__rows):
            for colum in range(self.__columns):
                if not self.__board[row][colum].is_empty():
                    occupied_cells.append((row,colum))
        return occupied_cells

    def how_many_entities(self, type):
        occupied_cells = self.where_are_entities()
        cant_entities = 0
        for cell in occupied_cells:
            cant_entities += self.__board[cell[0]][cell[1]].cant_ente(type)
        return cant_entities