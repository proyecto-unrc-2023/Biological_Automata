from models.logic.cell import Cell
from models.logic.Bacteriophage import Bacteriophage
from models.logic.Bacterium import *


class CellBacteriophague(Cell):
  def __init__(self):
    self.__bacteriophages = []
    self.__cant_bacteriophague = 0

  def get_bacteriophagues(self):
    return self.__bacteriophages


  def set_bacteriophagues(self, array):
    self.__bacteriophages = array


  def get_cant_bacteriophague(self):
    return self.__cant_bacteriophague


  def set_cant_bacteriophague(self, value):
    self.__cant_bacteriophague = value


  def add_bacteriophague(self, entity: Bacteriophage):
    self.__bacteriophages.append(entity)
    self.__cant_bacteriophague += 1


  def burst_bacteriumInfected(self,x,y):
    bacteria_to_remove = []
    for bacterium in self.__bacteria:
      if isinstance(bacterium,BacteriumInfected) and bacterium.lithic_State():
        bacteria_to_remove.append(bacterium)
        for _ in range(4):
          bacteriophage = Bacteriophage(4)
          bacteriophage.set_pos(x,y)
          self.__bacteriophages.append(bacteriophage)

    for bacterium in bacteria_to_remove:
      self.__bacteria.remove(bacterium)

    self.set_cant_bacteriophague(len(self.__bacteriophages))
    self.set_cant_bacteria(len(self.__bacteria))


  def infection_to_bacteria(self,x,y):
    one_not_infected = False
    power = 0

    for bacteriophage in self.__bacteriophages:
      power += bacteriophage.infection

    power = min(power, 4)

    infected = []
    for bacterium in self.__bacteria:
      if not isinstance(bacterium, BacteriumInfected):
        bacterium = BacteriumInfected(power)
        bacterium.set_pos(x,y)
        infected.append(bacterium)
        one_not_infected = True
      else:
        bacterium.set_pos(x,y)
        infected.append(bacterium)

    if one_not_infected:
      self.__bacteriophages = []

    self.__bacteria = infected
    self.set_cant_bacteriophague(len(infected))
    self.__cant_bacteriophague = 0


  def death_bacteriophague(self):
    bacteriophage_to_remove = []

    for bacteriophage in self.__bacteriophages:
      if bacteriophage.moment_death():
        bacteriophage_to_remove.append(bacteriophage)

    for bacteriophage in bacteriophage_to_remove:
      self.__bacteriophages.remove(bacteriophage)
      self.__cant_bacteriophague -= 1



  def update_cell(self,x,y):
    #aplico regla de sobrepoblación
    if self.__cant_bacteria >= 4:
      self.overpopulation(x,y)

		#si existen bacteriofagos y bacterias en la misma celda, aplico las reglas de cruzamiento
    if self.__cant_bacteriophague > 0 and self.__cant_bacteria > 0:
      self.infection_to_bacteria(x,y)

		#actualizo por la reproduccion de bacterias
    self.update_for_reproduction(x,y)

		#actualizo por bacteriofagos que se quedaron sin movimientos
    self.death_bacteriophague()

		#actualizo por la explosion de bacteriofagos
    self.burst_bacteriumInfected(x,y)



  def is_empty(self):
    return self.__cant_bacteriophague == 0 and super().is_empty()


  def __str__(self):
    if self.is_empty():
      return ' '
    res = ''
    cant =  self.__cant_bacteriophague
    if cant != 0:
      res = res + cant.__str__() + 'v'
    return super().__str__() + res

