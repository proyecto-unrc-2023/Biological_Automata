from enum import Enum
from Board import Board

class Game_Mode(Enum):
    NOT_STARTER = 1     #Todavia no empezo el juego
    CELLS_PLACEMENT = 2 #JUGADOR ELIJE LOS SPAWNS
    ANTIBIOTIC = 3      #Modo de juego
    BACTERIOPHAGE = 4   #Modo de juego
    BACTERIUM = 5       #Modo de juego

class gameController:

    def __init__(self):
        #se pueden dejar algunos valores por defecto y que el usuario los modifique si quiere
        self.__game_mode = Game_Mode.NOT_STARTER
        self.__board = Board(30, 50)
        self.__reproduction_moves = 3
        self.__recovery_moves = 6
        self.__overpopulation_cant = 4             ##USUARIO NO PUEDE ELEGIRLO
        self.__exploit_moves = 4

    @staticmethod
    def set_spawn_bacterium():
        pass

    @staticmethod
    def set_spawn_antibiotic():
        pass

    def get_mode(self):
        return self.__game_mode
