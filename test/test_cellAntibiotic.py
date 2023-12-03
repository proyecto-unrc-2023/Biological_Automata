import pytest
from models.logic.CellAntibiotic import CellAntibiotic
from models.logic.Bacterium import *
from models.logic.Antibiotic import Antibiotic


@pytest.fixture
def cellAntibiotic():
    return CellAntibiotic()

@pytest.fixture
def moves_for_reproduction():
    bacterium = Bacterium(0)
    moves_for_reproduction = bacterium.moves_for_reproduction

    return moves_for_reproduction

@pytest.fixture
def moves_for_recovery():
    bacterium = Bacterium(0)
    moves_for_recovery = bacterium.moves_for_recovery

    return moves_for_recovery

@pytest.fixture
def cant_overpopulation():
    return 4

def test_initial_cell_antibiotic(cellAntibiotic):
    assert cellAntibiotic.get_cant_antibiotic() == 0
    assert cellAntibiotic.get_cant_bacteria() == 0
    assert not cellAntibiotic.get_spawn()
    assert cellAntibiotic.is_empty()
    assert str(cellAntibiotic) == ' '


def test_spawn_cell_antibiotic(cellAntibiotic):
    cellAntibiotic.set_spawn()
    assert cellAntibiotic.get_cant_antibiotic() == 0
    assert cellAntibiotic.get_cant_bacteria() == 0
    assert cellAntibiotic.get_spawn()


def test_add_antibiotics(cellAntibiotic):
    cellAntibiotic.add_antibiotic(Antibiotic())
    assert cellAntibiotic.get_cant_antibiotic() == 1
    # assert cellAntibiotic.get_antibiotics()[str(0]) == 'a'


def test_antibiotics(cellAntibiotic):
    for _ in range(10):
        cellAntibiotic.add_antibiotic(Antibiotic())
    assert cellAntibiotic.get_cant_antibiotic() == 10


# def test_not_eq_cell_antibiotic(cellAntibiotic):
#    cell_aux = CellAntibiotic()
#    cellAntibiotic.add_antibiotic(Antibiotic())
#    assert not cellAntibiotic.__eq__(cell_aux)


def test_add_antibiotic_and_bacterium_eq(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cell_aux = CellAntibiotic()
    cell_aux.add_bacterium(BacteriumNormal(0))
    for _ in range(5):
        cellAntibiotic.add_antibiotic(Antibiotic())
        cell_aux.add_antibiotic(Antibiotic())
    assert cellAntibiotic.__eq__(cell_aux)


def test_update_cell_with_3_strongs(cellAntibiotic, cant_overpopulation):
    for _ in range (cant_overpopulation-1):
        cellAntibiotic.add_bacterium(BacteriumStrong(0))

    cellAntibiotic.update_cell(None, None, cant_overpopulation)
    n = str(cant_overpopulation-1)
    assert str(cellAntibiotic) == f'{n}f'


def test_to_string_cell_antibiotic_and_bacterium(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumInfected(0))
    cellAntibiotic.add_bacterium(BacteriumWeak(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    assert str(cellAntibiotic) == '1b1f1d1i1a'


def test_low_dose_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumWeak(0))
    cellAntibiotic.add_antibiotic(Antibiotic(3))
    cellAntibiotic.low_dose(None, None)
    assert str(cellAntibiotic) == '1d1a'


def test_high_dose_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_antibiotic(Antibiotic(3))
    cellAntibiotic.add_antibiotic(Antibiotic(2))
    cellAntibiotic.add_antibiotic(Antibiotic(3))
    cellAntibiotic.add_antibiotic(Antibiotic(2))
    cellAntibiotic.high_dose(None,None)
    assert str(cellAntibiotic) == '4a'


def test_update_cell_with_3_strongs_and_1_antibiotic(cellAntibiotic, cant_overpopulation):
    for _ in range (cant_overpopulation-1):
        cellAntibiotic.add_bacterium(BacteriumStrong(0))

    cellAntibiotic.add_antibiotic(Antibiotic(2))
    cellAntibiotic.update_cell(None, None, cant_overpopulation)

    n = str(cant_overpopulation-1)
    assert str(cellAntibiotic) == f'{n}d1a'


def test_update_cell_with_2_strongs_and_3_antibiotic(cellAntibiotic, cant_overpopulation):
    for _ in range(cant_overpopulation-1):
        cellAntibiotic.add_bacterium(BacteriumStrong(0))

    for _ in range (cant_overpopulation):
        cellAntibiotic.add_antibiotic(Antibiotic(3))

    cellAntibiotic.update_cell(None, None, cant_overpopulation)
    n = str(cant_overpopulation)
    assert str(cellAntibiotic) == f'{n}a'


def test_update_cell_with_1_strongs_1_weak_and_2_antibiotic(cellAntibiotic, cant_overpopulation):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumWeak(0))
    cellAntibiotic.add_antibiotic(Antibiotic(3))
    cellAntibiotic.add_antibiotic(Antibiotic(3))
    cellAntibiotic.update_cell(None, None, cant_overpopulation)
    assert str(cellAntibiotic) == '1d2a'


#def test_update_cell_with_2_strongs_4_normal_and_1_weak(cellAntibiotic):
#    cellAntibiotic.add_bacterium(BacteriumStrong(0))
#    cellAntibiotic.add_bacterium(BacteriumStrong(0))
#    cellAntibiotic.add_bacterium(BacteriumNormal(0))
#    cellAntibiotic.add_bacterium(BacteriumNormal(0))
#    cellAntibiotic.add_bacterium(BacteriumNormal(0))
#    cellAntibiotic.add_bacterium(BacteriumNormal(0))
#    cellAntibiotic.add_bacterium(BacteriumWeak(0))
#    cellAntibiotic.update_cell(None, None, CANT_OVERPOPULATION)
#    assert cellAntibiotic.get_cant_bacteria() == 1


def test_update_cell_with_overpopulation_and_2_antibiotics(cellAntibiotic, cant_overpopulation):
    for _ in range(cant_overpopulation): 
        cellAntibiotic.add_bacterium(BacteriumStrong(0))
        cellAntibiotic.add_bacterium(BacteriumNormal(0))
        cellAntibiotic.add_bacterium(BacteriumWeak(0))

    cellAntibiotic.add_antibiotic(Antibiotic(4))
    cellAntibiotic.add_antibiotic(Antibiotic(4))
    cellAntibiotic.update_cell(None, None, cant_overpopulation)
    assert str(cellAntibiotic) == '2a'


def test_update_cell_with_overpopulation_of_strongs_and_2_antibiotics(cellAntibiotic, cant_overpopulation):
    for _ in range (cant_overpopulation):
        cellAntibiotic.add_bacterium(BacteriumStrong(0))

    cellAntibiotic.add_antibiotic(Antibiotic(2))
    cellAntibiotic.add_antibiotic(Antibiotic(2))
    cellAntibiotic.update_cell(None, None, cant_overpopulation)
    assert str(cellAntibiotic) == '2a'


def test_update_cell_with_1_weak_ready_to_recover(cellAntibiotic, moves_for_recovery):
    cellAntibiotic.add_bacterium(BacteriumWeak(moves_for_recovery))
    cellAntibiotic.update_for_recovery(None, None)
    assert str(cellAntibiotic) == '1f'


def test_update_cell_with_1_weak_not_ready_to_recover(cellAntibiotic, moves_for_recovery):
    cellAntibiotic.add_bacterium(BacteriumWeak(moves_for_recovery-1))
    cellAntibiotic.update_for_recovery(None, None)
    assert str(cellAntibiotic) == '1d'


def test_update_cell_with_2_weak_ready_to_recover_and_1_weak_not_ready(cellAntibiotic, moves_for_recovery):
    cellAntibiotic.add_bacterium(BacteriumWeak(moves_for_recovery))
    cellAntibiotic.add_bacterium(BacteriumWeak(moves_for_recovery))
    cellAntibiotic.add_bacterium(BacteriumWeak(moves_for_recovery-1))
    cellAntibiotic.update_for_recovery(None, None)
    assert str(cellAntibiotic) == '2f1d'


def test_update_cell_with_overpopulation_of_weak_ready_to_recover(cellAntibiotic, moves_for_recovery, cant_overpopulation):
    for _ in range(cant_overpopulation):
        cellAntibiotic.add_bacterium(BacteriumWeak(moves_for_recovery))

    cellAntibiotic.update_cell(None, None, cant_overpopulation)
    assert str(cellAntibiotic) == '1f'



