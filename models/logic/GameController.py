from enum import Enum
from models.logic.board import Board
from models.logic.cell import Cell
from models.logic.Bacterium import *
from models.logic.Antibiotic import Antibiotic
from models.logic.Bacteriophage import Bacteriophage

class Game_Mode(Enum):
    ANTIBIOTIC = 1      #Modo de juego
    BACTERIOPHAGE = 2   #Modo de juego
    #Modo de juego BACTERIUM (Si no setea spawn de "other")

class Game_State(Enum):
    NOT_STARTER = 1     #Todavia no empezo el juego
    CONFIG_GAME = 2     #CONFIGURA LOS PARAMETROS
    START_GAME = 3      #Inicio de juego

class GameController:

    def __init__(self):
        #al iniciar se dejan valores por defecto que el usuario puede modificar si quiere
        self.__game_state = Game_State.NOT_STARTER
        self.__game_mode = None
        self.__board = Board(15,20)             # por defecto
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

        if cant_bact < 0 or cant_other < 0:
            raise ValueError("La cantidad de los entes no pueden ser negativas!")

        if frec_bact <= 0 or frec_other <= 0:
            raise ValueError("Los valores de las frecuencias deben ser positivos!")

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
        # print('m------  \n',actualizado.__str__())
        self.__board = actualizado
        self.generate_entities()
        # print('a------  \n',actualizado.__str__())
        actualizado.crossing_board()
        # print('b------  \n',actualizado.__str__())
        self.__movements += 1


    def stop(self):
        if self.__game_state != Game_State.START_GAME:
            raise ValueError("El juego no está en el estado START_GAME")

        self.__game_state = Game_State.NOT_STARTER
        self.__game_mode = None
        self.__board = Board(15,20)

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

    @property
    def spawn_bacterium(self):
        return self.__board.get_position_spawn_bacterium()

    @property
    def spawn_other(self):
        return self.__board.get_position_spawn_other()

    def count_in_adjacents(self, x, y, ente):
        vecinos = self._board.get_possible_moves(x,y)
        contador = 0

        for celda in vecinos:
            a = celda[0]
            b = celda[1]

            if ente == "bacteria" or ente == "bacterias":
                contador += self._board.get_cell(a,b).cant_bacteria()
            if ente == "antibiotico" or ente == "antibioticos":
                contador += self._board.get_cell(a,b)._antibiotics
            if ente == "bacteriofago" or ente == "bacteriofagos":
                contador += self._board.get_cell(a,b).cant_bacteriophages()

        return contador
    
    def add_entities(self, x, y, n, ente):
        if ente == "antibiotico":
            for _ in range(0,n):
                self._board.add_antibiotic(x,y,Antibiotic())
        if ente == "bacteriofago":
            for _ in range(0,n):
                self._board.set_bacteriophage(x,y, Bacteriophage(2))
        if ente == "bacteria normal":
            for _ in range(0,n):
                self._board.set_bacterium(x,y, BacteriumNormal(1))
        if ente == "bacteria debil":
            for _ in range(0,n):
                self._board.set_bacterium(x,y, BacteriumWeak(1))
        if ente == "bacteria fuerte":
            for _ in range(0,n):
                self._board.set_bacterium(x,y, BacteriumStrong(1))
        if ente == "bacteria infectada":
            for _ in range(0,n):
                self._board.set_bacterium(x,y, BacteriumInfected(1))

    def count_entities(self, x, y, ente):
        if ente == "antibioticos":
            return self._board.get_cell(x,y)._antibiotics
        if ente == "bacterias":
            return self._board.get_cell(x,y).cant_bacteria()
        if ente == "bacteria normal" or ente =="bacteria debil" or ente == "bacteria fuerte":
            return self._board.get_cell(x,y).cant_type_bacterium(ente)
        if ente == "bacteriofago" or ente == "bacteriofagos":
            return self._board.get_cell(x,y).cant_bacteriophages()

    def add_bacteriophage(self, x, y, power):
        self._board.set_bacteriophage(x,y, Bacteriophage(power))

    def count_infected(self, x, y, grade):
        return self._board.get_cell(x,y).count_infected(grade)

    def add_infected(self, x, y, grade):
        self._board.set_bacterium(x,y, BacteriumInfected(grade))

    def count_bacteriophages(self, x, y, power):
        return self._board.get_cell(x,y).count_bacteriophages(power)

    def count_bacteria_with_moves(self, x, y, type, moves):
        return self._board.get_cell(x,y).count_bacteria_with_moves(type,moves)

    def add_bacterium(self, x, y, moves, type):
        if type == "normal":
            self._board.add_bacterium_moves(x,y,BacteriumNormal(moves))
        if type == "debil":
            self._board.add_bacterium_moves(x,y,BacteriumWeak(moves))
        if type == "fuerte":
            self._board.add_bacterium_moves(x,y,BacteriumStrong(moves))

    def move_entity(self, x1, y1, x2, y2, ente):
        #asignacion para que no chille python, pero no hace nada en realidad
        entity_to_move = ente

        if ente == "bacteria normal":
            entity_to_move = self._board.get_cell(x1,y1).get_normal()
        if ente == "bacteria fuerte":
            entity_to_move = self._board.get_cell(x1,y1).get_strong()
        if ente == "bacteria debil":
            entity_to_move = self._board.get_cell(x1,y1).get_weak()
        if ente == "bacteria infectada":
            entity_to_move = self._board.get_cell(x1,y1).get_infected()
        if ente == "bacteriofago":
            entity_to_move = self._board.get_cell(x1,y1).get_bacteriophage()

        self._board.move_entity(x2, y2, x1, y1, self._board, entity_to_move)

    def count_total(self, ente):
        if ente == "bacterias":
            return self._board.how_many_entities('bacterias')
        if ente == "antibioticos":
            return self._board.how_many_entities('a')
        if ente == "bacteriofagos":
            return self._board.how_many_entities('v')
