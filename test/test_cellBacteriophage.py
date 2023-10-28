import pytest
from models.logic.CellBacteriophage import CellBacteriophage
from models.logic.Bacterium import BacteriumInfected, BacteriumNormal
from models.logic.Bacterium import BacteriumWeak, BacteriumStrong
from models.logic.Bacteriophage import Bacteriophage


@pytest.fixture
def cellBacteriophage():
    return CellBacteriophage()


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


def test_burst_burst_bacteriumInfected(cellBacteriophage):
    cellBacteriophage.add_bacterium(BacteriumInfected(4))
    cellBacteriophage.burst_bacteriumInfected(None, None)
    assert str(cellBacteriophage) == '4v'


def test_3_burst_bacteriumInfected(cellBacteriophage):
    cellBacteriophage.add_bacterium(BacteriumInfected(4))
    cellBacteriophage.add_bacterium(BacteriumInfected(4))
    cellBacteriophage.add_bacterium(BacteriumInfected(4))
    cellBacteriophage.burst_bacteriumInfected(None, None)
    assert str(cellBacteriophage) == '12v'
