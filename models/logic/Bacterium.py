import random
from .Entity import Entity
from .Bacteriophage import Bacteriophage
class Bacterium(Entity):
    
    # Constructor
    def __init__(self, moves, a = 20, b = 6, c = 4, d = 4, e = 4, f = 0.1):
        self.__pos = (None, None)
        self.__moves = max(0, moves)
        self.__moves_for_reproduction = a 
        self.__moves_for_recovery = b
        self.__moves_for_explotion = c
        self.__cant_bacteriophages_after_explotion = d
        self.__power_infection_after_explotion = e
        self.__mutation_probability = f

    def get_pos(self):
        return self.__pos

    def set_pos(self, row, colum):
        self.__pos = (row, colum)

    # Suma de movimiento de bacteria
    def add_move(self):
        self.__moves += 1

    @property
    def moves(self):
        return self.__moves
    
    @property
    def moves_for_reproduction(self):
        return self.__moves_for_reproduction

    @property
    def moves_for_recovery(self):
        return self.__moves_for_recovery
    
    @property
    def moves_for_explotion(self):
        return self.__moves_for_explotion
        
    @property
    def mutation_probability(self):
        return self.__mutation_probability

    @property
    def power_infection_after_explotion(self):
        return self.__power_infection_after_explotion
    
    @property
    def cant_bacteriophages_after_explotion(self):
        return self.__cant_bacteriophages_after_explotion
    
    def get_attributes_list(self):
        return [
                self.moves_for_reproduction, 
                self.moves_for_recovery, 
                self.moves_for_explotion, 
                self.cant_bacteriophages_after_explotion,
                self.power_infection_after_explotion, 
                self.__mutation_probability
            ]
    
    # Setter moves
    @moves.setter
    def moves(self, value: int):
        self.__moves = value

    def isReproducible(self):
        pass

    def isRecoverable(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def from_string(cell_str):
        if cell_str == str(BacteriumNormal(0)):
            return BacteriumNormal(0)
        elif cell_str == str(BacteriumStrong(0)):
            return BacteriumStrong(0)
        elif cell_str == str(BacteriumInfected(0)):
            return BacteriumInfected(0)
        elif cell_str == str(BacteriumWeak(0)):
            return BacteriumWeak(0)
        else:
            raise ValueError(f'Invalid Bacterium string: {cell_str}')

    @property
    def type(self):
        return str(self)



class BacteriumNormal(Bacterium):

    def __init__(self, moves, a = 20, b = 6, c = 4, d = 4, e = 4, f = 0.1, random_gen=random.random):
        super().__init__(moves, a, b, c, d, e, f)
        self.random_generator = random_gen


    def reproduce(self):
        if not self.isReproducible():
            raise ValueError(
                "La bacteria no está en condiciones de reproducirse!")

        self.moves = 0
        if self.random_generator() > self.mutation_probability:
            return BacteriumNormal(0, *self.get_attributes_list())
        else:
            return BacteriumStrong(0, *self.get_attributes_list())

    def isReproducible(self):
        return self.moves >= self.moves_for_reproduction
    
    def infect(self, power):
        infection = min(power, self.moves_for_explotion)
        return BacteriumInfected(infection, *self.get_attributes_list())

    def isRecoverable(self):
        return False

    def __str__(self):
        return 'b'


class BacteriumStrong(Bacterium):

    def __init__(self, moves, a = 20, b = 6, c = 4, d = 4, e = 4, f = 0.1, random_gen=random.random):
        super().__init__(moves, a, b, c, d, e, f)
        self.random_generator = random_gen


    def reproduce(self):
        if not self.isReproducible():
            raise ValueError(
                "La bacteria no está en condiciones de reproducirse!")

        self.moves = 0
        if self.random_generator() > self.mutation_probability:
            return BacteriumStrong(0, *self.get_attributes_list())
        else:
            return BacteriumNormal(0, *self.get_attributes_list())

    def isReproducible(self):
        return self.moves >= self.moves_for_reproduction
    
    def infect(self, power):
        infection = min(power, self.moves_for_explotion)

        return BacteriumInfected(infection, *self.get_attributes_list())

    def isRecoverable(self):
        return False

    def __str__(self):
        return 'f'


class BacteriumInfected(Bacterium):

    def lithic_State(self):
        return self.moves >= self.moves_for_explotion

    def exploit(self):
        if not self.lithic_State():
            raise ValueError(
                "La bacteria no está en condiciones de explotar!")
        
        bacteriophages = []
        for _ in range (self.cant_bacteriophages_after_explotion):
            bacteriophages.append(Bacteriophage(self.power_infection_after_explotion))

        return bacteriophages
    
    # Las bacterias infectadas no se pueden reproducir
    def isReproducible(self):
        return False

    def __str__(self):
        return 'i'


class BacteriumWeak(Bacterium):

    def isReproducible(self):
        return False

    def isRecoverable(self):
        return self.moves >= self.moves_for_recovery

    def recover(self):
        if not self.isRecoverable():
            raise ValueError(
                "La bacteria no está en condiciones de recuperarse!")

        return BacteriumStrong(0, *self.get_attributes_list())

    def __str__(self):
        return 'd'
