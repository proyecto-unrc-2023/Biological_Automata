from models.logic.cell import Cell
from models.logic.Bacterium import BacteriumStrong, BacteriumWeak
from models.logic.Antibiotic import Antibiotic


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

    def update_cell(self, x, y, cant_overpopulation):
        if self.get_cant_bacteria() >= cant_overpopulation:
            self.overpopulation(x, y)
        #aplico las reglas de cruzamiento entre bacterias y antibioticos
        if self.get_cant_antibiotic() > 0 and self.get_cant_bacteria() > 0:
            if self.get_cant_antibiotic() > self.get_cant_bacteria():
                self.high_dose(x, y)
            else:
                self.low_dose(x, y)
        self.update_for_reproduction(x, y)
        self.update_for_recovery(x, y)
        self.clean_harmless_antibiotic()

    def high_dose(self, x, y):
        self.set_bacteria([])
        self.set_cant_bacteria(0)
        for antibiotic in self.__antibiotics:
            antibiotic.decrease_power()
            if antibiotic.get_power() > 0:
                antibiotic.set_pos(x,y)

    def low_dose(self, x, y):
        new_bacteria = []
        for bacterium in self.get_bacteria():
            if isinstance(bacterium, BacteriumStrong):
                bact_weak = BacteriumWeak(0)
                bact_weak.set_pos(x, y)
                new_bacteria.append(bact_weak)

        self.set_bacteria(new_bacteria)
        self.set_cant_bacteria(len(new_bacteria))
        for antibiotic in self.__antibiotics:
            antibiotic.decrease_power()
            if antibiotic.get_power() > 0:
                antibiotic.set_pos(x,y)

    def update_for_recovery(self, x, y):
        bacteria_to_add = []
        bacteria_to_remove = []
        for bacterium in self.get_bacteria():
            if bacterium.isRecoverable():
                recovered = bacterium.recover()
                recovered.set_pos(x, y)
                bacteria_to_add.append(recovered)
                bacteria_to_remove.append(bacterium)

        for bacterium in bacteria_to_add:
            self.get_bacteria().append(bacterium)
        for bacterium in bacteria_to_remove:
            self.get_bacteria().remove(bacterium)

        self.set_cant_bacteria(len(self.get_bacteria()))

    def clean_harmless_antibiotic(self):
        antibiotic_to_remove = []
        for antibiotic in self.__antibiotics:
            if antibiotic.is_harmless():
                antibiotic_to_remove.append(antibiotic)

        for antibiotic in antibiotic_to_remove:
            self.__antibiotics.remove(antibiotic)
            self.__cant_antibiotic -= 1

    def is_empty(self):
        return self.__cant_antibiotic == 0 and super().is_empty()

    def __str__(self):
        res = ''
        cant = self.__cant_antibiotic
        if cant != 0:
            res = res + cant.__str__() + 'a'
        return super().__str__() + res

    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if self.get_cant_antibiotic() != 0 or other.get_cant_antibiotic() != 0:
            if not isinstance(other, CellAntibiotic):
                return False
            if self.get_cant_antibiotic() != other.get_cant_antibiotic():
                return False
        return True

##para schema
    @property
    def _other(self):
        return self.get_cant_antibiotic()

#para behave
    def count_antibiotic(self,power):
        counter = 0

        for antibiotic in self.__antibiotics:
            if antibiotic.get_power() == power:
                counter += 1
        
        return counter
