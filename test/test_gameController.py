import pytest
from models.logic.GameController import GameController, Game_Mode

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
  game.set_spawn_antibiotic(pos)
  position = game._board.get_position_spawn_other()
  if position != None:
    assert position[0] == 2
    assert position[1] == 2
