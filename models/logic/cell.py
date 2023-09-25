
class Cell:

	def __init__(self):
		self.__bacteria = []
		self.__antibiotics = 0
		self.__bacteriophages = []
		self.__spawn_bacterium = False
		self.__spawn_other = False

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

	@property
	def _bacteria(self):
		return self.__bacteria
	
	@_bacteria.setter
	def _bacteria(self, state, moves ):
		#crear bacteria del tipo correcto
		self.__bacteria.append()

	@_bacteria.setter
	def _bacteria(self, state ):
	#crear bacteria del tipo correcto
		self.__bacteria.append()

	def _cant_bacteria(self):
		return self.__bacteria.__len__()
	
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
	
