
class Celda:

	def __init__(self):
		self.bacterias = []
		self.cant_antibiotic = 0
		self.virus = []
		self.spawn_bacterium = False
		self.spawn_other = False


	def create_spawn_other(self):
		self.spawn_other = True

	def create_spawn_bacterium(self):
		self.spawn_bacterium = True

	def _spawn_other(self):
		return self.spawn_other
	
	
	def _spawn_bacterium(self):
		return self.spawn_bacterium

	def __eq__(self, other):
		return isinstance(other, Celda)
	
	def get_bacterias(self):
		return self.bacterias
    
	def get_cant_bacterias(self):
		return self.bacterias.__len__
	
