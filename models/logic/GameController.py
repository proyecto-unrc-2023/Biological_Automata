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