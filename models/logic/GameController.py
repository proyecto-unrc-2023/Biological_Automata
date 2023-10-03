from enum import Enum
from models.logic.board import Board
from models.logic.Bacterium import BacteriumNormal
from models.logic.Bacteriophage import Bacteriophage

class Game_Mode(Enum):
    NOT_STARTER = 1     #Todavia no empezo el juego
    CONFIG_GAME = 2     #JUGADOR ELIJE LOS SPAWNS
    ANTIBIOTIC = 3      #Modo de juego
    BACTERIOPHAGE = 4   #Modo de juego
    BACTERIUM = 5       #Modo de juego

class GameController:

    def __init__(self):
        #se pueden dejar algunos valores por defecto y que el usuario los modifique si quiere
        self.__game_mode = Game_Mode.NOT_STARTER
        self.__board = Board(0,0)
        self.__reproduction_moves = 0
        self.__recovery_moves = 0
        self.__overpopulation_cant = 4
        self.__exploit_moves = 0
        self.__cant_bacteria = 0
        self.__cant_bacteriophage = 0
        self.__cant_antibiotic = 0
        self.__frecuency = 0

    def set_mode(self, mode: Game_Mode):
        self.__game_mode = mode

    def get_mode(self):
        return self.__game_mode

    def config(self, b_rows, b_columns):
        self.__game_mode = Game_Mode.CONFIG_GAME
        self.__board = Board(b_rows, b_columns)
        self.__reproduction_moves = 3
        self.__recovery_moves = 6
        self.__exploit_moves = 4
        self.__cant_bacteria = 10
        self.__cant_bacteriophage = 10
        self.__cant_antibiotic = 20

    @property
    def _board(self):
        return self.__board

    @property
    def _frecuency(self):
        return self.__frecuency

    @property
    def _cant_bacteria(self):
        return self.__cant_bacteria

    @property
    def _cant_antibiotic(self):
        return self.__cant_antibiotic

    @property
    def _cant_bacteriophage(self):
        return self.__cant_bacteriophage

    def set_frecuency(self, new_frec):
        self.__frecuency = new_frec

    def set_cant_bacteria(self, new_cant):
        self.__cant_bacteria = new_cant

    def set_cant_antibiotic(self, new_cant):
        self.__cant_antibiotic = new_cant

    def set_cant_bacteriophage(self, new_cant):
        self.__cant_bacteriophage = new_cant

    def set_spawn_bacterium(self, position):
        self.__board.set_position_spawn_bacterium(position)

    def set_spawn_other(self, position):
        self.__board.set_position_spawn_other(position)

    def generate_bacterium(self):
        spawn = self.__board.get_position_spawn_bacterium()
        if spawn != None:
            move = self.__board.get_random_move(spawn[0], spawn[1])
            bacterium = BacteriumNormal(0)
            if move != None:
                self._board.set_bacterium(move[0], move[1], bacterium)
                self.__cant_bacteria -= 1

    def generate_other(self):
        spawn = self.__board.get_position_spawn_other()
        if spawn != None:
            move = self.__board.get_random_move(spawn[0], spawn[1])
            if move != None:
                if self.__game_mode == Game_Mode.ANTIBIOTIC:
                    self._board.set_antibiotics(move[0],move[1], 1)
                    self.__cant_antibiotic -= 1
                else:
                    ente = Bacteriophage(4)
                    self.__board.set_bacteriophage(move[0], move[1], ente)
                    self.__cant_bacteriophage -= 1


    def generate_entities(self):
        if(self.__cant_bacteria > 0):
            self.generate_bacterium()
        elif(self.__cant_antibiotic > 0):
            self.generate_other()
        else:
            self.generate_other()


    def refresh_board(self):
        actualizado = self._board.move_entity()
        actualizado.crossing_board()
        self.__board = actualizado
        self.__frecuency += 1
        if (self.__frecuency == 2):
            self.generate_entities()
            self.__frecuency = 0

