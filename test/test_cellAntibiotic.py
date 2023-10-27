import pytest
from models.logic.cell import *
from models.logic.CellAntibiotic import *
from models.logic.Bacterium import *
from models.logic.Antibiotic import Antibiotic

@pytest.fixture
def cellAntibiotic():
    return CellAntibiotic()

def test_initial_cell_antibiotic(cellAntibiotic):
    assert cellAntibiotic.get_cant_antibiotic() == 0
    assert cellAntibiotic.get_cant_bacteria() ==0
    assert not cellAntibiotic.get_spawn()
    assert cellAntibiotic.is_empty()
    assert cellAntibiotic.__str__() == ' '


def test_spawn_cell_antibiotic(cellAntibiotic):
    cellAntibiotic.set_spawn()
    assert cellAntibiotic.get_cant_antibiotic() == 0
    assert cellAntibiotic.get_cant_bacteria() == 0
    assert cellAntibiotic.get_spawn()


def test_add_antibiotics(cellAntibiotic):
    cellAntibiotic.add_antibiotic(Antibiotic())
    assert cellAntibiotic.get_cant_antibiotic() == 1
   # assert cellAntibiotic.get_antibiotics()[0].__str__() == 'a'


def test_antibiotics(cellAntibiotic):
    for _ in range(10):
        cellAntibiotic.add_antibiotic(Antibiotic())
    assert cellAntibiotic.get_cant_antibiotic() == 10


#def test_not_eq_cell_antibiotic(cellAntibiotic):
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


def test_update_cell_with_3_strongs(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.update_cell(None, None)
    assert cellAntibiotic.__str__() == '3f'

def test_to_string_cell_antibiotic_and_bacterium(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumInfected(0))
    cellAntibiotic.add_bacterium(BacteriumWeak(0))
    cellAntibiotic.add_antibiotic(Antibiotic())  
    assert cellAntibiotic.__str__() == '1b1f1d1i1a'


def test_low_dose_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumWeak(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.low_dose(None, None)
    assert cellAntibiotic.__str__()== '1d'

def test_high_dose_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.high_dose()
    assert cellAntibiotic.__str__() == ' '

def test_update_cell_with_3_strongs_and_1_antibiotic(cell):
    cell.add_bacterium(BacteriumStrong(0))
    cell.add_bacterium(BacteriumStrong(0))
    cell.add_bacterium(BacteriumStrong(0))
    cell.add_antibiotic(Antibiotic())
    cell.update_cell(None,None)
    assert cell.__str__() == '3d'

def test_update_cell_with_2_strongs_and_3_antibiotic(cell):
    cell.add_bacterium(BacteriumStrong(0))
    cell.add_bacterium(BacteriumStrong(0))
    cell.add_antibiotic(Antibiotic())
    cell.add_antibiotic(Antibiotic())
    cell.add_antibiotic(Antibiotic())
    cell.update_cell(None,None)
    assert cell.__str__() == ' '


def test_update_cell_with_3_strongs_and_1_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.update_cell(None, None)
    assert cellAntibiotic.__str__() == '3d'
    

def test_update_cell_with_2_strongs_and_3_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.update_cell(None, None)
    assert cellAntibiotic.__str__() == ' '


def test_update_cell_with_1_strongs_1_weak_and_2_antibiotic(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumWeak(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.update_cell(None, None)
    assert cellAntibiotic.__str__() == '1d'

def test_update_cell_with_2_strongs_4_normal_and_1_weak(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumNormal(0))
    cellAntibiotic.add_bacterium(BacteriumWeak(0))
    cellAntibiotic.update_cell(None, None)
    assert cellAntibiotic.__str__() == '1f'

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
    assert cellAntibiotic.__str__() == ' '


def test_update_cell_with_4_bacterium_strong_amd_2_antibiotics(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_bacterium(BacteriumStrong(0))
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.add_antibiotic(Antibiotic())
    cellAntibiotic.update_cell(None,None)
    assert cellAntibiotic.__str__() == ' '

def test_update_cell_with_1_weak_ready_to_recover(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumWeak(6))
    cellAntibiotic.update_for_recovery(None,None)
    assert cellAntibiotic.__str__() == '1f'


def test_update_cell_with_1_weak_not_ready_to_recover(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumWeak(3))
    cellAntibiotic.update_for_recovery(None,None)
    assert cellAntibiotic.__str__() == '1d'

def test_update_cell_with_2_weak_ready_to_recover_and_1_weak_not_ready(cellAntibiotic):
   cellAntibiotic.add_bacterium(BacteriumWeak(6))
   cellAntibiotic.add_bacterium(BacteriumWeak(6))
   cellAntibiotic.add_bacterium(BacteriumWeak(3))
   cellAntibiotic.update_for_recovery(None,None)
   assert cellAntibiotic.__str__() == '2f1d'

  
def test_update_cell_with_4_weak_ready_to_recover_and_1_weak_not_ready(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumWeak(6))
    cellAntibiotic.add_bacterium(BacteriumWeak(6))
    cellAntibiotic.add_bacterium(BacteriumWeak(6))
    cellAntibiotic.add_bacterium(BacteriumWeak(6))
    cellAntibiotic.add_bacterium(BacteriumWeak(3))
    cellAntibiotic.update_cell(None,None)
    assert cellAntibiotic.__str__() == '1f'


def test_update_cell_with_2_weak_ready_to_recover_and_1_weak_not_ready(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumWeak(6))
    cellAntibiotic.add_bacterium(BacteriumWeak(6))
    cellAntibiotic.add_bacterium(BacteriumWeak(3))
    cellAntibiotic.update_for_recovery(None,None)
    assert cellAntibiotic.__str__() == '2f1d'

def test_update_cell_with_4_weak_ready_to_recover_and_1_weak_not_ready(cellAntibiotic):
    cellAntibiotic.add_bacterium(BacteriumWeak(6))
    cellAntibiotic.add_bacterium(BacteriumWeak(6))
    cellAntibiotic.add_bacterium(BacteriumWeak(6))
    cellAntibiotic.add_bacterium(BacteriumWeak(6))
    cellAntibiotic.add_bacterium(BacteriumWeak(3))
    cellAntibiotic.update_cell(None,None)
    assert cellAntibiotic.__str__() == '1f'

