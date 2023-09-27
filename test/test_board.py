import pytest

from models.logic.board import Board

from models.logic.Bacterium import * 

from models.logic.cell import Cell


@pytest.fixture
def board():
    return Board(2, 2)

def test_initial_board(board):
     assert board._rows == 2
     assert board._columns == 2
     assert board.get_position_spawn_bacterium() == None
     assert board.get_position_spawn_other() == None
     assert board.get_cell(0, 0).is_empty()
     assert board.get_cell(0, 1).is_empty()
     assert board.get_cell(1, 0).is_empty()
     assert board.get_cell(1, 1).is_empty()
     assert board.is_empty()

def test_board_set_spwn(board):
     assert board._rows == 2
     assert board._columns == 2
     board.set_position_spawn_bacterium(0,0)
     board.set_position_spawn_other(1,1) 
     assert board.get_cell(0, 0).get_spawn_bacterium() == True
     assert board.get_cell(0, 1).is_empty()
     assert board.get_cell(1, 0).is_empty()
     assert board.get_cell(1, 1).get_spawn_other() == True   
     assert not(board.is_empty())

def test_set_spawn_bacterium_error(board):
     assert board._rows == 2
     assert board._columns == 2
     board.set_position_spawn_bacterium(0,0)
     with pytest.raises(ValueError):
          board.set_position_spawn_other(0,0)
     assert board.get_position_spawn_other()==None

def test_set_spawn_other_error(board):
     assert board._rows == 2
     assert board._columns == 2
     board.set_position_spawn_other(0,0)
     with pytest.raises(ValueError):
          board.set_position_spawn_bacterium(0,0)
     assert board.get_position_spawn_bacterium()==None
                                                      
def test_add_antibiotico(board):
     assert board._rows == 2
     assert board._columns == 2
     board.add_antibiotico(1,1,1)
     assert board.get_cell(0, 0).is_empty()
     assert board.get_cell(0, 1).is_empty()
     assert board.get_cell(1, 0).is_empty()
     assert board.get_cell(1, 1)._antibiotics == 1 

def test_empty_board_to_string(board):
    res = board.__str__()
    expected = ' | \n'\
               ' | '
    assert expected == res

def test_add_bacteria_Normal_board_to_string(board):
   bacte = BacteriumNormal(0)
   bacte1 = BacteriumStrong(0)
   board.add_bacteria(1,1,bacte)
   board.add_bacteria(1,1,bacte1)
   res = board.__str__()
   expected = ' | \n'\
              ' |fb '
   assert expected == res

def test_add_4_x_4_bacteria_Strong_board_to_string():
   board = Board(4, 4)
   bacte = BacteriumStrong(0)
   board.add_bacteria(1,1,bacte)
   res = board.__str__()
   expected = ' | | | \n'\
              ' |f | | \n'\
              ' | | | \n'\
              ' | | | '
   assert expected == res


def test_add_3_4_x_4_bacteria_Strong_board_to_string():
   board = Board(4, 4)
   bacte = BacteriumStrong(0)
   bacte2 = BacteriumNormal(0) 
   bacte1 = BacteriumNormal(0) 
   board.add_bacteria(1,1,bacte)
   board.add_bacteria(3,3,bacte1)
   board.add_bacteria(1,1,bacte2)
   res = board.__str__()
   expected = ' | | | \n'\
              ' |bf | | \n'\
              ' | | | \n'\
              ' | | |b '
   assert expected == res



def test_4x4_board_to_string():
    board = Board(4, 4)
    res = board.__str__()
    expected = ' | | | \n'\
               ' | | | \n'\
               ' | | | \n'\
               ' | | | '
    assert expected == res
