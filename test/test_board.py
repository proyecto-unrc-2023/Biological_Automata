import pytest

from models.logic.board import Board

from models.logic.cell import Cell

@pytest.fixture
def board():
    return Board(2, 2)


def test_initial_board(board):
     assert board._rows == 2
     assert board._columns == 2
     assert board.get_cell(0, 0).is_empty()
     assert board.get_cell(0, 1).is_empty()
     assert board.get_cell(1, 0).is_empty()
     assert board.get_cell(1, 1).is_empty()

def test_initial_spwn(board):
     assert board._rows == 2
     assert board._columns == 2
     board.set_position_spawn_bacterium(0,0)
     board.set_position_spawn_other(1,1) 
     assert board.get_cell(0, 0).get_spawn_bacterium() == True
     assert board.get_cell(0, 1).is_empty()
     assert board.get_cell(1, 0).is_empty()
     assert board.get_cell(1, 1).get_spawn_other() == True                                                                                                                                                                                                                                


