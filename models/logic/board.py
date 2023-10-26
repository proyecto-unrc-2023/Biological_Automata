import random

from models.logic.cell import Cell
from models.logic.CellAntibiotic import CellAntibiotic
from models.logic.CellBacteriophage import CellBacteriophage

from models.logic.Bacterium import Bacterium

from models.logic.Bacteriophage import Bacteriophage

from models.logic.Antibiotic import Antibiotic



class Board:

    def __init__(self, rows, columns):
        self.__position = []
        self.__rows = rows
        self.__columns = columns
        self.__position_spawn_other = None
        self.__position_spawn_bacterium = None
        self.__board = []
        self.__game_mode = None

    def set_gameMode(self, mode):
        self.__game_mode = mode

    def create_board(self):
        for _ in range(self.__rows):
            curr_row = []
            for _ in range(self.__columns):
                if (self.__game_mode == 1):
                    curr_row.append(CellAntibiotic())
                else:
                    curr_row.append(CellBacteriophage())
            self.__board.append(curr_row)

    #@staticmethod
    #def from_string(board_str):
    #    rows = board_str.split('\n')
    #    n_rows = len(rows)
    #    if n_rows <= 1:
    #        raise ValueError(f'Invalid number of rows: {n_rows}')
    #    matrix = [row.split('|') for row in rows]
    #    n_cols = len(matrix[0])
    #    if n_cols <= 1:
    #        raise ValueError(f'Invalid number of columns: {n_cols}')
    #    for row in range(n_rows):
    #        row_len = len(matrix[row])
    #        if row_len != n_cols:
    #            raise ValueError(f'Invalid number of columns: {row_len}')
#
    #    return Board._from_string_matrix(n_rows, n_cols, matrix)

    #@staticmethod
    #def _from_string_matrix(rows, cols, matrix):
    #    new_board = Board(rows, cols)
    #    for row in range(rows):
    #        for col in range(cols):
    #            for i in matrix[row][col].__str__():
    #                curr_cell = i
    #                new_board.put_celda(row, col, Cell.from_string(curr_cell))
    #    return new_board

    #@staticmethod
    #def _row_to_string(row):
    #    res = ''
    #    columns = len(row)
    #    for col in range(columns):
    #        res += row[col].__str__()
    #        if col < columns - 1:
    #            res += '|'
    #    return res

    #def __str__(self):
    #    res = ''
    #    for row_num in range(self.__rows):
    #        res += Board._row_to_string(self.__board[row_num])
    #        if row_num < self.__rows - 1:
    #            res += '\n'
    #    return res
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

    def get_position(self):
        return self.__position

    def set_position(self, positions):
        self.__position = positions

    def set_position_spawn_other(self, position):
        try:
            self.__board[position[0]][position[1]].set_spawn(True)
        except ValueError:
            raise ValueError('no se puede poner un spawn')
        self.__position_spawn_other = position

    ##Devuelve la tupla
    def get_position_spawn_bacterium(self):
        return self.__position_spawn_bacterium

    def set_position_spawn_bacterium(self, position):
        try:
            self.__board[position[0]][position[1]].set_spawn(True)
        except ValueError:
            raise ValueError('no se puede poner un spawn')
        self.__position_spawn_bacterium = position

    def is_empty(self):
        for row in range(self.__rows):
            for colum in range(self.__columns):
                if not (self.__board[row][colum].is_empty()):
                    return False
        return True

    def add_bacterium(self, row, colum, bacterium: Bacterium):
        bacterium.set_pos(row, colum)
        self.__board[row][colum].add_bacterium(bacterium)
        self.__position.append(bacterium)

    def add_antibiotic(self, row, colum, antibiotic: Antibiotic):
        antibiotic.set_pos(row, colum)
        cell = self.__board[row][colum]
        cell.add_antibiotic(antibiotic)
        self.__position.append(antibiotic)

    def add_bacteriophage(self, row, colum, bacteriophage: Bacteriophage):
        bacteriophage.set_pos(row, colum)
        self.__board[row][colum].add_bacteriophage(bacteriophage)
        self.__position.append(bacteriophage)

    ##CHEKEENLO ALGUN DIA
    def __eq__(self, other):
        if self.__rows != other.__rows:
            return False
        if self.__columns != other.__columns:
            return False
        if self.__position_spawn_bacterium != other.__position_spawn_bacterium:
            return False
        if self.__position_spawn_other != other.__position_spawn_other:
            return False
        for row in range(self.__rows):
            for colum in range(self.__columns):
                if not (self.__board[row][colum].__eq__(other.__board[row][colum])):
                    return False
        return True

    # new
    def get_random_move(self, i, j):
        possible_moves = self.get_possible_moves(i, j)
        if possible_moves:
            random_move = random.choice(possible_moves)
            return random_move
        else:
            return None

    def get_possible_moves(self, i, j):
        moves = []
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if (x, y) != (i, j):
                    if 0 <= x < self.__rows and 0 <= y < self.__columns:
                        if not self.__board[x][y].get_spawn():
                            moves.append((x, y))
        return moves

    def position_ocupped(self, position):
        aux = []
        for i in range(len(position)):
            aux.append(position[i].get_pos())

        return list(set(aux))

    def move_all_entities(self):
        new_board = Board(self.__rows, self.__columns)
        new_board.set_gameMode(self.__game_mode)
        new_board.create_board()
        new_board.set_position_spawn_other(self.__position_spawn_other)
        new_board.set_position_spawn_bacterium(self.__position_spawn_bacterium)

        lista = self.position_ocupped(self.__position)

        for j in range(len(lista)):
            pos = lista[j]
            if isinstance(pos[0], int) and isinstance(pos[1], int):
                new_board = self.move_entities(pos[0], pos[1], new_board)
        return new_board

    def crossing_board(self):
        lista = self.position_ocupped(self.__position)
        self.__position.clear()

        for j in range(len(lista)):
            pos = lista[j]
            if isinstance(pos[0], int) and isinstance(pos[1], int):
                celda = self.__board[pos[0]][pos[1]]
                celda.update_cell(pos[0], pos[1])
                self.__position.extend(celda.get_bacteria())
                if (self.__game_mode == 1):
                    self.__position.extend(celda.get_antibiotics())
                else:
                    self.__position.extend(celda.get_bacteriophages())

    def move_entities(self, x, y, new_board):
        new_x = None
        new_y = None
        for bacterium in self.__board[x][y].get_bacteria():
            resultMoves = self.get_random_move(x, y)
            if resultMoves != None:
                new_x, new_y = resultMoves
                bacterium.add_move()
                new_board.add_bacterium(new_x, new_y, bacterium)
        if (self.__game_mode == 1):
            for antibiotic in self.__board[x][y].get_antibiotics():
                resultMoves = self.get_random_move(x, y)
                if resultMoves != None:
                    new_x, new_y = resultMoves
                    new_board.add_antibiotic(new_x, new_y, antibiotic)
        else:
            for bacteriophage in self.__board[x][y].get_bacteriophages():
                resultMoves = self.get_random_move(x, y)
                if resultMoves != None:
                    new_x, new_y = resultMoves
                    bacteriophage.add_move()
                    new_board.add_bacteriophage(new_x, new_y, bacteriophage)

        return new_board

    def move_entity(self, new_x, new_y, x, y, board, entity):
        if isinstance(entity, Bacterium):
            entity.add_move()
            board.add_bacterium(new_x, new_y, entity)
            board.get_cell(x, y).get_bacteria().remove(entity)
        elif isinstance(entity, Bacteriophage):
            entity.add_move()
            board.set_bacteriophage(new_x, new_y, entity)
            board.get_cell(x, y).get_bacteriophages().remove(entity)
        else:
            board.add_antibiotic(new_x, new_y, entity)
            board.get_cell(x, y).get_antibiotics().remove(entity)

        return board

    ##CHEQUEAR ESTO
    def where_are_entities(self):
        occupied_cells = []
        for row in range(self.__rows):
            for colum in range(self.__columns):
                if not self.__board[row][colum].is_empty() and not self.__board[row][colum].get_spawn():
                    occupied_cells.append((row, colum))
        return occupied_cells

    def how_many_entities(self, type):
        occupied_cells = self.where_are_entities()
        cant_entities = 0
        for cell in occupied_cells:
            cant_entities += self.__board[cell[0]][cell[1]].cant_ente(type)
        return cant_entities
