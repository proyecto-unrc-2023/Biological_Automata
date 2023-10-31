import random

from .Entity import Entity


class Bacterium(Entity):

    # Constructor
    def __init__(self, moves: int):
        self.__pos = (None, None)
        self.__moves = max(0, moves)

    def get_pos(self):
        return self.__pos

    def set_pos(self, row, colum):
        self.__pos = (row, colum)

    # Suma de movimiento de bacteria
    def add_move(self):
        self.__moves = self.__moves + 1

    @property
    def moves(self):
        return self.__moves

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

    def reproducir(self):
        # #genero un numero aleatorio entre 0 y 1
        random_number = random.random()
        return self.replicate_with_parameter(random_number)

    def replicate_with_parameter(self, random_number):
        if not self.isReproducible():
            raise ValueError(
                "La bacteria no está en condiciones de reproducirse!")
        mutation_probability = 0.01
        self.moves = 0
        if random_number > mutation_probability:
            return BacteriumNormal(0)
        else:
            return BacteriumStrong(0)

    def isReproducible(self):
        return self.moves >= 3

    def isRecoverable(self):
        return False

    def __str__(self):
        return 'b'


class BacteriumStrong(Bacterium):

    def reproducir(self):
        if not self.isReproducible():
            raise ValueError(
                "La bacteria no está en condiciones de reproducirse!")

        self.moves = 0
        return BacteriumStrong(0)

    def isReproducible(self):
        return self.moves >= 3

    def isRecoverable(self):
        return False

    def __str__(self):
        return 'f'


class BacteriumInfected(Bacterium):

    def lithic_State(self):
        return self.moves >= 4

    def exploid(self):
        if self.lithic_State():
            del self

    # Las bacterias infectadas no se pueden reproducir
    def isReproducible(self):
        return False

    def __str__(self):
        return 'i'


class BacteriumWeak(Bacterium):

    def isReproducible(self):
        return False

    def isRecoverable(self):
        return self.moves >= 6

    def recover(self):
        if not self.isRecoverable():
            raise ValueError(
                "La bacteria no está en condiciones de recuperarse!")

        return BacteriumStrong(0)

    def __str__(self):
        return 'd'
