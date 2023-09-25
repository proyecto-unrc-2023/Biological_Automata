from models.logic.Bacterium import *
from models.logic.Antibiotic import *
from models.logic.Bacteriophage import *

class Cell:


	def __init__(self):
		self.__bacteria = []
		self.__antibiotics = 0
		self.__bacteriophages = []
		self.__spawn_bacterium = False
		self.__spawn_other = False

	def __str__(self):
			res = ' '
			for _ in range(0,self.__antibiotics):
				 
				res = self.__antibiotics.__str__()+ res

			for bac in self.__bacteria:
				res = bac.__str__() + res

			for vir in self.__bacteriophages:
			 	res = vir.__str__() + res
			
			return res
			
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
			elif (cell_str == Antibiotic().__str__()):
				return Antibiotic()
			else:
				raise ValueError(f'Invalid cell string: {cell_str}')
	

	def get_spawn_other(self):
		return self.__spawn_other

	def set_spawn_other(self):
		if self.is_empty():
			self.__spawn_other = True
		else:
			raise ValueError (f'celda ocupada')

	def get_spawn_bacterium(self):
		return self.__spawn_bacterium
		
	
	def set_spawn_bacterium(self):
		if self.is_empty():
			self.__spawn_bacterium = True
		else:
			raise ValueError(f'celda ocupada')

	#def __eq__(self, other):
	#	return isinstance(other, Cell)
	def __eq__(self, other):
		if self._antibiotics == other._antibiotics and self._bacteria.__eq__(other._bacteria) and self._bacteriophages.__eq__(other._bacteriophages) and self.__spawn_bacterium.__eq__(other.__spawn_bacterium) and self.__spawn_other.__eq__(other.__spawn_other):
			return True
		return False
	
	def is_empty(self):
		if self._antibiotics == 0 and self._cant_bacteria() == 0 and self._cant_bacteriophages() == 0 and not(self.__spawn_bacterium or self.__spawn_other):
			return True
		return False

	@property
	def _bacteria(self):
		return self.__bacteria
	
	@_bacteria.setter
	def _bacteria(self, bacteria:Bacterium):
		#crear bacteria del tipo correcto
		self.__bacteria.append(bacteria)

	#def set_bacterias(self, state:Type_Bacterium):
	#	self.bacterias.append([Bacterium(state)])
	
	def _cant_bacteria(self):
		return self.__bacteria.__len__()
	
	#def set_bacterias(self, bacter:Bacterium, moves:int):
	#	self.bacterias.append

	
	@property
	def _antibiotics(self):
		return self.__antibiotics

	@_antibiotics.setter
	def _antibiotics(self, cant:int):
		self.__antibiotics = cant
	
	@property
	def _bacteriophages(self):
		return self.__bacteriophages

	@_bacteriophages.setter
	def _bacteria(self, poder ):
		#crear bacteriografo  del tipo correcto
		self.__bacteriophages.append()

	
	def _cant_bacteriophages(self):
		return self.__bacteriophages.__len__()

	def is_empty(self):
		if self._antibiotics == 0 and self._cant_bacteria() == 0 and self._cant_bacteriophages() == 0 and not(self.__spawn_bacterium or self.__spawn_other):
			return True
		return False
			
	def __eq__(self, other):
		if self._antibiotics == other._antibiotics and self._bacteria.__eq__(other._bacteria) and self._bacteriophages.__eq__(other._bacteriophages) and self.__spawn_bacterium.__eq__(other.__spawn_bacterium) and self.__spawn_other.__eq__(other.__spawn_other):
			return True
		return False
	
