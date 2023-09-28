from models.logic.Bacterium import *
from models.logic.Antibiotic import Antibiotic
from models.logic.Bacteriophage import Bacteriophage

class Cell:

	def __init__(self):
		self.__bacteria = []
		self.__antibiotics = 0
		self.__bacteriophages = []
		self.__spawn_bacterium = False
		self.__spawn_other = False

	def __str__(self):
		if self.is_empty():
			return ' '
		res = ''
		cant =self.cant_ente('a')
		if cant != 0:
			res = res + cant.__str__() + 'a'
		cant =self.cant_ente('b')
		if cant != 0:
			res = res + cant.__str__() + 'b'
		cant =self.cant_ente('f')
		if cant != 0:
			res = res + cant.__str__() + 'f'
		cant =self.cant_ente('d')
		if cant != 0:
			res = res + cant.__str__() + 'd'
		cant =self.cant_ente('i')
		if cant != 0:
			res = res + cant.__str__() + 'i'
		cant =  self.cant_bacteriophages()
		if cant != 0:
			res = res + cant.__str__() + 'v'
		return res
			
	@staticmethod
	def from_string(cell_str):
		cell = Cell()
		for i in range (cell_str.__len__()-1):
			num = cell_str[i]
			if cell_str[i+1] == 'b':
				for _ in  range(int(num)):
					cell._bacterium = BacteriumNormal(0)
				i += 1
				continue
			if cell_str[i+1] == 'f':
				for _ in  range(int(num)):
					cell._bacterium = BacteriumStrong(0)
				i += 1
				continue
			elif cell_str[i+1] == 'i':
				for _ in range(num):
					cell._bacterium = BacteriumInfected(0)
				i += 1
				continue
			elif cell_str[i+1] == 'd':
				for _ in range(int(num)):
					cell._bacterium = BacteriumWeak(0)
				i += 1
				continue
			elif cell_str[i+1] == 'a':
				cell._antibiotics = int(i)
				i += 1
				continue
			elif cell_str[i+1] == 'v':
				for _ in  range(int(num)):
					cell._bacteriophage = Bacteriophage(4)
				i += 1
				continue
		return cell

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


	def __eq__(self, other):
		if self._antibiotics == other._antibiotics and self.cant_bacteria() == other.cant_bacteria() and self.cant_bacteriophages() == other.cant_bacteriophages() and self.__spawn_bacterium.__eq__(other.__spawn_bacterium) and self.__spawn_other.__eq__(other.__spawn_other):
			for i in range(self.cant_bacteria()):
				if self._bacteria[i].__str__() != other._bacteria[i].__str__():
					return False
			for i in range(self.cant_bacteriophages()):
				if self._bacteriophages[i].__str__() != other._bacteriophages[i].__str__():
					return False
			return True
		return False

	@property
	def _bacteria(self):
		return self.__bacteria
	
	@_bacteria.setter
	def _bacterium(self, bacterium: Bacterium ):
		self.__bacteria.append(bacterium)

	def add_bacterium(self, moves:int, state):
		bacterium = Bacterium.from_string(state)
		bacterium.moves = moves
		self.__bacteria.append(bacterium)
	
	def cant_bacteria(self):
		return self.__bacteria.__len__()
	
	@property
	def _antibiotics(self):
		return self.__antibiotics

	@_antibiotics.setter
	def _antibiotics(self, cant:int):
		self.__antibiotics = cant
	
	def add_antibiotic(self):
		self.__antibiotics += 1
	
	@property
	def _bacteriophages(self):
		return self.__bacteriophages

	@_bacteriophages.setter
	def _bacteriophage(self, bacteriophage:Bacteriophage):
		self.__bacteriophages.append(bacteriophage)
	
	def add_bacteriophage(self, levelInfection:int):
		self.__bacteriophages.append(Bacteriophage(levelInfection))

	def cant_bacteriophages(self):
		return self.__bacteriophages.__len__()

	def is_empty(self):
		if self._antibiotics == 0 and self.cant_bacteria() == 0 and self.cant_bacteriophages() == 0 and not(self.__spawn_bacterium or self.__spawn_other):
			return True
		return False
	
	def cant_ente(self,type):
		if type =='a':
			return self._antibiotics
		if type == 'v':
			return self.cant_bacteriophages()
		cant = 0
		for bacterium in self.__bacteria:
			if type == bacterium.__str__():
				cant += 1
		return cant 
	
	#new
	def is_spwn(self):
		return self.get_spawn_bacterium() or self.get_spawn_other()

	def update_cell(self):
	#aplico regla de sobrepoblación
		if self.cant_bacteria() >= 4:
			self.overpopulation(x,y)

	#si existen bacterias y antibioticos en la misma celda, aplico las reglas de cruzamiento 
		if self._antibiotics > 0 and self.cant_bacteria() > 0:
			if self._antibiotics > cant_bacterias():
				self.high_dose_antibiotic()
			else:
				self.low_dose_antibiotic()
		
		for bacterium in self._bacteria:
			#chequeo las bacterias que están en condiciones de reproducirse
			if bacterium.isReproducible():
				self.bacterium.append(bacterium.reproducir())
		#una vez aplicadas todas las reglas de cruzamiento, le resto un movimiento a todo lo que quedo
		self.add_move()
	
	def high_dose_antibiotic(self):
		#esa celda se queda sin bacterias y sin antibioticos
		self._bacterias = []
		self.cant_antibiotics = 0

	def low_dose_antibiotic(self):
		total_antibiotics = self._antibiotics
		new_bacteria = []
		for bacterium in self._bacteria:
			if bacterium.__str__() == 'f':
				#ver si los movimientos se acumulan
				new_bacterias.append(BacteriumWeak())
		self._bacteria = new_bacteria
		self._antibiotics = 0

	def overpopulation(self):
		strongest = None
		#ciclo para quedarme con la bacteria más fuerte de la celda
		for bacterium in self._bacteria:
			if bacterium.__str__() == 'f':
				strongest = bacterium
				break
			else:
				if bacterium.__str__() == 'b':
					strongest = bacterium
		#si no encontre ninguno fuerte ni normal, es porque tengo todos debiles
		#asigno cualquiera, en este caso el primero
		if strongest == None:
			strongest = self._bacteria[0]
		
		self._bacterium(strongest)

	def add_move(self):
		for bacterium in self._bacteria:
			bacterium.add_move()
		for bacteriophage in self._bacteriophage:
			bacteriophage.add_move()
		