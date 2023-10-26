from models.logic.cell import Cell
from models.logic.Antibiotic import Antibiotic
from models.logic.Bacterium import *


class CellAntibiotic(Cell):
  def __init__(self):
    super().__init__()
    self.__antibiotics = []
    self.__cant_antibiotic = 0


  def get_antibiotics(self):
    return self.__antibiotics


  def set_antibiotics(self, array):
    self.__antibiotics = array


  def get_cant_antibiotic(self):
    return self.__cant_antibiotic


  def set_cant_antibiotic(self, value):
    self.__cant_antibiotic = value


  def add_antibiotic(self, entity: Antibiotic):
    self.__antibiotics.append(entity)
    self.__cant_antibiotic += 1


  def low_dose(self,x,y):
		# total_antibiotics = self._antibiotics
    new_bacteria = []
    for bacterium in self.get_bacteria():
      if isinstance(bacterium, BacteriumStrong):
	    #ver si los movimientos se acumulan
        bact_weak = BacteriumWeak(0)
        bact_weak.set_pos(x,y)
        new_bacteria.append(bact_weak)

    self.set_bacteria(new_bacteria)
    self.set_cant_bacteria(len(new_bacteria))
    self.__antibiotics = []
    self.set_cant_antibiotic(0)


  def high_dose(self):
    #esa celda se queda sin bacterias y sin antibioticos
    self.set_bacteria([])
    self.set_cant_bacteria(0)
    self.__antibiotics.clear()
    self.set_cant_antibiotic(0)


  def update_for_recovery(self,x,y):
    bacteria_to_add = []
    bacteria_to_remove = []
    for bacterium in self.get_bacteria():

      if bacterium.isRecoverable():
        recovered = bacterium.recover()
        recovered.set_pos(x,y)

        bacteria_to_add.append(recovered)
        bacteria_to_remove.append(bacterium)


    for bacterium in bacteria_to_add:
      self.get_bacteria().append(bacterium)
    for bacterium in bacteria_to_remove:
      self.get_bacteria().remove(bacterium)

    self.set_cant_bacteria(len(self.get_bacteria()))


  def update_cell(self,x,y):
		#aplico regla de sobrepoblación
    if self.get_cant_bacteria() >= 4:
      self.overpopulation(x,y)

		#si existen bacterias y antibioticos en la misma celda, aplico las reglas de cruzamiento
    if self.get_cant_antibiotic() > 0 and self.get_cant_bacteria() > 0:
      if self.get_cant_antibiotic() > self.get_cant_bacteria():
        self.high_dose()
      else:
        self.low_dose(x,y)

		#actualizo por la reproduccion de bacterias
    self.update_for_reproduction(x,y)

		#actualizo por la recuperación de bacterias
    self.update_for_recovery(x,y)

  def is_empty(self):
    return self.__cant_antibiotic == 0 and super().is_empty()


  def __str__(self):
    res = ''
    cant = self.__cant_antibiotic
    if cant != 0:
      res = res + cant.__str__() + 'a'
    return super().__str__() + res




  ##falta eq
