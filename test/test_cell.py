import pytest

from models.logic.cell import *
from models.logic.Bacterium import *
from models.logic.Antibiotic import Antibiotic
from models.logic.Bacteriophage import Bacteriophage

@pytest.fixture
def cell():
    return Cell()

def test_initial_cell(cell):
    assert cell._antibiotics == 0
    assert cell.cant_bacteria() == 0
    assert cell.cant_bacteriophages() == 0
    assert cell.get_spawn_bacterium() == False
    assert cell.get_spawn_other() == False
    assert cell.is_empty()
    
def test_spawn_bacterium_cell(cell):
    cell.set_spawn_bacterium()
    assert cell._antibiotics == 0
    assert cell.cant_bacteria() == 0
    assert cell.cant_bacteriophages() == 0
    assert cell.get_spawn_bacterium() == True
    assert cell.get_spawn_other() == False

def test_spawn_other_cell(cell):
    cell_aux = Cell()
    cell_aux.set_spawn_other()
    cell.set_spawn_other()
    assert cell._antibiotics == 0
    assert cell.cant_bacteria ()== 0
    assert cell.cant_bacteriophages() == 0
    assert cell.get_spawn_bacterium() == False
    assert cell.get_spawn_other() == True

def test_spawn_bacterium_cell_not_empty(cell):
    cell.set_spawn_other()
    with pytest.raises(ValueError):
        cell.set_spawn_bacterium()

def test_spawn_other_cell_not_empty(cell):
    cell.set_spawn_bacterium()
    with pytest.raises(ValueError):
        cell.set_spawn_other()

def test_eq_cell(cell):
    cell_aux = Cell()
    cell_aux.set_spawn_other()
    cell.set_spawn_other()
    assert cell.__eq__(cell_aux)

def test_not_eq_cell(cell):
    cell_aux = Cell()
    cell_aux.set_spawn_other()
    cell.set_spawn_bacterium()
    assert not (cell.__eq__(cell_aux))

def test_add_bacterium(cell):
    cell.add_bacterium(0,'b')
    assert cell.cant_bacteria() == 1
    assert cell._bacteria[0].__str__() == 'b'

def test_add_bacterium_class(cell):
    cell._bacterium = BacteriumNormal(0)
    assert cell.cant_bacteria() == 1
    assert cell._bacteria[0].__str__() == 'b'

def test_add_antibiotics(cell):
    cell.add_antibiotic()
    assert cell._antibiotics == 1

def test_antibiotics(cell):
    cell._antibiotics = 10
    assert cell._antibiotics == 10

def test_add_bacteriophage(cell):
    cell.add_bacteriophage(4)
    assert cell.cant_bacteriophages() == 1
    assert cell._bacteriophages[0].__str__() == 'v'
    assert cell._bacteriophages[0].get_infection == 4

def test_add_bacteriophage_class(cell):
    cell._bacteriophage = Bacteriophage(4)
    assert cell.cant_bacteriophages() == 1
    assert cell._bacteriophages[0].__str__() == 'v'
    assert cell._bacteriophages[0].get_infection == 4


def test_add_entes(cell):
    cell._bacterium = BacteriumNormal(0)
    cell._antibiotics = 5
    cell_aux = Cell()
    cell_aux._bacterium = BacteriumNormal(0)
    cell_aux._antibiotics = 5

    assert cell.__eq__(cell_aux)

def test_add_diferent_bacteriophages(cell):
    cell.add_bacteriophage(4)
    cell_aux = Cell()
    cell_aux.add_bacteriophage(2)
    assert cell.__eq__(cell_aux)

def test_to_string_1(cell):
    cell.add_bacterium(0,'b')
    cell.add_bacterium(0,'f')
    assert cell.cant_ente('b') == 1
    assert cell.cant_ente('f') == 1
    cell.add_bacteriophage(4)
    cell.add_bacteriophage(4)
    # string = cell.__str__()
    assert cell.__str__() == '1b1f2v'

def test_to_string_2(cell):
    cell.add_bacterium(0,'b')
    cell.add_bacterium(0,'f')
    cell.add_bacterium(0,'b')
    assert cell.cant_ente('b') == 2
    assert cell.cant_ente('f') == 1
    cell.add_bacteriophage(4)
    cell.add_bacteriophage(4)
    # string = cell.__str__()
    assert cell.__str__() == '2b1f2v'

def test_from_string():
    cell = Cell.from_string('1b1f2v')
    assert cell.cant_ente('b') == 1
    assert cell.cant_ente('f') == 1
    assert cell.cant_ente('v') == 2
    assert cell.__str__() == '1b1f2v'

def test_overpoblation_strongest(cell):
    cell.add_bacterium(0,'b')
    cell.add_bacterium(0,'b')
    cell.add_bacterium(0,'d')
    cell.add_bacterium(0,'f')
    cell.overpopulation()
    assert cell.__str__() == '1f'

def test_overpoblation_sin_strongest(cell):
    cell.add_bacterium(0,'b')
    cell.add_bacterium(0,'d')
    cell.add_bacterium(0,'d')
    cell.add_bacterium(0,'b')
    cell.overpopulation()
    assert cell.__str__() == '1b'

def test_overpoblation_debiles(cell):
    cell.add_bacterium(0,'d')
    cell.add_bacterium(0,'d')
    cell.add_bacterium(0,'d')
    cell.add_bacterium(0,'d')
    cell.overpopulation()
    assert cell.__str__() == '1d'

def test_low_dose_antibiotic(cell):
    cell.add_bacterium(0, 'b')
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'd')
    cell.add_antibiotic()
    cell.low_dose_antibiotic()
    assert cell.__str__() == '1d'

def test_high_dose_antibiotic(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'b')
    cell.add_antibiotic()
    cell.add_antibiotic()
    cell.add_antibiotic()
    cell.add_antibiotic()
    cell.high_dose_antibiotic()
    assert cell.__str__() == ' '

def test_update_cell_with_3_strongs_and_1_antibiotic(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_antibiotic()
    cell.update_cell()
    assert cell.__str__() == '3d'

def test_update_cell_with_2_strongs_and_3_antibiotic(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_antibiotic()
    cell.add_antibiotic()
    cell.add_antibiotic()
    cell.update_cell()
    assert cell.__str__() == ' '

def test_update_cell_with_1_strongs_1_weak_and_2_antibiotic(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'd')
    cell.add_antibiotic()
    cell.add_antibiotic()
    cell.update_cell()
    assert cell.__str__() == '1d'

def test_update_cell_with_2_strongs_4_normal_and_1_weak(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'b')
    cell.add_bacterium(0, 'b')
    cell.add_bacterium(0, 'b')
    cell.add_bacterium(0, 'b')
    cell.add_bacterium(0, 'd')
    cell.update_cell()
    assert cell.__str__() == '1f'

def test_update_cell_with_1_strongs_4_normal_1_weak_and_2_antibiotic(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'b')
    cell.add_bacterium(0, 'b')
    cell.add_bacterium(0, 'b')
    cell.add_bacterium(0, 'b')
    cell.add_bacterium(0, 'd')
    cell.add_antibiotic()
    cell.add_antibiotic()
    cell.update_cell()
    assert cell.__str__() == ' '

def test_update_cell_with_1_bacterium_ready_to_reproduce(cell):
    cell.add_bacterium(3, 'b')
    cell.update_cell()
    assert cell.cant_bacteria() == 2

def test_update_cell_with_1_bacterium_not_ready_to_reproduce(cell):
    cell.add_bacterium(2, 'b')
    cell.update_cell()
    assert cell.__str__() == '1b'

def test_update_cell_with_1_weak_ready_to_recover(cell):
    cell.add_bacterium(6, 'd')
    cell.update_cell()
    assert cell.__str__() == '1f'

def test_update_cell_with_1_weak_not_ready_to_recover(cell):
    cell.add_bacterium(3, 'd')
    cell.update_cell()
    assert cell.__str__() == '1d'

def test_update_cell_with_2_weak_ready_to_recover_and_1_weak_not_ready(cell):
    cell.add_bacterium(6, 'd')
    cell.add_bacterium(6, 'd')
    cell.add_bacterium(3, 'd')
    cell.update_cell()
    assert cell.__str__() == '2f1d'

def test_update_cell_with_4_weak_ready_to_recover_and_1_weak_not_ready(cell):
    cell.add_bacterium(6, 'd')
    cell.add_bacterium(6, 'd')
    cell.add_bacterium(6, 'd')
    cell.add_bacterium(6, 'd')
    cell.add_bacterium(3, 'd')
    cell.update_cell()
    assert cell.__str__() == '1f'

def test_update_cell_with_4_bacterium_normal_ready_to_reproduce(cell):
    cell.add_bacterium(3, 'b')
    cell.add_bacterium(3, 'b')
    cell.add_bacterium(3, 'b')
    cell.add_bacterium(3, 'b')
    cell.update_cell()
    assert cell.__str__() == '2b'

def test_update_cell_with_4_bacterium_strong_amd_2_antibiotics(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_antibiotic()
    cell.add_antibiotic()
    cell.update_cell()
    assert cell.__str__() == ' '