from .Entity import Entity

class Bacteriophage(Entity):

    def __init__(self, levelInfection:int):
      self.__infection = levelInfection

    @property
    def infection(self):
      return self.__infection

    @infection.setter
    def infection(self, levelInfection):
      self.__infection = levelInfection

    #Suma
    def add_move(self):
        self.__infection -= 1

    #Eliminacion
    def __del__(self):
      del self

    def moment_death(self):
      if (self.__infection == 0):
        return True
      return False

    #Muerte del virus despues de un determinado tiempo
    def degradacion (self):
      if (self.moment_death()):
        del self


    def __str__(self):
      return 'v'

    def __str_aux__(self):
      return self.__str__()+self.infection.__str__()

    @staticmethod
    def from_string(cell_str):
      if cell_str != 'v':
        raise ValueError(f'Invalid Bacteriofago string: {cell_str}')
      return Bacteriophage(4)



