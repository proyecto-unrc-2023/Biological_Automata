from .Entity import Entity


class Antibiotic(Entity):

    def __init__(self, power=3):
        self.__pos = (None, None)
        self.__power = power

    def get_pos(self):
        return self.__pos

    def set_pos(self, row, colum):
        self.__pos = (row, colum)

    def get_power(self):
        return self.__power
    
    def is_harmless(self):
        return self.__power == 0
    
    def decrease_power(self):
        self.__power -= 1

    def add_move(self):
        pass

    @staticmethod
    def from_string(cell_str):
        if cell_str == 'a':
            return Antibiotic()
        raise ValueError("Invalid input: 'cell_str' must be 'a'")

    def __str__(self):
        return 'a'
