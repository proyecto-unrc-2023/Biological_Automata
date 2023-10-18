import random

from .Entity import Entity

class Bacterium(Entity):

    #Constructor
    def __init__(self, moves:int):
      self.__moves = max(0, moves)

    #Suma de movimiento de bacteria
    def add_move(self):
        self.__moves = self.__moves + 1

    @property
    def moves(self):
      return self.__moves

    #Setter moves
    @moves.setter
    def moves(self, value:int):
      self.__moves = value

    def isReproducible(self):
      pass

    def isRecoverable(self):
      pass

    def __str__(self):
      pass

    @staticmethod
    def from_string(cell_str):
      if cell_str == BacteriumNormal(0).__str__():
        return BacteriumNormal(0)
      elif cell_str == BacteriumStrong(0).__str__():
        return BacteriumStrong(0)
      elif cell_str == BacteriumInfected(0).__str__():
        return BacteriumInfected(0)
      elif cell_str == BacteriumWeak(0).__str__():
        return BacteriumWeak(0)
      else:
        raise ValueError(f'Invalid Bacterium string: {cell_str}')

    @property
    def type(self):
      return self.__str__()

class BacteriumNormal(Bacterium):

    def reproducir(self):
      if (not self.isReproducible()):
        raise ValueError("El número de movimientos no es 3")

      mutation_probability = 0.01

      #genero un numero aleatorio entre 0 y 1
      random_number = random.random()
      self.moves = 0
      if random_number > mutation_probability:
        return BacteriumNormal(0)
      else:
        return BacteriumStrong(0)

    def isReproducible(self):
      if (self.moves == 3):
        return True
      return False

    def isRecoverable(self):
       return False

    def __str__(self):
      return 'b'

class BacteriumStrong(Bacterium):

    def reproducir(self):
      if (not self.isReproducible()):
        raise ValueError("El numero de movimientos es inferior a 3")
      return BacteriumStrong(0)

    def isReproducible(self):
      if (self.moves == 3):
        return True
      return False

    def isRecoverable(self):
       return False

    def __str__(self):
      return 'f'

    
class BacteriumInfected(Bacterium):

    def lithic_State(self):
      if (self.moves >= 4):
          return True
      return False

    def exploid (self):
      if (self.lithic_State()):
        del self

    #Las bacterias infectadas no se pueden reproducir
    def isReproducible(self):
      return False

    def __str__(self):
      return 'i'



class BacteriumWeak(Bacterium):

    def isReproducible(self):
      return False

    def isRecoverable(self):
      if (self.moves == 6):
        return True
      return False

    def recover(self):
       return BacteriumStrong(0)

    def __str__(self):
      return 'd'
