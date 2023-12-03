from models.logic.cell import Cell
from models.logic.Bacterium import BacteriumInfected
from models.logic.Bacteriophage import Bacteriophage
import random

class CellBacteriophage(Cell):

    def __init__(self):
        super().__init__()
        self.__bacteriophages = []
        self.__cant_bacteriophage = 0

    def get_bacteriophages(self):
        return self.__bacteriophages

    def set_bacteriophages(self, array):
        self.__bacteriophages = array

    def get_cant_bacteriophage(self):
        return self.__cant_bacteriophage

    def set_cant_bacteriophage(self, value):
        self.__cant_bacteriophage = value

    def add_bacteriophage(self, entity: Bacteriophage):
        self.__bacteriophages.append(entity)
        self.__cant_bacteriophage += 1

    def update_cell(self, x, y, cant_overpopulation):
        if self.get_cant_bacteria() >= cant_overpopulation:
            self.overpopulation(x, y)

        self.clean_dead_bacteriophages()
        if self.__cant_bacteriophage > 0 and self.get_cant_bacteria() > 0:
            self.infection_to_bacteria(x, y)

        self.update_for_reproduction(x, y)
        self.burst_bacteriumInfected(x, y)

    def clean_dead_bacteriophages(self):
        bacteriophage_to_remove = []

        for bacteriophage in self.__bacteriophages:
            if bacteriophage.moment_death():
                bacteriophage_to_remove.append(bacteriophage)

        for bacteriophage in bacteriophage_to_remove:
            self.__bacteriophages.remove(bacteriophage)
            self.__cant_bacteriophage -= 1
            
    def infection_to_bacteria(self, x, y):
        one_not_infected = False
        power = 0

        for bacteriophage in self.__bacteriophages:
            power += bacteriophage.get_infection()

        infected = []
        for bacterium in self.get_bacteria():
            if not isinstance(bacterium, BacteriumInfected):
                bacterium = bacterium.infect(power)
                bacterium.set_pos(x, y)
                infected.append(bacterium)
                one_not_infected = True
            else:
                bacterium.set_pos(x, y)
                infected.append(bacterium)

        if one_not_infected:
            self.__bacteriophages = []
            self.__cant_bacteriophage = 0

        self.set_bacteria(infected)
        self.set_cant_bacteria(len(infected))

    def burst_bacteriumInfected(self, x, y):
        bacteria_to_remove = []
        for bacterium in self.get_bacteria():
            if isinstance(bacterium, BacteriumInfected) and bacterium.lithic_State():
                bacteria_to_remove.append(bacterium)
                new_bacteriophages = bacterium.exploit()
                for bacteriophage in new_bacteriophages:
                    bacteriophage.set_pos(x, y)
                    self.__bacteriophages.append(bacteriophage)

        for bacterium in bacteria_to_remove:
            self.get_bacteria().remove(bacterium)

        self.set_cant_bacteria(len(self.get_bacteria()))
        self.set_cant_bacteriophage(len(self.__bacteriophages))

    def is_empty(self):
        return self.__cant_bacteriophage == 0 and super().is_empty()

    def __str__(self):
        if self.is_empty():
            return ' '
        res = ''
        cant = self.__cant_bacteriophage
        if cant != 0:
            res = res + cant.__str__() + 'v'
        return super().__str__() + res
    
    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if self.get_cant_bacteriophage() != 0 or other.get_cant_bacteriophage() != 0:
            if not isinstance(other, CellBacteriophage):
                return False
            if self.get_cant_bacteriophage() != other.get_cant_bacteriophage():
                return False
            for i in range(self.get_cant_bacteriophage()):
                if not (self.__bacteriophages[i].get_infection() == other.__bacteriophages[i].get_infection()):
                    return False
        return True

# para schema
    @property
    def _other(self):
        return self.get_cant_bacteriophage()

    @property
    def _power_other(self):
        power = 0

        if self.__bacteriophages != []:
            selected = random.choice(self.__bacteriophages)
            power = selected.get_infection()
        
        return power
# METODOS PARA BEHAVE

    def count_infected(self, grade):
        counter = 0

        for bacterium in self.get_bacteria():
            if isinstance(bacterium, BacteriumInfected) and bacterium.moves == grade:
                counter += 1
        
        return counter

    def count_bacteriophages(self, power):
        counter = 0

        for bacteriophage in self.get_bacteriophages():
            if bacteriophage.get_infection() == power:
                counter += 1
        
        return counter

    def get_bacteriophage(self):

        for bacteriophage in self.get_bacteriophages():
            return bacteriophage
