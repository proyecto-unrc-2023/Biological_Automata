import pytest

from models.logic.board import Board

from models.logic.cell import Cell

@pytest.fixture
def cell():
    return Cell()


def test_initial_cell(cell):
    assert cell._antibiotics == 0
    assert cell._cant_bacteria() == 0
    assert cell._cant_bacteriophages() == 0
    assert cell.get_spawn_bacterium() == False
    assert cell.get_spawn_other() == False
    assert cell.is_empty()
    

def test_spawn_bacterium_cell(cell):
    cell.set_spawn_bacterium()
    assert cell._antibiotics == 0
    assert cell._cant_bacteria() == 0
    assert cell._cant_bacteriophages() == 0
    assert cell.get_spawn_bacterium() == True
    assert cell.get_spawn_other() == False

def test_spawn_other_cell(cell):
    cell_aux = Cell()
    cell_aux.set_spawn_other()
    cell.set_spawn_other()
    assert cell._antibiotics == 0
    assert cell._cant_bacteria ()== 0
    assert cell._cant_bacteriophages() == 0
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
