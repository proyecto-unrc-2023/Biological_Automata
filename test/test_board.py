import pytest

from models.logic.board import Board

from models.logic.Bacterium import *

from models.logic.cell import Cell

from models.logic.Bacteriophage import Bacteriophage
from models.logic.Antibiotic import Antibiotic

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
     assert board._board.__eq__(board_aux._board)
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

def test_4x4_board_from_string_row_empty_error():
     board_str = ''
     with pytest.raises(ValueError):
          Board.from_string(board_str)

def test_4x4_board_from_string_colum_empty_error():
     board_str = '\n'\
                 ''
     with pytest.raises(ValueError):
          Board.from_string(board_str)

def test_4x4_board_from_string_error_cant_colum():
     board_str = ' | \n'\
                 ''
     with pytest.raises(ValueError):
          Board.from_string(board_str)

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

def test_move_entities_none():
    board = Board(3, 3)
    board.set_bacterium(1, 1,BacteriumNormal(0))
    board.set_bacteriophage(1,1, Bacteriophage(4))
    board.add_antibiotic(1,1)
    new_board = board
    new_board = board.move_entities(-2,-2, new_board)
    assert board.__eq__(new_board)
def test_update_board():
    board =Board(3,3)
    board.get_cell(2, 2).add_antibiotic()
    board.set_position_spawn_bacterium((0,0))
    board.set_position_spawn_other((2,1))
    assert board.get_cell(0, 0).get_spawn_bacterium() == True
    assert board.get_cell(2, 1).get_spawn_other() == True
    assert board.get_cell(0, 1).is_empty()
    assert board.get_cell(0, 2).is_empty()
    assert board.get_cell(1, 1).is_empty()
    assert board.get_cell(1, 2).is_empty()
    assert board.get_cell(2, 0).is_empty()
    actualizado = board.move_all_entities()
    actualizado.crossing_board()
    res = actualizado.__str__()

    expected1 = 'sb| | \n'\
                ' | |1a\n'\
                ' |so| '

    expected2 = 'sb| | \n'\
                ' |1a| \n'\
                ' |so| '

    assert  res == expected1 or res == expected2

def test_update_board_1():
    board =Board(3,3)
    board.get_cell(2, 2).add_bacteriophage(4)
    board.set_position_spawn_bacterium((0,0))
    board.set_position_spawn_other((2,1))
    assert board.get_cell(0, 0).get_spawn_bacterium() == True
    assert board.get_cell(2, 1).get_spawn_other() == True
    assert board.get_cell(0, 1).is_empty()
    assert board.get_cell(0, 2).is_empty()
    assert board.get_cell(1, 1).is_empty()
    assert board.get_cell(1, 2).is_empty()
    assert board.get_cell(2, 0).is_empty()
    actualizado = board.move_all_entities()
    actualizado.crossing_board()
    res = actualizado.__str__()
        
    expected1 = 'sb| | \n'\
                ' | |1v\n'\
                ' |so| '
    
    expected2 = 'sb| | \n'\
                ' |1v| \n'\
                ' |so| '

    assert  res == expected1 or res == expected2 


def test_update_board_2():
    board =Board(3,3)
    board.set_bacterium(0,1,BacteriumStrong(0))
    board.set_position_spawn_bacterium((0,0))
    board.set_position_spawn_other((2,1))
    assert board.get_cell(0, 0).get_spawn_bacterium() == True
    assert board.get_cell(2, 1).get_spawn_other() == True
    assert board.get_cell(1, 1).is_empty()
    assert board.get_cell(0, 2).is_empty()
    assert board.get_cell(1, 1).is_empty()
    assert board.get_cell(1, 2).is_empty()
    assert board.get_cell(2, 0).is_empty()
    actualizado = board.move_all_entities()
    actualizado.crossing_board()
    res = actualizado.__str__()

    expected1 = 'sb| |1f\n'\
                ' | | \n'\
                ' |so| '

    expected2 = 'sb| | \n'\
                ' |1f| \n'\
                ' |so| '

    expected3 = 'sb| | \n'\
                ' | |1f\n'\
                ' |so| '

    expected4 = 'sb| | \n'\
                '1f| | \n'\
                ' |so| '
    assert  res == expected1 or res == expected2 or res == expected3 or res == expected4


def test_update_board_2_con_cruzamiento():
    board =Board(3,3)
    board.set_bacterium(0,1,BacteriumNormal(0))
    board.get_cell(2, 2).add_antibiotic()
    board.set_position_spawn_bacterium((0,0))
    board.set_position_spawn_other((2,1))
    assert board.get_cell(0, 0).get_spawn_bacterium() == True
    assert board.get_cell(2, 1).get_spawn_other() == True
    assert board.get_cell(1, 1).is_empty()
    assert board.get_cell(0, 2).is_empty()
    assert board.get_cell(1, 1).is_empty()
    assert board.get_cell(1, 2).is_empty()
    assert board.get_cell(2, 0).is_empty()
    actualizado = board.move_all_entities()
    actualizado.crossing_board()
    res = actualizado.__str__()
        
    expected1 = 'sb| |1b\n'\
                ' | |1a\n'\
                ' |so| '
    
    expected2 = 'sb| |1b\n'\
                ' |1a| \n'\
                ' |so| '

    expected3 = 'sb| |  \n'\
                ' | | \n'\
                ' |so| '
    
    expected4 = 'sb| | \n'\
                ' |1a|1b\n'\
                ' |so| '
    
    expected5 = 'sb| | \n'\
                ' |1b|1a\n'\
                ' |so| '
    
    expected6 = 'sb| | \n'\
                '1b| |1a\n'\
                ' |so| '
    
    expected7 = 'sb| | \n'\
                '1b|1a| \n'\
                ' |so| '

    assert  res == expected1 or res == expected2 or res == expected3 or res == expected4 or res == expected5 or res == expected6 or res == expected7 

def test_4_x_4_move_entity_bacterium():
   board = Board(4, 4)
   bacteria = BacteriumStrong(0)
   board.set_bacterium(1,2, bacteria)
   board = board.move_entity(1,1,1,2,board,bacteria)
   res = board.__str__()
   expected = ' | | | \n'\
              ' |1f| | \n'\
              ' | | | \n'\
              ' | | | '
   assert expected == res

def test_4_x_4_move_entity_bacteriphage():
   board = Board(4, 4)
   bacteriophage = Bacteriophage(4)
   board.set_bacteriophage(1,2, bacteriophage)
   board = board.move_entity(1,1,1,2,board,bacteriophage)
   res = board.__str__()
   expected = ' | | | \n'\
              ' |1v| | \n'\
              ' | | | \n'\
              ' | | | '
   assert expected == res

def test_4_x_4_move_entity_antibiotic():
   board = Board(4, 4)
   board.add_antibiotic(1,2)
   board.add_antibiotic(1,1)
   board = board.move_entity(1,1,1,2,board,Antibiotic())
   res = board.__str__()
   expected = ' | | | \n'\
              ' |2a| | \n'\
              ' | | | \n'\
              ' | | | '
   assert expected == res


def test_update_board_2_con_burst_bacteriophage():
    board =Board(3,3)
    board.set_bacterium(2,2,BacteriumInfected(3))
    board.set_position_spawn_bacterium((0,0))
    board.set_position_spawn_other((2,1))
    assert board.get_cell(0, 0).get_spawn_bacterium() == True
    assert board.get_cell(2, 1).get_spawn_other() == True
    actualizado = board.move_all_entities()
    actualizado.crossing_board()
    res = actualizado.__str__()

    expected1 = 'sb| | \n'\
                ' | |4v\n'\
                ' |so| '
    
    expected2 = 'sb| | \n'\
                ' |4v| \n'\
                ' |so| '

    assert res == expected1 or res == expected2
  
def test_4_x_4_move_entity_bacterium():
   board = Board(4, 4)
   bacteria = BacteriumStrong(0)
   board.set_bacterium(1,2, bacteria)
   board = board.move_entity(1,1,1,2,board,bacteria)
   res = board.__str__()
   expected = ' | | | \n'\
              ' |1f| | \n'\
              ' | | | \n'\
              ' | | | '
   assert expected == res

def test_4_x_4_move_entity_bacteriphage():
   board = Board(4, 4)
   bacteriophage = Bacteriophage(4)
   board.set_bacteriophage(1,2, bacteriophage)
   board = board.move_entity(1,1,1,2,board,bacteriophage)
   res = board.__str__()
   expected = ' | | | \n'\
              ' |1v| | \n'\
              ' | | | \n'\
              ' | | | '
   assert expected == res

def test_4_x_4_move_entity_antibiotic():
   board = Board(4, 4)
   board.add_antibiotic(1,2)
   board.add_antibiotic(1,1)
   board = board.move_entity(1,1,1,2,board,Antibiotic())
   res = board.__str__()
   expected = ' | | | \n'\
              ' |2a| | \n'\
              ' | | | \n'\
              ' | | | '
   assert expected == res
