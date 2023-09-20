import pytest

from models.logic.board import Board

from models.logic.celda import Celda

@pytest.fixture
def board():
    return Board(2, 2)


def test_initial_board(board):
     assert board.rows == 2
     assert board.columns == 2
     assert board.get_celda(0, 0).__eq__(Celda())
     assert board.get_celda(0, 1).__eq__(Celda())
     assert board.get_celda(1, 0).__eq__(Celda())
     assert board.get_celda(1, 1).__eq__(Celda())

def test_initial_spwn(board):
     assert board.rows == 2
     assert board.columns == 2
     board.set_position_spawn_bacterium(0,0)
     board.set_position_spawn_other(1,1) 
     assert board.get_celda(0, 0)._spawn_bacterium().__eq__(True)
     assert board.get_celda(0, 1).__eq__(Celda())
     assert board.get_celda(1, 0).__eq__(Celda())
     assert board.get_celda(1, 1)._spawn_other().__eq__(True)


