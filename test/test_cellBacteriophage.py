import pytest
from models.logic.CellBacteriophage import CellBacteriophage
from models.logic.Bacterium import *
from models.logic.Bacteriophage import Bacteriophage

@pytest.fixture
def cellBacteriophage():
    return CellBacteriophage()

@pytest.fixture
def moves_for_explotion():
    bacterium = Bacterium(0)
    moves_for_explotion = bacterium.moves_for_explotion

    return moves_for_explotion

@pytest.fixture
def initial_power():
    bacterium = Bacterium(0)
    initial_power_infection = bacterium.power_infection_after_explotion

    return initial_power_infection

@pytest.fixture
def cant_after_explotion():
    bacterium = Bacterium(0)
    cant_after_explotion = bacterium.cant_bacteriophages_after_explotion

    return cant_after_explotion

def test_not_eq_cell_bacteriophage(cellBacteriophage):
    cell_aux = CellBacteriophage()
    cellBacteriophage.add_bacteriophage(Bacteriophage(4))
    cell_aux.add_bacteriophage(Bacteriophage(3))
    assert not cellBacteriophage.__eq__(cell_aux)


def test_add_bacteriophage(cellBacteriophage):
    cellBacteriophage.add_bacteriophage(Bacteriophage(4))
    assert cellBacteriophage.get_cant_bacteriophage() == 1
    assert str(cellBacteriophage) == '1v'
    assert cellBacteriophage.get_bacteriophages()[0].get_infection() == 4


def test_add_bacteriophage_and_bacterium_eq(cellBacteriophage):
    cellBacteriophage.add_bacterium(BacteriumNormal(0))
    for _ in range(5):
        cellBacteriophage.add_bacteriophage(Bacteriophage(4))
    cell_aux = CellBacteriophage()
    cell_aux.add_bacterium(BacteriumNormal(0))
    for _ in range(5):
        cell_aux.add_bacteriophage(Bacteriophage(4))
    assert cellBacteriophage.__eq__(cell_aux)


def test_to_string_1(cellBacteriophage):
    cellBacteriophage.add_bacterium(BacteriumNormal(0))
    cellBacteriophage.add_bacterium(BacteriumStrong(0))
    cellBacteriophage.add_bacterium(BacteriumInfected(0))
    cellBacteriophage.add_bacterium(BacteriumWeak(0))
    assert cellBacteriophage.get_cant_bacteriophage() == 0
    cellBacteriophage.add_bacteriophage(Bacteriophage(4))
    cellBacteriophage.add_bacteriophage(Bacteriophage(4))
    assert cellBacteriophage.get_cant_bacteriophage() == 2
    assert str(cellBacteriophage) == '1b1f1d1i2v'


def test_burst_burst_bacteriumInfected(cellBacteriophage, moves_for_explotion, cant_after_explotion):
    cellBacteriophage.add_bacterium(BacteriumInfected(moves_for_explotion))
    cellBacteriophage.burst_bacteriumInfected(None, None)
    n = str(cant_after_explotion)
    assert str(cellBacteriophage) == f'{n}v'


def test_3_burst_bacteriumInfected(cellBacteriophage, moves_for_explotion, cant_after_explotion):
    cellBacteriophage.add_bacterium(BacteriumInfected(moves_for_explotion))
    cellBacteriophage.add_bacterium(BacteriumInfected(moves_for_explotion))
    cellBacteriophage.add_bacterium(BacteriumInfected(moves_for_explotion))
    cellBacteriophage.burst_bacteriumInfected(None, None)
    n = str(3*cant_after_explotion)
    assert str(cellBacteriophage) == f'{n}v'
