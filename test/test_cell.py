import pytest

from models.logic.cell import Cell
from models.logic.CellAntibiotic import CellAntibiotic
from models.logic.CellBacteriophage import CellBacteriophage
from models.logic.Bacterium import BacteriumNormal, BacteriumStrong
from models.logic.Bacterium import BacteriumWeak, BacteriumInfected
from models.logic.Antibiotic import Antibiotic
from models.logic.Bacteriophage import Bacteriophage


@pytest.fixture
def cell():
    return Cell()


@pytest.fixture
def cellAntibiotic():
    return CellAntibiotic()


@pytest.fixture
def cellBacteriophage():
    return CellBacteriophage()


# CELL TEST

def test_initial_cell(cell):
    # assert cell._antibiotics == 0
    assert cell.get_cant_bacteria() == 0
    # assert cell.cant_bacteriophages() == 0
    # assert not cell.get_spawn_bacterium()
    # assert not cell.is_spawn_bacterium()
    assert not cell.get_spawn()
    # assert not cell.is_spawn_other()
    assert cell.is_empty()


def test_spawn_cell(cell):
    cell.set_spawn()
    # assert cell._antibiotics == 0
    assert cell.get_cant_bacteria() == 0
    # assert cell.cant_bacteriophages() == 0
    assert cell.get_spawn()
    # assert cell.get_spawn_other() == False


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
    # cell.set_spawn_bacterium()
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
    assert str(cell) == '1b1f1d1i'


def test_overpoblation_strongest(cell):
    cell.add_bacterium(BacteriumNormal(0))
    cell.add_bacterium(BacteriumNormal(0))
    cell.add_bacterium(BacteriumWeak(0))
    cell.add_bacterium(BacteriumStrong(0))
    cell.overpopulation(None, None)
    assert str(cell) == '1f'


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


# CELL OF BACTERIOPHAGES TEST

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
    assert cell.__eq__(cell_aux)


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


def test_update_cell_with_3_strongs(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.update_cell(None, None)
    assert str(cellAntibiotic) == '3f'



# def test_to_string_2(cell):
#     cell.add_bacterium(0,'b')
#     cell.add_bacterium(0,'f')
#     cell.add_bacterium(0,'b')
#     assert cell.cant_ente('b') == 2
#     assert cell.cant_ente('f') == 1
#     cell.add_bacteriophage(4)
#     cell.add_bacteriophage(4)
#     assert cell.__str__() == '2b1f2v'


# CELL OF ANTIBIOTIC TEST

def test_add_antibiotics(cellAntibiotic):
    cellAntibiotic.add_antibiotic(Antibiotic())
    assert cellAntibiotic.get_cant_antibiotic() == 1


def test_antibiotics(cellAntibiotic):
    for _ in range(10):
        cellAntibiotic.add_antibiotic(Antibiotic())
    assert cellAntibiotic.get_cant_antibiotic() == 10


def test_add_antibiotic_and_bacterium_eq(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    for _ in range(5):
        cellAntibiotic.add_antibiotic(Antibiotic())
    cell_aux = CellAntibiotic()
    cell_aux.add_bacterium(BacteriumNormal(0))
    for _ in range(5):
        cell_aux.add_antibiotic(Antibiotic())
    assert cell.__eq__(cell_aux)


def test_low_dose_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumWeak(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.low_dose(None, None)
    assert str(cellAntibiotic) == '1d'


def test_high_dose_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.high_dose()
    assert str(cellAntibiotic) == ' '


def test_update_cell_with_3_strongs_and_1_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.update_cell(None, None)
    assert str(cellAntibiotic) == '3d'


def test_update_cell_with_2_strongs_and_3_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.update_cell(None, None)
    assert str(cellAntibiotic) == ' '


def test_update_cell_with_1_strongs_1_weak_and_2_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumWeak(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.update_cell(None, None)
    assert str(cellAntibiotic) == '1d'


def test_update_cell_with_2_strongs_4_normal_and_1_weak(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumWeak(0))
    cellAntibiotic.update_cell(None, None)
    assert str(cellAntibiotic) == '1f'


def test_update_cell_with_1_strongs_4_normal_1_weak_and_2_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumWeak(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.update_cell(None, None)
    assert str(cellAntibiotic) == ' '





# def test_update_cell_with_1_weak_ready_to_recover(cell):
#     cell.add_bacterium(6, 'd')
#     cell.update_cell(None,None)
#     assert cell.__str__() == '1f'

# def test_update_cell_with_1_weak_not_ready_to_recover(cell):
#     cell.add_bacterium(3, 'd')
#     cell.update_cell(None,None)
#     assert cell.__str__() == '1d'

# def test_update_cell_with_2_weak_ready_to_recover_and_1_weak_not_ready(cell):
#     cell.add_bacterium(6, 'd')
#     cell.add_bacterium(6, 'd')
#     cell.add_bacterium(3, 'd')
#     cell.update_cell(None,None)
#     assert cell.__str__() == '2f1d'

# def test_update_cell_with_4_weak_ready_to_recover_and_1_weak_not_ready(cell):
#     cell.add_bacterium(6, 'd')
#     cell.add_bacterium(6, 'd')
#     cell.add_bacterium(6, 'd')
#     cell.add_bacterium(6, 'd')
#     cell.add_bacterium(3, 'd')
#     cell.update_cell(None,None)
#     assert cell.__str__() == '1f'

# def test_update_cell_with_4_bacterium_normal_ready_to_reproduce(cell):
#     cell.add_bacterium(3, 'b')
#     cell.add_bacterium(3, 'b')
#     cell.add_bacterium(3, 'b')
#     cell.add_bacterium(3, 'b')
#     cell.update_cell(None,None)
#     assert cell.cant_bacteria() == 2

# def test_update_cell_with_4_bacterium_strong_amd_2_antibiotics(cell):
#     cell.add_bacterium(0, 'f')
#     cell.add_bacterium(0, 'f')
#     cell.add_bacterium(0, 'f')
#     cell.add_bacterium(0, 'f')
#     cell.add_antibiotic(Antibiotic())
#     cell.add_antibiotic(Antibiotic())
#     cell.update_cell(None,None)
#     assert cell.__str__() == ' '

# def test_add_move_to_bacteriums(cell):
#     cell.add_bacterium(0, 'f')
#     cell.add_bacterium(0, 'f')
#     cell.add_bacterium(0, 'f')

# def test_burst_bacteriophage(cell):
#     cell.add_bacterium(4,'i')
#     cell.burst_bacteriophage(None,None)
#     assert cell.__str__() == '4v'

# def test_3_burst_bacteriophage(cell):
#     cell.add_bacterium(4,'i')
#     cell.add_bacterium(4,'i')
#     cell.add_bacterium(4,'i')
#     cell.burst_bacteriophage(None,None)
#     assert cell.__str__() == '12v'
