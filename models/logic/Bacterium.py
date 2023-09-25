from .Ente import Ente

class Bacterium(Ente):

    #Constructor
    def __init__(self, moves:int):
      self.moves = max(0, moves)

    #Suma de movimiento de bacteria
    def add_move(self):
        self.moves = self.moves + 1

    @property
    def moves(self):
      return self.__moves

    #Setter moves
    @moves.setter
    def moves(self, value:int):
      self.__moves = value

    def isReproducible(self):
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


class BacteriumNormal(Bacterium):

    def reproducir(self):
      if (self.isReproducible()):
        self.moves = 0
        return BacteriumNormal(0)
      raise ValueError("El número de movimientos no es 3") #ver que error tirar

    def isReproducible(self):
      if (self.moves == 3):
        return True
      return False


    def __str__(self):
      return 'b'

    @staticmethod
    def from_string():
      pass



class BacteriumStrong(Bacterium):

    def reproducir(self):
      if (self.isReproducible()):
        self.moves = 0
        return BacteriumStrong(0)
      return ValueError #ver que error tira

    def isReproducible(self):
      if (self.moves == 3):
        return True
      return False

    def __str__(self):
      return 'f'


class BacteriumInfected(Bacterium):

    #Esta en condiciones de explotar?
    def lithic_State(self):
      if (self.moves == 4):
          return True
      return False


    ##NOSE SI ESTO ESTA BIEN
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

    def returnState(self):
      if (self.moves == 6):
        return True
      return False

    def __str__(self):
      return 'd'
