from models.logic.board import Board
from models.logic.Bacterium import *
from models.logic.Antibiotic import Antibiotic
from models.logic.Bacteriophage import Bacteriophage
from models.logic.Game_State import Game_State
from models.logic.Game_Mode import Game_Mode
class GameController:

    def __init__(self):
        self.__game_state = Game_State.NOT_STARTED
        self.__game_mode = None
        self.__board = Board(15, 20, 4)  # por defecto
        self.__cant_bacterium = 10             
        self.__cant_other = 20
        self.__frecuency_bacterium = 2
        self.__frecuency_other = 2
        self.__movements = 0
        #atributos correspondientes a la configuracion avanzada
        self.__moves_for_reproduction = 20
        self.__moves_for_recovery = 6
        self.__power_antibiotic = 3
        self.__moves_for_explotion = 4
        self.__cant_bacteriophages_after_explotion = 4
        self.__initial_power_infection = 4
        self.__mutation_probability = 0.1
        self.__cant_overpopulation = 4    


    def config(self, cant_bact, frec_bact, cant_other, frec_other, mode: Game_Mode):
        if self._game_state != Game_State.NOT_STARTED:
            raise ValueError("El juego no está en el estado START_GAME")

        if not isinstance(mode, Game_Mode):
            raise ValueError("El modo de juego cargado no es válido!")
        
        if cant_bact < 0 or cant_other < 0:
            raise ValueError(
                "La cantidad de los entes no pueden ser negativas!")

        if frec_bact <= 0 or frec_other <= 0:
            raise ValueError(
                "Los valores de las frecuencias deben ser positivos!")

        self._game_state = Game_State.CONFIG_GAME
        self._game_mode = mode
        self.__board.create_board()
        self._frecuency_bacterium = frec_bact
        self._frecuency_other = frec_other
        self._cant_bacterium = cant_bact
        self._cant_other = cant_other

    def set_spawn_bacterium(self, position):
        if self._game_state != Game_State.CONFIG_GAME:
            raise ValueError("El juego no está en el estado CONFIG_GAME")

        self.__board.set_position_spawn_bacterium(position)

    def set_spawn_other(self, position):
        if self._game_state != Game_State.CONFIG_GAME:
            raise ValueError("El juego no está en el estado CONFIG_GAME")

        self.__board.set_position_spawn_other(position)

    def advanced_config(self, moves_for_reproduction, moves_for_recovery, 
            power_antibiotic, moves_for_explotion, cant_bacteriophages_after_explotion, 
            initial_power_infection, mutation_probablity, cant_overpopulation):
        
        if self.__game_state != Game_State.CONFIG_GAME:
            raise ValueError("El juego no está en el estado CONFIG_GAME")

        self.set_moves_for_reproduction(moves_for_reproduction)
        self.set_moves_for_recovery(moves_for_recovery)
        self.set_power_antibiotic(power_antibiotic)
        self.set_moves_for_explotion(moves_for_explotion)
        self.set_cant_bacteriophages_after_explotion(cant_bacteriophages_after_explotion)
        self.set_initial_power_infection(initial_power_infection)
        self.set_mutation_probability(mutation_probablity)
        self.set_cant_overpopulation(cant_overpopulation)
        self._board.set_cant_overpopulation(self.__cant_overpopulation)

    @property
    def _game_mode(self):
        return self.__game_mode

    @_game_mode.setter
    def _game_mode(self, mode: Game_Mode):
        if self.__game_state != Game_State.CONFIG_GAME:
            raise ValueError(
                "El juego no está en el estado CONFIG_GAME")
        
        self.__game_mode = mode
        self._board.set_gameMode(mode)
        
    def start_game(self):
        if self.__game_state != Game_State.CONFIG_GAME:
            raise ValueError("El juego no está en el estado CONFIG_GAME")

        if self.__board.get_position_spawn_bacterium == None:
            raise ValueError("El spawn de bacterias no está seteado")
        
        if self.__board.get_position_spawn_other == None:
            raise ValueError("El spawn de otro no está seteado")
        
        self.__game_state = Game_State.START_GAME

    def generate_bacterium(self):
        if self._game_state != Game_State.START_GAME:
            raise ValueError("El juego no está en el estado START_GAME")

        spawn = self.__board.get_position_spawn_bacterium()
        if spawn is not None:
            move = self._board.get_random_move(spawn[0], spawn[1])
            bacterium = BacteriumNormal(0, *self.parameters_for_creation())
            if move is not None:
                self._board.add_bacterium(move[0], move[1], bacterium)
                self._cant_bacterium -= 1

    def parameters_for_creation(self):
                return [
                self.__moves_for_reproduction, 
                self.__moves_for_recovery, 
                self.__moves_for_explotion, 
                self.__cant_bacteriophages_after_explotion,
                self.__initial_power_infection, 
                self.__mutation_probability
            ]

    def generate_other(self):
        if self._game_state != Game_State.START_GAME:
            raise ValueError("El juego no está en el estado START_GAME")

        spawn = self.__board.get_position_spawn_other()
        if spawn is not None:
            move = self.__board.get_random_move(spawn[0], spawn[1])
            if move is not None:
                if self.__game_mode == Game_Mode.ANTIBIOTIC:
                    entity = Antibiotic(self.__power_antibiotic)
                    self._board.add_antibiotic(move[0], move[1], entity)
                    self._cant_other -= 1
                else:
                    entity = Bacteriophage(self.__initial_power_infection)
                    self._board.add_bacteriophage(move[0], move[1], entity)
                    self._cant_other -= 1

    def generate_entities(self):
        if self._game_state != Game_State.START_GAME:
            raise ValueError("El juego no está en el estado START_GAME")

        if (self._cant_bacterium > 0 and self._movements % self._frecuency_bacterium == 0):
            self.generate_bacterium()

        if (self._game_mode == Game_Mode.ANTIBIOTIC and 
            self._cant_other > 0 and self._movements % self._frecuency_other == 0):

            self.generate_other()

        if (self._game_mode == Game_Mode.BACTERIOPHAGE and 
            self._cant_other > 0 and self._movements % self._frecuency_other == 0):

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

        self.__game_state = Game_State.NOT_STARTED

        self.__game_state = Game_State.NOT_STARTED
        self.__game_mode = None
        self.__board = Board(15, 20, 4)


    #ALGUNOS SETTERS Y GETTERS
    @property
    def _game_state(self):
        return self.__game_state

    @_game_state.setter
    def _game_state(self, mode: Game_State):
        self.__game_state = mode

    @property
    def spawn_bacterium(self):
        return self.__board.get_position_spawn_bacterium()

    @property
    def spawn_other(self):
        return self.__board.get_position_spawn_other()

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

    def set_moves_for_reproduction(self, moves_for_reproduction):
        if moves_for_reproduction < 0:
            raise ValueError("La cantidad de movimientos para reproducirse no puede ser negativa!")
        
        self.__moves_for_reproduction = moves_for_reproduction

    def set_moves_for_recovery(self, moves_for_recovery):
        if moves_for_recovery < 0:
            raise ValueError("La cantidad de movimientos para recuperarse no puede ser negativa!")
        
        self.__moves_for_recovery = moves_for_recovery

    def set_power_antibiotic(self, power_antibiotic):
        if power_antibiotic <= 0:
            raise ValueError("El poder de los antibioticos debe ser positivo!")
        
        self.__power_antibiotic = power_antibiotic
        
    def set_moves_for_explotion(self, moves_for_explotion):
        if moves_for_explotion < 0:
            raise ValueError("La cantidad de movimientos para explotar no puede ser negativa!")
        
        self.__moves_for_explotion = moves_for_explotion

    def set_cant_bacteriophages_after_explotion(self, cant_bacteriophages_after_explotion):
        if cant_bacteriophages_after_explotion <= 0:
            raise ValueError("La cantidad de bacteriófagos después de la explosión debe ser positva!")
        
        self.__cant_bacteriophages_after_explotion = cant_bacteriophages_after_explotion

    def set_initial_power_infection(self, initial_power_infection):
        if initial_power_infection <= 0:
            raise ValueError("El poder inicial de infección debe ser positivo!")
        
        self.__initial_power_infection = initial_power_infection
    
    def set_mutation_probability(self, mutation_probability):
        if mutation_probability < 0 or mutation_probability > 1:
            raise ValueError("La probabilidad de mutación debe estar entre 0 y 1!")
        
        self.__mutation_probability = mutation_probability
        
    def set_cant_overpopulation(self, cant_overpopulation):
        if cant_overpopulation < 1:
            raise ValueError("La cantidad para sobrepoblación debe ser mayor a 1!")
        
        self.__cant_overpopulation = cant_overpopulation


    # METODOS PARA IMPLEMENTAR STEPS DE BEHAVE

    def get_rows(self):
        return self._board._rows
    
    def get_columns(self):
        return self._board._columns
        
    def add_bacterium(self, x, y, moves, type):
        if type == "normal":
            self._board.add_bacterium(x, y, BacteriumNormal(moves, *self.parameters_for_creation()))
        if type == "debil":
            self._board.add_bacterium(x, y, BacteriumWeak(moves, *self.parameters_for_creation()))
        if type == "fuerte":
            self._board.add_bacterium(x, y, BacteriumStrong(moves, *self.parameters_for_creation()))
    
    def add_antibiotic(self,x,y,power):
        self._board.add_antibiotic(x,y,Antibiotic(power))

    def add_bacteriophage(self, x, y, power):
        self._board.add_bacteriophage(x, y, Bacteriophage(power))

    def add_infected(self, x, y, grade):
        self._board.add_bacterium(x, y, BacteriumInfected(grade, *self.parameters_for_creation()))

    def add_entities(self, x, y, n, ente):
        if ente == "antibiotico":
            for _ in range(0, n):
                self._board.add_antibiotic(x, y, Antibiotic(self.__power_antibiotic))
        if ente == "bacteriofago":
            for _ in range(0, n):
                self._board.add_bacteriophage(x, y, Bacteriophage(self.__initial_power_infection))
        if ente == "bacteria normal":
            for _ in range(0, n):
                self._board.add_bacterium(x, y, BacteriumNormal(0, *self.parameters_for_creation()))
        if ente == "bacteria debil":
            for _ in range(0, n):
                self._board.add_bacterium(x, y, BacteriumWeak(0, *self.parameters_for_creation()))
        if ente == "bacteria fuerte":
            for _ in range(0, n):
                self._board.add_bacterium(x, y, BacteriumStrong(0, *self.parameters_for_creation()))
        if ente == "bacteria infectada":
            for _ in range(0, n):
                self._board.add_bacterium(x, y, BacteriumInfected(0, *self.parameters_for_creation()))

    def move_entity(self, x1, y1, x2, y2, ente):
        entity_to_move = None

        if ente == "bacteria normal":
            entity_to_move = self._board.get_cell(x1,y1).get_bacterium('b')
        if ente == "bacteria fuerte":
            entity_to_move = self._board.get_cell(x1,y1).get_bacterium('f')
        if ente == "bacteria debil":
            entity_to_move = self._board.get_cell(x1,y1).get_bacterium('d')
        if ente == "bacteria infectada":
            entity_to_move = self._board.get_cell(x1,y1).get_bacterium('i')
        if ente == "bacteriofago":
            entity_to_move = self._board.get_cell(x1, y1).get_bacteriophage()

        self._board.move_entity(x2, y2, x1, y1, self._board, entity_to_move)

    def count_bacteria_with_moves(self, x, y, type, moves):
        return self._board.get_cell(x, y).count_bacteria_with_moves(type, moves)
            
    def count_antibiotics(self,x,y,power):
        return self._board.get_cell(x,y).count_antibiotic(power)
        
    def count_total_antibiotics(self, power):
        return self._board.count_total_antibiotics(power)
    
    def count_bacteriophages(self, x, y, power):
        return self._board.get_cell(x, y).count_bacteriophages(power)
    
    def count_infected(self, x, y, grade):
        return self._board.get_cell(x, y).count_infected(grade)
    
    def count_in_adjacents(self, x, y, ente):
        vecinos = self._board.get_possible_moves(x, y)
        contador = 0

        for celda in vecinos:
            a = celda[0]
            b = celda[1]

            if ente in ("bacteria", "bacterias"):
                contador += self._board.get_cell(a, b).get_cant_bacteria()
            if ente in ("antibiotico", "antibioticos"):
                contador += self._board.get_cell(a, b).get_cant_antibiotic()
            if ente in ("bacteriofago", "bacteriofagos"):
                contador += self._board.get_cell(a, b).get_cant_bacteriophage()

        return contador
    
    def count_entities(self, x, y, ente):
        if ente == "antibioticos":
            return self._board.get_cell(x,y).get_cant_antibiotic()
        if ente in  ("bacteria","bacterias"):
            return self._board.get_cell(x,y).get_cant_bacteria()
        if ente == "bacteria normal":
            return self._board.get_cell(x,y).cant_ente('b')
        if ente == "bacteria fuerte":
            return self._board.get_cell(x,y).cant_ente('f')
        if ente == "bacteria debil":
            return self._board.get_cell(x,y).cant_ente('d')
        if ente == "bacteria infectada":
            return self._board.get_cell(x,y).cant_ente('i')
        if ente in ("bacteriofago","bacteriofagos"):
            return self._board.get_cell(x,y).get_cant_bacteriophage()

    def count_total(self, ente):
        if ente == "bacterias":
            return self._board.how_many_entities('bacterias')
        if ente == "antibioticos":
            return self._board.how_many_entities('a')
        if ente == "bacteriofagos":
            return self._board.how_many_entities('v')