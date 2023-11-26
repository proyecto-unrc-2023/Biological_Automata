import pytest

from models.logic.cell import Cell
from models.logic.Bacterium import *

@pytest.fixture
def cell():
    return (Cell())

@pytest.fixture
def moves_for_reproduction():
    bacterium = Bacterium(0)
    moves_for_reproduction = bacterium.moves_for_reproduction

    return moves_for_reproduction

@pytest.fixture
def cant_overpopulation():
    return 4

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
    assert str(cell.get_bacteria()[0]) == 'b'


def test_to_string_cell(cell):
    cell.add_bacterium(BacteriumNormal(2))
    cell.add_bacterium(BacteriumStrong(2))
    cell.add_bacterium(BacteriumWeak(4))
    cell.add_bacterium(BacteriumInfected(1))
    assert cell.bacterias == ["b", "f", "d", "i"]
    assert cell.get_cant_bacteria() == 4

    assert str(cell) == '1b1f1d1i'

    assert cell.count_bacteria_with_moves("normal", 2) == 1

def test_overpoblation(cell, cant_overpopulation):
    for _ in range (cant_overpopulation):
        cell.add_bacterium(BacteriumNormal(0))
        cell.add_bacterium(BacteriumStrong(0))

    cell.overpopulation(None, None)
    assert cell.get_cant_bacteria() == 1


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


def test_overpoblation_without_strongest(cell, cant_overpopulation):
    for _ in range (cant_overpopulation):
        cell.add_bacterium(BacteriumNormal(0))
        cell.add_bacterium(BacteriumWeak(0))

    cell.overpopulation(None, None)

    assert str(cell) == '1b'


def test_overpoblation_debiles(cell, cant_overpopulation):
    for _ in range (cant_overpopulation):
        cell.add_bacterium(BacteriumWeak(0))

    cell.overpopulation(None, None)
    assert str(cell) == '1d'


def test_update_cell_with_1_bacterium_ready_to_reproduce(cell, moves_for_reproduction):
    cell.add_bacterium(BacteriumNormal(moves_for_reproduction))
    cell.update_for_reproduction(None, None)
    assert cell.get_cant_bacteria() == 2


def test_update_cell_with_1_bacterium_not_ready_to_reproduce(cell, moves_for_reproduction):
    cell.add_bacterium(BacteriumNormal(moves_for_reproduction-1))
    cell.update_for_reproduction(None, None)
    assert str(cell) == '1b'


def test_update_cell_with_4_bacterium_normal_ready_to_reproduce(cell, cant_overpopulation, moves_for_reproduction):
    for _ in range (cant_overpopulation):
        cell.add_bacterium(BacteriumNormal(moves_for_reproduction))

    cell.overpopulation(None, None)
    cell.update_for_reproduction(None, None)
    assert cell.get_cant_bacteria() == 2

