class Antibiotic:

    def __init__(self):
      pass

    #Eliminacion
    def __del__(self):
      del self

    @staticmethod
    def from_string(cell_str):
      if (cell_str == 'a'):
        return Antibiotic
      return TypeError #ver que error ponerle


    def __str__(self):
      return 'a'
