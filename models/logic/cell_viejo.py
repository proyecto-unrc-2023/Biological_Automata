from models.logic.Bacterium import *
from models.logic.Bacteriophage import Bacteriophage
from models.logic.Antibiotic import Antibiotic

class Cell:

	def __init__(self):
		self.__bacteria = []
		self.__antibiotics = []
		self.__bacteriophages = []
		self.__spawn_bacterium = False
		self.__spawn_other = False

	def __str__(self):
		if self.is_empty():
			return ' '

		if self.__spawn_bacterium:
			return 'sb'

		if self.__spawn_other:
			return 'so'

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
		cant =  self.cant_ente('v')
		if cant != 0:
			res = res + cant.__str__() + 'v'
		return res

	@staticmethod
	def from_string(cell_str):
		cell = Cell()
		for i in range (0,cell_str.__len__()-1,2):
			num = cell_str[i]
			if cell_str == 'sb':
				cell.set_spawn_bacterium()
				break
			if cell_str == 'so':
				cell.set_spawn_other()
				break
			if cell_str[i+1] == 'b':
				for _ in  range(int(num)):
					cell._bacterium = BacteriumNormal(0)
				continue
			if cell_str[i+1] == 'f':
				for _ in  range(int(num)):
					cell._bacterium = BacteriumStrong(0)
				continue
			elif cell_str[i+1] == 'i':
				for _ in range(int(num)):
					cell._bacterium = BacteriumInfected(0)
				continue
			elif cell_str[i+1] == 'd':
				for _ in range(int(num)):
					cell._bacterium = BacteriumWeak(0)
				continue
			elif cell_str[i+1] == 'a':
				for _ in range(int(num)):
					cell.__antibiotics.append(Antibiotic())
				continue
			elif cell_str[i+1] == 'v':
				for _ in  range(int(num)):
					cell._bacteriophages = Bacteriophage(4)
				continue
			else:
				raise ValueError('string invalido')
		return cell

	def get_spawn_other(self):
		return self.__spawn_other

	def set_spawn_other(self):
		if not self.is_empty():
			raise ValueError ('celda ocupada')
		self.__spawn_other = True

	def get_spawn_bacterium(self):
		return self.__spawn_bacterium

	def set_spawn_bacterium(self):
		if not self.is_empty():
			raise ValueError('celda ocupada')
		self.__spawn_bacterium = True


	def __eq__(self, other):
		if self.__antibiotics != other._antibiotics:
			return False
		if self.cant_bacteria() != other.cant_bacteria():
			return False
		if self.cant_bacteriophages() != other.cant_bacteriophages():
			return False
		if not self.__spawn_bacterium.__eq__(other.__spawn_bacterium):
			return False
		if not self.__spawn_other.__eq__(other.__spawn_other):
			return False
		for i in range(self.cant_bacteria()):
			if self._bacteria[i].__str__() != other._bacteria[i].__str__():
				return False
		for i in range(self.cant_bacteriophages()):
			if self.__bacteriophages[i].__str_aux__() != other._bacteriophages[i].__str_aux__():
				return False
		return True

	@property
	def _bacteria(self):
		return self.__bacteria

	@_bacteria.setter
	def _bacterium(self, bacterium: Bacterium):
		self.__bacteria.append(bacterium)


	def add_bacterium(self, moves:int, state):
		bacterium = Bacterium.from_string(state)
		bacterium.moves = moves
		self.__bacteria.append(bacterium)

	def cant_bacteria(self):
		return self.__bacteria.__len__()

	@property
	def _antibiotics(self):
		return self.__antibiotics.__len__()


	def get_antibiotics(self):
		return self.__antibiotics

	@_antibiotics.setter
	def _antibiotics(self, cant:int):
		for _ in range(cant):
			self.__antibiotics.append(Antibiotic())

	def add_antibiotic(self, antibiotic:Antibiotic):
		self.__antibiotics.append(antibiotic)

	@property
	def _bacteriophages(self):
		return self.__bacteriophages

	@_bacteriophages.setter
	def _bacteriophages(self, bacteriophage:Bacteriophage):
		self.__bacteriophages.append(bacteriophage)

	def add_bacteriophage(self, levelInfection:int):
		bacteriophage = Bacteriophage(levelInfection)
		self.__bacteriophages.append(bacteriophage)

	def cant_bacteriophages(self):
		return self.__bacteriophages.__len__()

	def is_empty(self):
		if self._antibiotics != 0:
			return False
		if self.cant_bacteria() != 0:
			return False
		if self.cant_bacteriophages() != 0:
			return False
		if self.__spawn_bacterium or self.__spawn_other:
			return False
		return True

	def is_spawn(self):
		return self.get_spawn_bacterium() or self.get_spawn_other()

	def is_spawn_bacterium(self):
		return self.get_spawn_bacterium()

	def is_spawn_other(self):
		return self.get_spawn_other()

	def update_cell(self,x,y):
		#aplico regla de sobrepoblación


		if self.cant_bacteria() >= 4:
			self.overpopulation(x,y)

		#si existen bacterias y antibioticos en la misma celda, aplico las reglas de cruzamiento
		if self._antibiotics > 0 and self.cant_bacteria() > 0:
			if self._antibiotics > self.cant_bacteria():
				self.high_dose_antibiotic()
			else:
				self.low_dose_antibiotic(x,y)

		#si existen bacteriofagos y bacterias en la misma celda, aplico las reglas de cruzamiento
		if self.cant_bacteriophages() > 0 and self.cant_bacteria() > 0:
			self.infection_to_bacteria(x,y)

		#actualizo por la reproduccion de bacterias
		self.update_for_reproduction(x,y)

		#actualizo por la recuperación de bacterias
		self.update_for_recovery(x,y)

		#actualizo por bacteriofagos que se quedaron sin movimientos
		self.update_for_death_bacteriophages()

		#actualizo por la explosion de bacteriofagos
		self.burst_bacteriophage(x,y)

	#metodo auxiliar para update_cell()
	def high_dose_antibiotic(self):
		#esa celda se queda sin bacterias y sin antibioticos
		self.__bacteria = []
		self.__antibiotics = []

	#metodo auxiliar para update_cell()
	def low_dose_antibiotic(self,x,y):
		# total_antibiotics = self._antibiotics
		new_bacteria = []
		for bacterium in self._bacteria:
			if bacterium.__str__() == 'f':
				#ver si los movimientos se acumulan
				bact_debil = BacteriumWeak(0)
				bact_debil.set_pos(x,y)
				new_bacteria.append(bact_debil)
		self.__bacteria = new_bacteria
		self.__antibiotics = []

	#metodo auxiliar para update_cell()
	def overpopulation(self,x,y):
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

		self.__bacteria.clear()
		strongest.set_pos(x,y)
		self.__bacteria.append(strongest)

	#metodo auxiliar para update_cell()
	def infection_to_bacteria(self,x,y):
		one_not_infected = False
		power = 0

		for bacteriophage in self._bacteriophages:
			power += bacteriophage.infection

		power = min(power, 4)

		infected = []
		for bacterium in self._bacteria:
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

	#metodo auxiliar para update_cell()
	def update_for_reproduction(self,x,y):
		for bacterium in self._bacteria:
			#chequeo las bacterias que están en condiciones de reproducirse
			if bacterium.isReproducible():
				bacteria_reproducida = bacterium.reproducir()
				bacteria_reproducida.set_pos(x,y)
				self._bacterium = bacteria_reproducida

	#metodo auxiliar para update_cell()
	def update_for_recovery(self,x,y):
		bacteria_to_add = []
		bacteria_to_remove = []
		for bacterium in self._bacteria:
			#chequeo las bacterias debiles que están en condiciones de recuperarse
			if bacterium.isRecoverable():
				bacteria_recuperada = bacterium.recover()
				bacteria_recuperada.set_pos(x,y)
				bacteria_to_add.append(bacteria_recuperada)

				bacteria_to_remove.append(bacterium)

		for bacterium in bacteria_to_add:
			self._bacterium.append(bacterium)

		for bacterium in bacteria_to_remove:
			self._bacterium.remove(bacterium)

	#metodo auxiliar para update_cell()
	def burst_bacteriophage(self,x,y):
		bacteria_to_remove = []
		for bacterium in self.__bacteria:
			if isinstance(bacterium,BacteriumInfected) and bacterium.lithic_State():
						bacteria_to_remove.append(bacterium)
						for _ in range(4):
							bacteriophage = Bacteriophage(4)
							bacteriophage.set_pos(x,y)
							self.__bacteriophages.append(bacteriophage)

		for bacterium in bacteria_to_remove:
			self._bacterium.remove(bacterium)

	#metodo auxiliar para update_cell()
	def update_for_death_bacteriophages(self):
		bacteriophage_to_remove = []

		for bacteriophage in self._bacteriophages:
			if bacteriophage.moment_death():
				bacteriophage_to_remove.append(bacteriophage)

		for bacteriophage in bacteriophage_to_remove:
			self._bacteriophages.remove(bacteriophage)

	def add_move(self):
		for bacterium in self._bacteria:
			bacterium.add_move()
		for bacteriophage in self._bacteriophages:
			bacteriophage.add_move()


	#METODOS PARA IMPLEMENTAR STEPS EN BEHAVE

	def get_infected(self):
		for bacterium in self._bacterium:
			if isinstance(bacterium, BacteriumInfected):
				return bacterium

	def get_bacteriophage(self):
		return self.__bacteriophages[0]

	def get_normal(self):
		for bacterium in self._bacterium:
			if isinstance(bacterium, BacteriumNormal):
				return bacterium

	def get_strong(self):
		for bacterium in self._bacterium:
			if isinstance(bacterium, BacteriumStrong):
				return bacterium

	def get_weak(self):
		for bacterium in self._bacterium:
			if isinstance(bacterium, BacteriumWeak):
				return bacterium

	def cant_type_bacterium(self, ente):
		counter_normal = 0
		counter_weak = 0
		counter_strong = 0

		for bacteria in self._bacteria:
			if isinstance(bacteria, BacteriumNormal):
				counter_normal += 1
			elif isinstance(bacteria, BacteriumWeak):
				counter_weak += 1
			elif isinstance(bacteria, BacteriumStrong):
				counter_strong += 1

		if ente == "bacteria normal":
			return counter_normal
		if ente == "bacteria debil":
			return counter_weak
		if ente == "bacteria fuerte":
			return counter_strong

	def count_infected(self, grade):
		counter = 0

		for bacteria in self._bacteria:
			if isinstance(bacteria, BacteriumInfected):
				if bacteria.moves == grade:

					counter += 1

		return counter

	def count_bacteriophages(self, power):
		counter = 0

		for bacteriophage in self._bacteriophages:
			if bacteriophage.infection == power:
				counter += 1

		return counter

	def count_bacteria_with_moves(self, type, moves):
		counter_normal = 0
		counter_weak = 0
		counter_strong = 0

		for bacteria in self._bacteria:
			if isinstance(bacteria, BacteriumNormal) and bacteria.moves == moves:
				counter_normal += 1
			elif isinstance(bacteria, BacteriumWeak) and bacteria.moves == moves:
				counter_weak += 1
			elif isinstance(bacteria, BacteriumStrong) and bacteria.moves == moves:
				counter_strong += 1

		if type == "normal":
			return counter_normal
		if type == "debil":
			return counter_weak
		if type == "fuerte":
			return counter_strong

	def cant_total(self):
		return self.cant_bacteriophages() + self.cant_bacteria() + self._antibiotics

	def cant_ente(self,type):
		if type =='a':
			return self._antibiotics
		if type == 'v':
			return self.cant_bacteriophages()
		if type == 'bacterias':
			return self.cant_bacteria()
		cant = 0
		for bacterium in self.__bacteria:
			if type == bacterium.__str__():
				cant += 1
		return cant
