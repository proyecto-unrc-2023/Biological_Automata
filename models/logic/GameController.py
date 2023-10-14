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
        self.__board = Board(30,50)             # por defecto
        self.__cant_bacterium = 10              # cantidad de bacterias que expulsara
        self.__cant_other = 20                  # cantidad de bacterias que de antibiotico o bacterifago segun el modo                  
        self.__frecuency_bacterium = 2          # frecuencia con el que expulsara bacterias el spawn bacterium
        self.__frecuency_other = 2              # frecuencia con el que expulsara antibiotico o bacterifago el spawn other
        self.__movements = 0                    # un movimiento es una actualizacion del board, y se usara junto con la frecuencia
                                                # para controlar los "spawns"

        # self.__reproduction_moves = 3         # todavia no usado
        # self.__recovery_moves = 6             # todavia no usado
        # self.__overpopulation_cant = 4        # valor no modificable
        # self.__exploit_moves = 4              # todavia no usado


    def config(self, cant_bact, frec_bact, cant_other, frec_other):
        if self._game_state != Game_State.NOT_STARTER:
            raise ValueError("El juego no está en el estado START_GAME")

        self._game_state = Game_State.CONFIG_GAME
        self._frecuency_bacterium = frec_bact
        self._frecuency_other = frec_other
        self._cant_bacterium = cant_bact
        self._cant_other = cant_other
        # self.__reproduction_moves = 3
        # self.__recovery_moves = 6
        # self.__exploit_moves = 4

    def generate_bacterium(self):
        if self._game_state != Game_State.START_GAME:
            raise ValueError("El juego no está en el estado START_GAME")

        spawn = self.__board.get_position_spawn_bacterium()
        if spawn != None:
            move = self._board.get_random_move(spawn[0], spawn[1])
            bacterium = BacteriumNormal(0)
            if move != None:
                self._board.set_bacterium(move[0], move[1], bacterium)
                self._cant_bacterium -= 1

    def generate_other(self):
        if self._game_state != Game_State.START_GAME:
            raise ValueError("El juego no está en el estado START_GAME")

        spawn = self.__board.get_position_spawn_other()
        if spawn != None:
            move = self.__board.get_random_move(spawn[0], spawn[1])
            if move != None:
                if self.__game_mode == Game_Mode.ANTIBIOTIC:
                    self._board.set_antibiotics(move[0],move[1], 1)
                    self._cant_other -= 1
                else:
                    ente = Bacteriophage(4)
                    self._board.set_bacteriophage(move[0], move[1], ente)
                    self._cant_other -= 1

    def generate_entities(self):
        if self._game_state != Game_State.START_GAME:
            raise ValueError("El juego no está en el estado START_GAME")

        if(self._cant_bacterium > 0 and self._movements % self._frecuency_bacterium == 0):
            self.generate_bacterium()

        if(self._game_mode == Game_Mode.ANTIBIOTIC and self._cant_other > 0 and self._movements % self._frecuency_other == 0):
            self.generate_other()

        if(self._game_mode == Game_Mode.BACTERIOPHAGE and self._cant_other > 0 and self._movements % self._frecuency_other == 0):
            self.generate_other()

    def refresh_board(self):
        if self._game_state != Game_State.START_GAME:
            raise ValueError("El juego no está en el estado START_GAME")
        
        actualizado = self._board.move_all_entities()
        self.__board = actualizado
        self.generate_entities()
        actualizado.crossing_board()
        self.__movements += 1


    def stop(self):
        if self.__game_state != Game_State.START_GAME:
            raise ValueError("El juego no está en el estado START_GAME")
        
        self.__game_state = Game_State.FINISH_GAME


############ SETTERS Y GETTERS ###############

    @property
    def _game_mode(self):
        return self.__game_mode

    @_game_mode.setter
    def _game_mode(self, mode: Game_Mode):
        spawn_bacterium = self.__board.get_position_spawn_bacterium()
        spawn_other = self.__board.get_position_spawn_other()
        if not (self.__game_state == Game_State.CONFIG_GAME and spawn_bacterium != None and spawn_other != None):
            raise ValueError("El juego no está en el estado CONFIG_GAME o no se configuró uno de los spawn")
        
        self.__game_mode = mode

    def start_game(self):
        if not (self.__game_state == Game_State.CONFIG_GAME and self.__game_mode != None):
            raise ValueError("El juego no está en el estado CONFIG_GAME o no se configuró el modo de juego")
        
        self.__game_state = Game_State.START_GAME

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

    @_frecuency_bacterium.setter
    def _frecuency_bacterium(self, new_frec):
        self.__frecuency_bacterium = new_frec

    @property
    def _frecuency_other(self):
        return self.__frecuency_other

    @_frecuency_other.setter
    def _frecuency_other(self, new_frec):
        self.__frecuency_other = new_frec

    @property
    def _cant_bacterium(self):
        return self.__cant_bacterium

    @_cant_bacterium.setter
    def _cant_bacterium(self, new_cant):
        self.__cant_bacterium = new_cant

    @property
    def _cant_other(self):
        return self.__cant_other

    @_cant_other.setter
    def _cant_other(self, new_cant):
        self.__cant_other = new_cant

    @property
    def _movements(self):
        return self.__movements

    def set_spawn_bacterium(self, position):
        if  self._game_state != Game_State.CONFIG_GAME:
            raise ValueError("El juego no está en el estado CONFIG_GAME")
        
        self.__board.set_position_spawn_bacterium(position)

    def set_spawn_other(self, position):
        if self._game_state != Game_State.CONFIG_GAME:
            raise ValueError("El juego no está en el estado CONFIG_GAME")

        self.__board.set_position_spawn_other(position)

    def count_in_adjacents(self, x, y, ente):
        vecinos = self._board.get_possible_moves(x,y)
        contador = 0

        for celda in vecinos:
            a = celda[0]
            b = celda[1]

            if ente == "b":
                contador += self._board.get_cell(a,b).cant_bacteria()
            if ente == "a":
                contador += self._board.get_cell(a,b)._antibiotics
            if ente == "v":
                contador += self._board.get_cell(a,b).cant_bacteriophages()

        return contador