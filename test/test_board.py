import pytest

from models.logic.board import Board

from models.logic.Bacterium import * 

from models.logic.cell import Cell

from models.logic.Bacteriophage import Bacteriophage

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
     board.set_position_spawn_bacterium((0,0))
     board.set_position_spawn_other((1,1)) 
     assert board.get_cell(0, 0).get_spawn_bacterium() == True
     assert board.get_cell(0, 1).is_empty()
     assert board.get_cell(1, 0).is_empty()
     assert board.get_cell(1, 1).get_spawn_other() == True   
     assert not(board.is_empty())

def test_set_spawn_bacterium_error(board):
     board.set_position_spawn_bacterium((0,0))
     with pytest.raises(ValueError):
          board.set_position_spawn_other((0,0))
     assert board.get_position_spawn_other()==None

def test_set_spawn_other_error(board):
     assert board._rows == 2
     assert board._columns == 2
     board.set_position_spawn_other((0,0))
     with pytest.raises(ValueError):
          board.set_position_spawn_bacterium((0,0))
     assert board.get_position_spawn_bacterium()==None

def test_eq_board_error(board):
     board_aux = Board(3,2)
     assert not board.__eq__(board_aux)

def test_eq_board_error_2(board):
     board_aux = Board(2,2)
     board_aux.add_antibiotic(1,1)
     assert not board.__eq__(board_aux)

def test_eq_board(board):
     board_aux = Board(2,2)
     assert  board.__eq__(board_aux)
                                                        
def test_add_antibiotic(board):
     board.add_antibiotic(1,1)
     assert board.get_cell(0, 0).is_empty()
     assert board.get_cell(0, 1).is_empty()
     assert board.get_cell(1, 0).is_empty()
     assert board.get_cell(1, 1)._antibiotics == 1 

def test_set_bacteriphages(board):
     bacteriophage = Bacteriophage(4)
     board.set_bacteriophage(1,1, bacteriophage)
     assert board.get_cell(0, 0).is_empty()
     assert board.get_cell(0, 1).is_empty()
     assert board.get_cell(1, 0).is_empty()
     assert board.get_cell(1, 1).cant_bacteriophages() == 1

def test_set_antibiotic(board):
     board.set_antibiotics(1,1,3)
     assert board.get_cell(0, 0).is_empty()
     assert board.get_cell(0, 1).is_empty()
     assert board.get_cell(1, 0).is_empty()
     assert board.get_cell(1, 1)._antibiotics == 3

def test_empty_board_to_string(board):
    res = board.__str__()
    expected = ' | \n'\
               ' | '
    assert expected == res

def test_add_bacteria_Normal_board_to_string(board):
   board.set_bacterium(1,1,BacteriumNormal(0))
   board.set_bacterium(1,1,BacteriumStrong(0))
   res = board.__str__()
   expected = ' | \n'\
              ' |1b1f'
   assert expected == res

def test_add_4_x_4_bacteria_Strong_board_to_string():
   board = Board(4, 4)
   board.set_bacterium(1,1,BacteriumStrong(0))
   res = board.__str__()
   expected = ' | | | \n'\
              ' |1f| | \n'\
              ' | | | \n'\
              ' | | | '
   assert expected == res


def test_add_3_4_x_4_bacteria_Strong_board_to_string():
   board = Board(4, 4)
   board.set_bacterium(1,1,BacteriumStrong(0))
   board.set_bacterium(3,3,BacteriumNormal(0) )
   board.set_bacterium(1,1,BacteriumNormal(0) )
   res = board.__str__()
   expected = ' | | | \n'\
              ' |1b1f| | \n'\
              ' | | | \n'\
              ' | | |1b'
   assert expected == res

def test_4x4_board_to_string():
    board = Board(4, 4)
    res = board.__str__()
    expected = ' | | | \n'\
               ' | | | \n'\
               ' | | | \n'\
               ' | | | '
    assert expected == res
    
def test_4x4_board_from_string():
     board_str=' | | | \n'\
               ' | | | \n'\
               ' | | | \n'\
               ' | | | '
     board = Board.from_string(board_str)
     assert board.__eq__(Board(4,4))

def test_random_move():
    board = Board(3, 3)
    board.set_bacterium(1, 1,BacteriumNormal(0))
    assert board.get_cell(0, 0).is_empty()
    assert board.get_cell(0, 1).is_empty()
    assert board.get_cell(0, 2).is_empty()
    assert board.get_cell(1, 0).is_empty()
    assert board.get_cell(1, 2).is_empty()
    assert board.get_cell(2, 0).is_empty()
    assert board.get_cell(2, 1).is_empty()
    assert board.get_cell(2, 2).is_empty()
    pos = board.get_random_move(1,1)
    assert board.get_random_move(-2,-2) == None
    assert pos == (0,0) or pos == (1,0) or pos == (2,0) or pos == (2,1) or pos == (2,2) or pos == (1,2) or pos == (0,2) or pos == (0,1)