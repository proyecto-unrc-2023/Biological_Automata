import pytest
from models.logic.GameController import GameController, Game_Mode
from models.logic.Bacterium import *

@pytest.fixture
def game():
    return GameController()

def test_initial_game(game):
  assert game._board._columns == 0
  assert game._board._rows == 0
  assert game.get_mode() == Game_Mode.NOT_STARTER

def test_modify_mode(game):
  game.set_mode(Game_Mode.ANTIBIOTIC)
  assert game.get_mode() == Game_Mode.ANTIBIOTIC

def test_config_(game):
  game.config(6,6)
  assert game._board._columns == 6
  assert game._board._rows == 6
  assert game.get_mode() == Game_Mode.CONFIG_GAME

def test_set_spawn_bacterium(game):
  game.config(6,6)
  game.set_mode(Game_Mode.ANTIBIOTIC)
  assert game.get_mode() == Game_Mode.ANTIBIOTIC
  pos = (2,2)
  game.set_spawn_bacterium(pos)
  position = game._board.get_position_spawn_bacterium()
  if position != None:
    assert position[0] == 2
    assert position[1] == 2


def test_set_spawn_other(game):
  game.config(6,6)
  pos = (2,2)
  game.set_spawn_other(pos)
  position = game._board.get_position_spawn_other()
  if position != None:
    assert position[0] == 2
    assert position[1] == 2

def test_spawn_bacterium(game):
  game.config(6,6)
  pos = (2,2)
  game.set_spawn_bacterium(pos)
  game.generate_bacterium()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  bacteria_found = any(len(game._board.get_cell(x, y)._bacteria) > 0 for x, y in moves_n)
  assert bacteria_found

def test_spawn_other_antibiotic(game):
  game.config(6,6)
  pos = (2,2)
  game.set_mode(Game_Mode.ANTIBIOTIC)
  game.set_spawn_other(pos)
  game.generate_other()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  bacteria_found = any(game._board.get_cell(x, y)._antibiotics > 0 for x, y in moves_n)
  assert bacteria_found


def test_spawn_bacteriophage(game):
  game.config(6,6)
  pos = (2,2)
  game.set_mode(Game_Mode.BACTERIOPHAGE)
  game.set_spawn_other(pos)
  game.generate_other()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  bacteria_found = any(len(game._board.get_cell(x, y)._bacteriophages) > 0 for x, y in moves_n)
  assert bacteria_found


def test_refresh_board(game):
  game.config(6,6)
  game.set_mode(Game_Mode.ANTIBIOTIC)
  game.set_spawn_other((0,0))
  game.set_spawn_bacterium((2,2))
  assert game._frecuency == 0
  game.refresh_board()
  assert game._frecuency == 1
  game.refresh_board()
  assert game._frecuency == 0
