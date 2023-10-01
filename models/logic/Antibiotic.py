from .Entity import Entity
class Antibiotic(Entity):

    def __init__(self):
      pass

    #Eliminacion
    def __del__(self):
      del self

    @staticmethod
    def from_string(cell_str):
      if (cell_str == 'a'):
        return Antibiotic()
      raise ValueError("Invalid input: 'cell_str' must be 'a'")


    def __str__(self):
      return 'a'
