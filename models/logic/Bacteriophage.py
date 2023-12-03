from .Entity import Entity


class Bacteriophage(Entity):

    def __init__(self, levelInfection: int):
        self.__infection = levelInfection
        self.__pos = (None, None)

    def get_pos(self):
        return self.__pos

    def set_pos(self, row, colum):
        self.__pos = (row, colum)

    def get_infection(self):
        return self.__infection

    def set_infection(self, levelInfection):
        self.__infection = levelInfection

    # Suma
    def add_move(self):
        self.__infection -= 1

    def moment_death(self):
        return self.__infection == 0

    def __str__(self):
        return 'v'

    def __str_aux__(self):
        return self.__str__() + self.__infection.__str__()

    @staticmethod
    def from_string(cell_str):
        if cell_str != 'v':
            raise ValueError(f'Invalid Bacteriofago string: {cell_str}')
        return Bacteriophage(4)
