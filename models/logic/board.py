import random

from models.logic.cell import Cell

from models.logic.Bacterium import *

from models.logic.Bacteriophage import Bacteriophage


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

    @staticmethod
    def from_string(board_str):
        rows = board_str.split('\n')
        n_rows = len(rows)
        if n_rows < 1:
            raise ValueError(f'Invalid number of rows: {n_rows}')
        matrix = [row.split('|') for row in rows]
        n_cols = len(matrix[0])
        if n_cols < 1:
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

    def set_antibiotics(self, row, colum, cant: int):
        self.__board[row][colum]._antibiotics = cant

    def add_antibiotic(self, row, colum):
        self.__board[row][colum].add_antibiotic()

    def set_bacteriophage(self, row, colum, bacteriophage:Bacteriophage):
        self.__board[row][colum]._bacteriophages = bacteriophage

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


    def move_entity(self):
        new_board = Board(self.__rows, self.__columns)
        new_board.set_position_spawn_other(self.__position_spawn_other)
        new_board.set_position_spawn_bacterium(self.__position_spawn_bacterium)
        for row in range(self.__rows):
            for colum in range(self.__columns):
            #si existen bacterias y antibioticos en la misma celda, aplico las reglas de cruzamiento
                new_board = self.move_entities(row, colum, new_board)
        return new_board

    def crossing_board(self):
        for row in range(self.__rows):
            for colum in range(self.__columns):
            #si existen bacterias y antibioticos en la misma celda, aplico las reglas de cruzamiento
                self.__board[row][colum].update_cell()

    def move_entities(self, x, y, new_board):
        #board_actualizado = Board(self.__rows,self.__columns)
        #board_actualizado.set_position_spawn_other(self.__position_spawn_other)
        #board_actualizado.set_position_spawn_bacterium(self.__position_spawn_bacterium)
        new_x = None
        new_y = None
        for bacterium in self.__board[x][y]._bacteria:
            resultMoves = self.get_random_move(x, y)
            if resultMoves != None:
                new_x, new_y = resultMoves
                new_board.get_cell(new_x,new_y)._bacterium = bacterium
                bacterium.add_move()

        for _ in range(self.__board[x][y]._antibiotics):
            resultMoves = self.get_random_move(x, y)
            if resultMoves != None:
                new_x, new_y = resultMoves
                new_board.get_cell(new_x,new_y).add_antibiotic()

        for bacteriophage in self.__board[x][y]._bacteriophages:
            resultMoves = self.get_random_move(x, y)
            if resultMoves != None:
                new_x, new_y = resultMoves
                bacteriophage.add_move()
                new_board.get_cell(new_x,new_y).add_bacteriophage(bacteriophage._infection(bacteriophage._infection-1))
        return new_board
