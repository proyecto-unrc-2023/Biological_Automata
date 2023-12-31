import random

from models.logic.CellAntibiotic import CellAntibiotic
from models.logic.CellBacteriophage import CellBacteriophage
from models.logic.Bacterium import Bacterium
from models.logic.Bacteriophage import Bacteriophage
from models.logic.Antibiotic import Antibiotic
from models.logic.Game_Mode import Game_Mode

class Board:

    def __init__(self, mode:Game_Mode ,rows, columns, overpopulation):
        self.__position = []
        self.__rows = rows
        self.__columns = columns
        self.__position_spawn_bacterium = None
        self.__position_spawn_other = None
        self.__game_mode = mode
        self.__cant_overpopulation = overpopulation
        self.__board = []
        self.create_board()

    def create_board(self):
        for _ in range(self.__rows):
            curr_row = []
            for _ in range(self.__columns):
                if self.__game_mode == Game_Mode.ANTIBIOTIC:
                    curr_row.append(CellAntibiotic())
                if self.__game_mode == Game_Mode.BACTERIOPHAGE:
                    curr_row.append(CellBacteriophage())
            self.__board.append(curr_row)

    @property
    def _rows(self):
        return self.__rows

    @property
    def _columns(self):
        return self.__columns

    @property
    def _board(self):
        return self.__board

    def set_cant_overpopulation(self, cant):
        self.__cant_overpopulation = cant

    def get_cell(self, row, column):
        return self.__board[row][column]

    def set_position_spawn_bacterium(self, position):
        try:
            self.__board[position[0]][position[1]].set_spawn()
        except ValueError as e:
            raise e
        self.__position_spawn_bacterium = position

    def get_position_spawn_bacterium(self):
        return self.__position_spawn_bacterium

    def set_position_spawn_other(self, position):
        try:
            self.__board[position[0]][position[1]].set_spawn()
        except ValueError as e:
            raise e
        self.__position_spawn_other = position

    def get_position_spawn_other(self):
        return self.__position_spawn_other

    def get_position(self):
        return self.__position

    def set_position(self, positions):
        self.__position = positions

    def is_empty(self):
        for row in range(self.__rows):
            for colum in range(self.__columns):
                if not self.__board[row][colum].is_empty():
                    return False
        return True

    def add_bacterium(self, row, colum, bacterium: Bacterium):
        bacterium.set_pos(row, colum)
        self.__board[row][colum].add_bacterium(bacterium)
        self.__position.append(bacterium)

    def add_antibiotic(self, row, colum, antibiotic: Antibiotic):
        antibiotic.set_pos(row, colum)
        self.__board[row][colum].add_antibiotic(antibiotic)
        self.__position.append(antibiotic)

    def add_bacteriophage(self, row, colum, bacteriophage: Bacteriophage):
        bacteriophage.set_pos(row, colum)
        self.__board[row][colum].add_bacteriophage(bacteriophage)
        self.__position.append(bacteriophage)

    def get_random_move(self, i, j):
        possible_moves = self.get_possible_moves(i, j)
        if not possible_moves:
            return None
        random_move = random.choice(possible_moves)
        return random_move

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
        for pos in position:
            aux.append(pos.get_pos())

        return list(set(aux))

    def move_all_entities(self):
        new_board = Board(self.__game_mode,self.__rows, self.__columns, self.__cant_overpopulation)
        new_board.create_board()
        new_board.set_position_spawn_bacterium(self.__position_spawn_bacterium)
        new_board.set_position_spawn_other(self.__position_spawn_other)

        lista = self.position_ocupped(self.__position)

        for pos in lista:
            if isinstance(pos[0], int) and isinstance(pos[1], int):
                new_board = self.move_entities(pos[0], pos[1], new_board)
        return new_board

    def crossing_board(self):
        lista = self.position_ocupped(self.__position)
        self.__position.clear()

        for pos in lista:
            if isinstance(pos[0], int) and isinstance(pos[1], int):
                celda = self.__board[pos[0]][pos[1]]
                celda.update_cell(pos[0], pos[1], self.__cant_overpopulation)
                self.__position.extend(celda.get_bacteria())
                if self.__game_mode == Game_Mode.ANTIBIOTIC:
                    self.__position.extend(celda.get_antibiotics())

                if self.__game_mode == Game_Mode.BACTERIOPHAGE:
                    self.__position.extend(celda.get_bacteriophages())

    def move_entities(self, x, y, new_board):
        new_x = None
        new_y = None
        for bacterium in self.__board[x][y].get_bacteria():
            resultMoves = self.get_random_move(x, y)
            if resultMoves is not None:
                new_x, new_y = resultMoves
                bacterium.add_move()
                new_board.add_bacterium(new_x, new_y, bacterium)

        if (self.__game_mode == Game_Mode.ANTIBIOTIC):
            for antibiotic in self.__board[x][y].get_antibiotics():
                resultMoves = self.get_random_move(x, y)
                if resultMoves is not None:
                    new_x, new_y = resultMoves
                    new_board.add_antibiotic(new_x, new_y, antibiotic)

        if (self.__game_mode == Game_Mode.BACTERIOPHAGE):
            for bacteriophage in self.__board[x][y].get_bacteriophages():
                resultMoves = self.get_random_move(x, y)
                if resultMoves is not None:
                    new_x, new_y = resultMoves
                    bacteriophage.add_move()
                    new_board.add_bacteriophage(new_x, new_y, bacteriophage)

        return new_board

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

    def _row_to_string(self, row, row_num):
        spawn_bac = self.__position_spawn_bacterium
        spawn_other = self.__position_spawn_other
        res = ''
        columns = len(row)
        for col in range(columns):
            if (spawn_other is not None and row_num == spawn_other[0] and col == spawn_other[1]):
                res += 'so'
            else:
                if (spawn_bac is not None and row_num == spawn_bac[0] and col == spawn_bac[1]):
                    res += 'sb'
                else:
                    res += str(row[col])
            if col < columns - 1:
                res += '|'
        return res

    def __str__(self):
       res = ''
       for row_num in range(self.__rows):
           res += self._row_to_string(self.__board[row_num], row_num)
           if row_num < self.__rows - 1:
               res += '\n'
       return res

    def where_are_entities(self):
        occupied_cells = []
        for row in range(self.__rows):
            for column in range(self.__columns):
                if not self.__board[row][column].is_empty() and not self.__board[row][column].get_spawn():
                    occupied_cells.append((row, column))
        return occupied_cells

    def how_many_entities(self, type):
        occupied_cells = self.where_are_entities()
        cant_entities = 0
        for cell in occupied_cells:
            if type == 'bacteriofagos':
                cant_entities += self.__board[cell[0]][cell[1]].get_cant_bacteriophage()
            elif type == 'bacterias':
                cant_entities += self.__board[cell[0]][cell[1]].get_cant_bacteria()
            elif type == 'antibioticos':
                cant_entities += self.__board[cell[0]][cell[1]].get_cant_antibiotic()
            else:
                cant_entities += self.__board[cell[0]][cell[1]].cant_ente(type)

        return cant_entities

    def move_entity(self, new_x, new_y, x, y, board, entity):
        if isinstance(entity, Bacterium):
            entity.add_move()
            board.add_bacterium(new_x, new_y, entity)
            board.get_cell(x, y).get_bacteria().remove(entity)
            aux = board.get_cell(x, y).get_cant_bacteria()
            board.get_cell(x, y).set_cant_bacteria(aux - 1)
        elif isinstance(entity, Bacteriophage):
            entity.add_move()
            board.add_bacteriophage(new_x, new_y, entity)
            board.get_cell(x, y).get_bacteriophages().remove(entity)
            aux = board.get_cell(x, y).get_cant_bacteriophage()
            board.get_cell(x, y).set_cant_bacteriophage(aux - 1)
        elif isinstance(entity, Antibiotic):
            board.add_antibiotic(new_x, new_y, entity)
            board.get_cell(x, y).get_antibiotics().remove(entity)
            aux = board.get_cell(x, y).get_cant_antibiotic()
            board.get_cell(x, y).set_cant_antibiotic(aux - 1)
        return board
