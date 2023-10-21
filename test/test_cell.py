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
    assert cell.is_spawn_bacterium() == False
    assert cell.get_spawn_other() == False
    assert cell.is_spawn_other() == False
    assert cell.is_empty()

def test_spawn_bacterium_cell(cell):
    cell.set_spawn_bacterium()
    assert cell._antibiotics == 0
    assert cell.cant_bacteria() == 0
    assert cell.cant_bacteriophages() == 0
    assert cell.get_spawn_bacterium() == True
    assert cell.get_spawn_other() == False

def test_spawn_other_cell(cell):
    cell.set_spawn_other()
    assert cell._antibiotics == 0
    assert cell.cant_bacteria ()== 0
    assert cell.cant_bacteriophages() == 0
    assert cell.get_spawn_bacterium() == False
    assert cell.get_spawn_other() == True

def test_spawn_bacterium_cell_not_empty(cell):
    cell.set_spawn_other()
    with pytest.raises(ValueError) as e:
        cell.set_spawn_bacterium()
    assert str(e.value) == 'celda ocupada'

def test_spawn_other_cell_not_empty(cell):
    cell.set_spawn_bacterium()
    with pytest.raises(ValueError) as e:
        cell.set_spawn_other()
    assert str(e.value) == 'celda ocupada'
    
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

def test_not_eq_cell_bacterium(cell):
    cell_aux = Cell()
    cell_aux.add_bacterium(1,'b')
    cell.add_bacterium(1,'f')
    assert not (cell.__eq__(cell_aux))

def test_not_eq_cell_bacteriophage(cell):
    cell_aux = Cell()
    cell.add_bacteriophage(4)
    cell_aux.add_bacteriophage(3)
    assert not(cell.__eq__(cell_aux))

def test_add_bacterium(cell):
    cell.add_bacterium(0,'b')
    assert cell.cant_bacteria() == 1
    assert cell._bacteria[0].__str__() == 'b'

def test_add_bacterium_class(cell):
    cell._bacterium = BacteriumNormal(0)
    assert cell.cant_bacteria() == 1
    assert cell._bacteria[0].__str__() == 'b'

def test_add_antibiotics(cell):
    cell.add_antibiotic(Antibiotic())
    assert cell._antibiotics == 1

def test_antibiotics(cell):
    cell._antibiotics = 10
    assert cell._antibiotics == 10

def test_add_bacteriophage(cell):
    cell.add_bacteriophage(4)
    assert cell.cant_bacteriophages() == 1
    assert cell.__str__() == '1v'
    assert cell._bacteriophages[0].infection == 4


def test_add_entes_and_eq_cells(cell):
    cell._bacterium = BacteriumNormal(0)
    cell._antibiotics = 5
    cell_aux = Cell()
    cell_aux._bacterium = BacteriumNormal(0)
    cell_aux._antibiotics = 5
    assert cell.__eq__(cell_aux)

def test_add_move(cell):
      cell._bacterium = BacteriumNormal(0)
      cell.add_bacteriophage(4)
      cell.add_move()
      assert cell._bacteria[0].moves == 1
      assert cell._bacteriophages[0].infection == 3

def test_to_string_1(cell):
    cell.add_bacterium(0,'b')
    cell.add_bacterium(0,'f')
    cell.add_bacterium(0,'i')
    cell.add_bacterium(0,'d')
    assert cell.cant_ente('b') == 1
    assert cell.cant_ente('f') == 1
    cell.add_antibiotic(Antibiotic())
    cell.add_bacteriophage(4)
    cell.add_bacteriophage(4)
    assert cell.__str__() == '1a1b1f1d1i2v'

def test_to_string_2(cell):
    cell.add_bacterium(0,'b')
    cell.add_bacterium(0,'f')
    cell.add_bacterium(0,'b')
    assert cell.cant_ente('b') == 2
    assert cell.cant_ente('f') == 1
    cell.add_bacteriophage(4)
    cell.add_bacteriophage(4)
    assert cell.__str__() == '2b1f2v'

def test_from_string():
    cell = Cell.from_string('1a1b1f1d1i2v')
    assert cell.cant_ente('a') == 1
    assert cell.cant_ente('b') == 1
    assert cell.cant_ente('f') == 1
    assert cell.cant_ente('d') == 1
    assert cell.cant_ente('i') == 1
    assert cell.cant_ente('v') == 2
    assert cell.__str__() == '1a1b1f1d1i2v'

def test_from_string_empty():
    cell = Cell.from_string(' ')
    assert cell.__str__() == ' '

def test_from_string_spwn_bacterium():
    cell = Cell.from_string('sb')
    assert cell.__str__() == 'sb'

def test_from_string_spwn_other():
    cell = Cell.from_string('so')
    assert cell.__str__() == 'so'

def test_from_string_error():
    with pytest.raises(ValueError) as e:
        cell = Cell.from_string('sO1b')
    assert str(e.value) == 'string invalido'

def test_overpoblation_strongest(cell):
    cell.add_bacterium(0,'b')
    cell.add_bacterium(0,'b')
    cell.add_bacterium(0,'d')
    cell.add_bacterium(0,'f')
    cell.overpopulation()
    assert cell.__str__() == '1f'

def test_overpoblation_without_strongest(cell):
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
    cell.add_antibiotic(Antibiotic())
    cell.low_dose_antibiotic()
    assert cell.__str__() == '1d'

def test_high_dose_antibiotic(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'b')
    cell.add_antibiotic(Antibiotic())
    cell.add_antibiotic(Antibiotic())
    cell.add_antibiotic(Antibiotic())
    cell.add_antibiotic(Antibiotic())
    cell.high_dose_antibiotic()
    assert cell.__str__() == ' '

def test_update_cell_with_3_strongs_and_1_antibiotic(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_antibiotic(Antibiotic())
    cell.update_cell()
    assert cell.__str__() == '3d'

def test_update_cell_with_2_strongs_and_3_antibiotic(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_antibiotic(Antibiotic())
    cell.add_antibiotic(Antibiotic())
    cell.add_antibiotic(Antibiotic())
    cell.update_cell()
    assert cell.__str__() == ' '

def test_update_cell_with_1_strongs_1_weak_and_2_antibiotic(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'd')
    cell.add_antibiotic(Antibiotic())
    cell.add_antibiotic(Antibiotic())
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
    cell.add_antibiotic(Antibiotic())
    cell.add_antibiotic(Antibiotic())
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
    assert cell.cant_bacteria() == 2

def test_update_cell_with_4_bacterium_strong_amd_2_antibiotics(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_antibiotic(Antibiotic())
    cell.add_antibiotic(Antibiotic())
    cell.update_cell()
    assert cell.__str__() == ' '

def test_add_move_to_bacteriums(cell):
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')
    cell.add_bacterium(0, 'f')

def test_burst_bacteriophage(cell):
    cell.add_bacterium(4,'i') 
    cell.burst_bacteriophage()
    assert cell.__str__() == '4v'

def test_3_burst_bacteriophage(cell):
    cell.add_bacterium(4,'i')
    cell.add_bacterium(4,'i')
    cell.add_bacterium(4,'i')   
    cell.burst_bacteriophage()
    assert cell.__str__() == '12v'