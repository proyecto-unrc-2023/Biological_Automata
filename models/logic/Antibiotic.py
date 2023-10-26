from .Entity import Entity


class Antibiotic(Entity):

    def __init__(self):
        self.__pos = (None, None)

    def get_pos(self):
        return self.__pos

    def set_pos(self, row, colum):
        self.__pos = (row, colum)

    def add_move(self):
        pass

    @staticmethod
    def from_string(cell_str):
        if cell_str == 'a':
            return Antibiotic()
        raise ValueError("Invalid input: 'cell_str' must be 'a'")

    def __str__(self):
        return 'a'
