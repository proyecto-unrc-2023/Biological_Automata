from models.logic.Bacterium import Bacterium, BacteriumNormal, BacteriumStrong


class Cell:
    def __init__(self):
        self.__bacteria = []
        self.__cant_bacteria = 0
        self.__spawn = False

    def get_bacteria(self):
        return self.__bacteria

    def set_bacteria(self, array):
        self.__bacteria = array
        self.__cant_bacteria = len(array)

    def get_spawn(self):
        return self.__spawn

    def set_spawn(self):
        if not self.is_empty():
            raise ValueError('celda ocupada')
        self.__spawn = True

    def get_cant_bacteria(self):
        return self.__cant_bacteria

    def set_cant_bacteria(self, value):
        self.__cant_bacteria = value

    def add_bacterium(self, entity: Bacterium):
        self.__bacteria.append(entity)
        self.__cant_bacteria += 1

    def update_for_reproduction(self, x, y):
        for bacterium in self.__bacteria:
            # chequeo las bacterias que están en condiciones de reproducirse
            if bacterium.isReproducible():
                new_bacterium = bacterium.reproducir()
                new_bacterium.set_pos(x, y)
                self.__bacteria.append(new_bacterium)
                self.__cant_bacteria += 1

    def overpopulation(self, x, y):
        live = None
        # ciclo para quedarme con la bacteria más fuerte de la celda
        for bacterium in self.__bacteria:
            if not isinstance(bacterium, BacteriumStrong):
                if isinstance(bacterium, BacteriumNormal):
                    live = bacterium
            else:
                live = bacterium
                break

        if live is None:
            live = self.__bacteria[0]

        self.__bacteria.clear()
        live.set_pos(x, y)
        self.__bacteria.append(live)
        self.__cant_bacteria = 1

    def __eq__(self, other):
        if self.get_cant_bacteria() != other.get_cant_bacteria():
            return False
        if not self.__spawn.__eq__(other.get_spawn()):
            return False
        for i in range(self.get_cant_bacteria()):
            if str(self.__bacteria[i]) != str(other.get_bacteria()[i]):
                return False
        return True

    def is_empty(self):
        return self.__cant_bacteria == 0 and (not self.__spawn)

    def __str__(self):
        if self.is_empty():
            return ' '
        res = ''
        cant = self.cant_ente('b')
        if cant != 0:
            res = res + str(cant) + 'b'
        cant = self.cant_ente('f')
        if cant != 0:
            res = res + str(cant) + 'f'
        cant = self.cant_ente('d')
        if cant != 0:
            res = res + str(cant) + 'd'
        cant = self.cant_ente('i')
        if cant != 0:
            res = res + str(cant) + 'i'
        return res

# Metodos de behave

    def cant_ente(self, type):
        cant = 0
        for bacterium in self.__bacteria:
            if type == str(bacterium):
                cant += 1
        return cant

    def get_bacterium(self, type):
        for bacterium in self.__bacteria:
            if type == str(bacterium):
                return bacterium
