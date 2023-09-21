class Bacteriophage:

    def __init__(self, levelInfection:int):
      self.__infection = levelInfection

    @property
    def get_infection(self):
      return self.__infection

    @get_infection.setter
    def set_infection(self, levelInfection):
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

    @staticmethod
    def from_string(cell_str):
      if cell_str == 'v':
          return Bacteriophage(4)
      else:
        raise ValueError(f'Invalid Bacteriofago string: {cell_str}')
