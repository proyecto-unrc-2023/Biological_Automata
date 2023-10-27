import pytest

from models.logic.cell import Cell
from models.logic.Bacterium import BacteriumNormal, BacteriumStrong
from models.logic.Bacterium import BacteriumWeak, BacteriumInfected

@pytest.fixture
def cell():
    return Cell()

# CELL TEST

def test_initial_cell(cell):
    assert cell.get_cant_bacteria() == 0
    assert not cell.get_spawn()
    assert cell.is_empty()


def test_spawn_cell(cell):
    cell.set_spawn()
    assert cell.get_cant_bacteria() == 0
    assert cell.get_spawn()


def test_spawn_cell_not_empty(cell):
    cell.set_spawn()
    with pytest.raises(ValueError) as e:
        cell.set_spawn()
    assert str(e.value) == 'celda ocupada'


def test_eq_cell(cell):
    cell_aux = Cell()
    cell_aux.set_spawn()
    cell.set_spawn()
    assert cell.__eq__(cell_aux)


def test_not_eq_cell(cell):
    cell_aux = Cell()
    cell_aux.set_spawn()
    assert not cell.__eq__(cell_aux)


def test_not_eq_cell_bacterium(cell):
    cell_aux = Cell()
    cell_aux.add_bacterium(BacteriumNormal(1))
    cell.add_bacterium(BacteriumStrong(1))
    assert not cell.__eq__(cell_aux)


def test_add_bacterium(cell):
    cell.add_bacterium(BacteriumNormal(0))
    assert cell.get_cant_bacteria() == 1
    assert cell.get_bacteria()[0].__str__() == 'b'


def test_to_string_cell(cell):
    cell.add_bacterium(BacteriumNormal(2))
    cell.add_bacterium(BacteriumStrong(4))
    cell.add_bacterium(BacteriumWeak(4))
    cell.add_bacterium(BacteriumInfected(1))
    assert cell.get_cant_bacteria() == 4
    assert str(cell) == '1b1f1d1i'


def test_overpoblation_strongest(cell):
    cell.add_bacterium(BacteriumNormal(0))
    cell.add_bacterium(BacteriumNormal(0))
    cell.add_bacterium(BacteriumWeak(0))
    cell.add_bacterium(BacteriumStrong(0))
    cell.overpopulation(None, None)
    assert str(cell) == '1f'

def test_cant_ente_bacterium(cell):
    cell.add_bacterium(BacteriumNormal(0))
    cell.add_bacterium(BacteriumNormal(0))
    cell.add_bacterium(BacteriumInfected(0))
    cell.add_bacterium(BacteriumWeak(0))
    cell.add_bacterium(BacteriumStrong(0))
    assert cell.cant_ente('b') == 2
    assert cell.cant_ente('f') == 1 
    assert cell.cant_ente('i') == 1 
    assert cell.cant_ente('d') == 1 


def test_overpoblation_without_strongest(cell):
    cell.add_bacterium(BacteriumNormal(0))
    cell.add_bacterium(BacteriumNormal(0))
    cell.add_bacterium(BacteriumWeak(0))
    cell.add_bacterium(BacteriumWeak(0))
    cell.overpopulation(None, None)
    assert str(cell) == '1b'


def test_overpoblation_debiles(cell):
    cell.add_bacterium(BacteriumWeak(0))
    cell.add_bacterium(BacteriumWeak(0))
    cell.add_bacterium(BacteriumWeak(0))
    cell.add_bacterium(BacteriumWeak(0))
    cell.overpopulation(None, None)
    assert str(cell) == '1d'


def test_update_cell_with_1_bacterium_ready_to_reproduce(cell):
    cell.add_bacterium(BacteriumNormal(3))
    cell.update_for_reproduction(None, None)
    assert cell.get_cant_bacteria() == 2


def test_update_cell_with_1_bacterium_not_ready_to_reproduce(cell):
    cell.add_bacterium(BacteriumNormal(2))
    cell.update_for_reproduction(None, None)
    assert str(cell) == '1b'


def test_update_cell_with_4_bacterium_normal_ready_to_reproduce(cell):
    cell.add_bacterium(BacteriumNormal(3))
    cell.add_bacterium(BacteriumNormal(3))
    cell.add_bacterium(BacteriumNormal(3))
    cell.add_bacterium(BacteriumNormal(3))
    cell.overpopulation(None, None)
    cell.update_for_reproduction(None,None )
    assert cell.get_cant_bacteria() == 2

# def test_add_move_to_bacteriums(cell):
#     cell.add_bacterium(0, 'f')
#     cell.add_bacterium(0, 'f')
#     cell.add_bacterium(0, 'f')

# CELL OF BACTERIOPHAGES TEST


# CELL OF ANTIBIOTIC TEST

