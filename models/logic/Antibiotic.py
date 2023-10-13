from .Entity import Entity

class Antibiotic(Entity):

    def __init__(self):
      pass

    def add_move(self):
      pass
    
    @staticmethod
    def from_string(cell_str):
      if (cell_str == 'a'):
        return Antibiotic()
      raise ValueError("Invalid input: 'cell_str' must be 'a'")

    def __str__(self):
      return 'a'