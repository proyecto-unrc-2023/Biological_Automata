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
  game.set_mode(Game_Mode.ANTIBIOTIC)
  game.generate_entities()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  bacteria_found = any(len(game._board.get_cell(x, y)._bacteria) > 0 for x, y in moves_n)
  assert bacteria_found

def test_spawn_other_antibiotic(game):
  game.config(6,6)
  pos = (2,2)
  game.set_mode(Game_Mode.ANTIBIOTIC)
  assert game.get_mode() == Game_Mode.ANTIBIOTIC
  game.set_spawn_other(pos)
  game.set_spawn_bacterium((5,5))
  game.generate_entities()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  bacteria_found = any(game._board.get_cell(x, y)._antibiotics > 0 for x, y in moves_n)
  assert bacteria_found


def test_spawn_bacteriophage(game):
  game.config(6,6)
  pos = (2,2)
  game.set_mode(Game_Mode.BACTERIOPHAGE)
  game.set_spawn_other(pos)
  game.generate_entities()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  bacteria_found = any(len(game._board.get_cell(x, y)._bacteriophages) > 0 for x, y in moves_n)
  assert bacteria_found


def test_refresh_board(game):
  game.config(6,6)
  game.set_mode(Game_Mode.ANTIBIOTIC)
  game.set_spawn_other((0,0))
  game.set_spawn_bacterium((2,2))
  cant_bacterium_prev = game._cant_bacterium
  cant_antibiotic_prev = game._cant_antibiotic
  game.refresh_board()
  assert game.get_mode() == Game_Mode.ANTIBIOTIC
  assert game._cant_bacterium == cant_bacterium_prev - 1
  assert game._cant_antibiotic == cant_antibiotic_prev - 1