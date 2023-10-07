from enum import Enum
from models.logic.board import Board
from models.logic.Bacterium import BacteriumNormal
from models.logic.Bacteriophage import Bacteriophage

class Game_Mode(Enum):
    ANTIBIOTIC = 1      #Modo de juego
    BACTERIOPHAGE = 2   #Modo de juego
    #Modo de juego BACTERIUM (Si no setea spawn de "other")

class Game_State(Enum):
    NOT_STARTER = 1     #Todavia no empezo el juego
    CONFIG_GAME = 2     #CONFIGURA LOS PARAMETROS
    START_GAME = 3      #Inicio de juego
    FINISH_GAME = 4

class GameController:

    def __init__(self):
        #al iniciar se dejan valores por defecto que el usuario puede modificar si quiere
        self.__game_state = Game_State.NOT_STARTER
        self.__game_mode = None
        self.__board = Board(30,50)             #por defecto
        self.__reproduction_moves = 3           #todavia no usado
        self.__recovery_moves = 6               #todavia no usado
        self.__overpopulation_cant = 4          #valor no modificable
        self.__exploit_moves = 4                #todavia no usado
        self.__cant_bacterium = 10
        self.__cant_other = 20
        self.__frecuency_bacterium = 2
        self.__frecuency_other = 2
        self.__movements = 0


    def config(self, b_rows, b_columns):
        if (self.__game_state == Game_State.NOT_STARTER):
            self.__game_state = Game_State.CONFIG_GAME
            self.__board = Board(b_rows, b_columns)
            self.__reproduction_moves = 3
            self.__recovery_moves = 6
            self.__exploit_moves = 4
            self.__frecuency_bacterium = 2
            self.__frecuency_other = 2
            self.__cant_bacterium = 10
            self.__cant_other = 20

    @property
    def _game_mode(self):
        return self.__game_mode

    @_game_mode.setter
    def _game_mode(self, mode: Game_Mode):
        spawn = self.__board.get_position_spawn_bacterium()
        if (self.__game_state == Game_State.CONFIG_GAME and (spawn != None)):
            self.__game_mode = mode
            self.__game_state = Game_State.START_GAME


    def generate_bacterium(self):
        spawn = self.__board.get_position_spawn_bacterium()
        if spawn != None:
            move = self.__board.get_random_move(spawn[0], spawn[1])
            bacterium = BacteriumNormal(0)
            if move != None:
                self._board.set_bacterium(move[0], move[1], bacterium)
                self.__cant_bacterium -= 1

    def generate_other(self):
        spawn = self.__board.get_position_spawn_other()
        if spawn != None:
            move = self.__board.get_random_move(spawn[0], spawn[1])
            if move != None:
                if self.__game_mode == Game_Mode.ANTIBIOTIC:
                    self._board.set_antibiotics(move[0],move[1], 1)
                    self.__cant_other -= 1
                else:
                    ente = Bacteriophage(4)
                    self.__board.set_bacteriophage(move[0], move[1], ente)
                    self.__cant_other -= 1


    def generate_entities(self):
        if(self.__cant_bacterium > 0 and self.__movements % self.__frecuency_bacterium == 0):
            self.generate_bacterium()

        if(self.__game_mode == Game_Mode.ANTIBIOTIC and self.__cant_other > 0 and self.__movements % self.__frecuency_other == 0):
            self.generate_other()

        if(self.__game_mode == Game_Mode.BACTERIOPHAGE and self.__cant_other > 0 and self.__movements % self.__frecuency_other == 0):
            self.generate_other()


    def refresh_board(self):
        if (self.__game_state == Game_State.START_GAME):
            actualizado = self._board.move_all_entities()
            self.__board = actualizado
            self.generate_entities()
            actualizado.crossing_board()
            self.__movements += 1


    def stop(self, b:bool):
        if (self.__game_state == Game_State.START_GAME and b == True):
            self.__game_state = Game_State.FINISH_GAME


############ SETTERS Y GETTERS ###############

    @property
    def _game_state(self):
        return self.__game_state

    @_game_state.setter
    def _game_state(self, mode: Game_State):
        self.__game_state = mode


    @property
    def _board(self):
        return self.__board

    @property
    def _frecuency_bacterium(self):
        return self.__frecuency_bacterium

    @property
    def _frecuency_other(self):
        return self.__frecuency_other

    @property
    def _cant_bacterium(self):
        return self.__cant_bacterium

    @property
    def _cant_other(self):
        return self.__cant_other

    @_frecuency_bacterium.setter
    def _frecuency_bacterium(self, new_frec):
        self.__frecuency_bacterium = new_frec

    @_frecuency_other.setter
    def _frecuency_other(self, new_frec):
        self.__frecuency_other = new_frec
    @_cant_bacterium.setter
    def _cant_bacterium(self, new_cant):
        self.__cant_bacterium = new_cant

    @_cant_other.setter
    def _cant_other(self, new_cant):
        self.__cant_other = new_cant


    def set_spawn_bacterium(self, position):
        self.__board.set_position_spawn_bacterium(position)

    def set_spawn_other(self, position):
        self.__board.set_position_spawn_other(position)
