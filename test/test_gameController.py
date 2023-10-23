import pytest
import time
from models.logic.GameController import *
from models.logic.Bacterium import *

@pytest.fixture
def game():
    game_controller = GameController()
    game_controller.config(10, 2, 20, 2)
    game_controller.set_spawn_bacterium((0,0))
    game_controller.set_spawn_other((3,3))
    return game_controller

def test_initial_game(game):
  game = GameController()
  assert game._game_state == Game_State.NOT_STARTER
  assert game._game_mode == None
  assert game._board == Board(30,50)
  assert game._cant_bacterium == 10
  assert game._cant_other == 20
  assert game._frecuency_bacterium == 2
  assert game._frecuency_other == 2
  assert game._movements == 0

def test_config_():
  game = GameController()
  game.config(10, 2, 20, 2)
  assert game._game_state == Game_State.CONFIG_GAME
  assert game._board == Board(30, 50)
  assert game._frecuency_bacterium == 2
  assert game._frecuency_other == 2
  assert game._cant_bacterium == 10
  assert game._cant_other == 20

def test_config_state_is_not_NOT_STARTER(game):
  game._game_mode = Game_Mode.BACTERIOPHAGE
  game.start_game()
  with pytest.raises(ValueError) as e:
    game.config(10, 2, 20, 2)
  assert str(e.value) == "El juego no está en el estado START_GAME"

def test_game_mode(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  game.start_game()
  assert game._game_mode == Game_Mode.ANTIBIOTIC
  assert game._game_state == Game_State.START_GAME

def test_game_mode_not_CONFIG_GAME(game):
  game = GameController()
  with pytest.raises(ValueError) as e:
    game.start_game()
  assert str(e.value) == "El juego no está en el estado CONFIG_GAME o no se configuró el modo de juego"

def test_game_mode_without_configuration():
  game = GameController()
  with pytest.raises(ValueError) as e:
    game._game_mode = Game_Mode.BACTERIOPHAGE
  assert str(e.value) == "El juego no está en el estado CONFIG_GAME o no se configuró uno de los spawn"
  assert game._game_mode == None
  assert game._game_state != Game_State.CONFIG_GAME

def test_game_mode_without_spawn_bacterium():
  game = GameController()
  game.config(10, 2, 20, 2)
  game.set_spawn_other((5,5))
  with pytest.raises(ValueError) as e:
    game._game_mode = Game_Mode.ANTIBIOTIC
  assert str(e.value) == "El juego no está en el estado CONFIG_GAME o no se configuró uno de los spawn"
  assert game._game_mode == None
  assert game._game_state == Game_State.CONFIG_GAME

def test_game_mode_without_spawn_other():
  game = GameController()
  game.config(10, 2, 20, 2)
  game.set_spawn_bacterium((5,5))
  with pytest.raises(ValueError) as e:
    game._game_mode = Game_Mode.BACTERIOPHAGE
  assert str(e.value) == "El juego no está en el estado CONFIG_GAME o no se configuró uno de los spawn"
  assert game._game_mode == None
  assert game._game_state == Game_State.CONFIG_GAME

def test_generate_bacterium_Mode_Antibiotic(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  cant_bacterium_temp = game._cant_bacterium
  game.start_game()
  game.generate_bacterium()
  assert game._cant_bacterium == cant_bacterium_temp - 1

def test_generate_bacterium_Mode_Bacteriophage(game):
  game._game_mode = Game_Mode.BACTERIOPHAGE
  cant_bacterium_temp = game._cant_bacterium
  game.start_game()
  game.generate_bacterium()
  assert game._cant_bacterium == cant_bacterium_temp - 1

def test_generate_bacterium_not_START_GAME(game):
  with pytest.raises(ValueError) as e:
    game.generate_bacterium()
  assert str(e.value) == "El juego no está en el estado START_GAME"

def test_generate_other_Mode_Antibiotic(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  cant_antibiotic_temp = game._cant_other
  game.start_game()
  game.generate_other()
  assert game._cant_other == cant_antibiotic_temp - 1

def test_generate_other_Mode_Bacteriophage(game):
  game._game_mode = Game_Mode.BACTERIOPHAGE
  cant_bacteriophage_temp = game._cant_other
  game.start_game()
  game.generate_other()
  assert game._cant_other == cant_bacteriophage_temp - 1

def test_generate_other_not_START_GAME(game):
  with pytest.raises(ValueError) as e:
    game.generate_other()
  assert str(e.value) == "El juego no está en el estado START_GAME"

def test_generate_entities_Mode_Antibiotic(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  cant_bacterium_temp = game._cant_bacterium
  cant_antibiotic_temp = game._cant_other
  game.start_game()
  game.generate_entities()
  assert game._cant_bacterium == cant_bacterium_temp - 1
  assert game._cant_other == cant_antibiotic_temp - 1

def test_generate_entities_Mode_Bacteriophage(game):
  game._game_mode = Game_Mode.BACTERIOPHAGE
  cant_bacterium_temp = game._cant_bacterium
  cant_bacteriophage_temp = game._cant_other
  game.start_game()
  game.generate_entities()
  assert game._cant_bacterium == cant_bacterium_temp - 1
  assert game._cant_other == cant_bacteriophage_temp - 1

def test_generate_entities_not_START_GAME(game):
  with pytest.raises(ValueError) as e:
    game.generate_entities()
  assert str(e.value) == "El juego no está en el estado START_GAME"

def test_refresh_board(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  cant_bacterium_temp = game._cant_bacterium
  cant_antibiotic_temp = game._cant_other
  cant_movements_temp = game._movements
  game.start_game()
  
  #incio = time.time()
  game.refresh_board()
  #fin = time.time()
  #assert print(fin-incio)

  assert game._cant_bacterium == cant_bacterium_temp - 1
  assert game._cant_other == cant_antibiotic_temp - 1
  assert game._movements == cant_movements_temp + 1

  

def test_refresh_board_twice(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  cant_bacterium_temp = game._cant_bacterium
  cant_antibiotic_temp = game._cant_other
  cant_movements_temp = game._movements
  game.start_game()
  game.refresh_board()
  game.refresh_board()
  assert game._cant_bacterium == cant_bacterium_temp - 1
  assert game._cant_other == cant_antibiotic_temp - 1
  assert game._movements == cant_movements_temp + 2

def test_refresh_board_not_START_GAME(game):
  with pytest.raises(ValueError) as e:
    game.refresh_board()
  assert str(e.value) == "El juego no está en el estado START_GAME"

def test_stop_NOT_STARTER():
  game = GameController()
  with pytest.raises(ValueError) as e:
    game.stop()
  assert str(e.value) == "El juego no está en el estado START_GAME"
  assert game._game_state != Game_State.NOT_STARTER   # Game_State.NOT_STARTER

def test_stop_CONFIG_GAME(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  with pytest.raises(ValueError) as e:
    game.stop()
  assert str(e.value) == "El juego no está en el estado START_GAME"
  assert game._game_state != Game_State.NOT_STARTER   # Game_State.NOT_STARTER
  game.start_game()
  game.stop()
  assert game._game_state == Game_State.NOT_STARTER

def test_set_spawn_bacterium(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  assert game._game_mode == Game_Mode.ANTIBIOTIC
  position = game._board.get_position_spawn_bacterium()
  if position != None:
    assert position[0] == 0
    assert position[1] == 0

def test_set_spawn_bacterium_not_CONFIG_GAME():
  game = GameController()
  position = (0,0)
  with pytest.raises(ValueError) as e:
    game.set_spawn_bacterium(position)
  assert str(e.value) == "El juego no está en el estado CONFIG_GAME"

def test_set_spawn_other(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  position = game._board.get_position_spawn_other()
  if position != None:
    assert position[0] == 3
    assert position[1] == 3

def test_set_spawn_other_not_CONFIG_GAME(game):
  game = GameController()
  position = (1,2)
  with pytest.raises(ValueError) as e:
    game.set_spawn_other(position)
  assert str(e.value) == "El juego no está en el estado CONFIG_GAME"

def test_spawn_bacterium(game):
  pos = (0,0)
  game._game_mode = Game_Mode.ANTIBIOTIC
  game.start_game()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  bacteria_found = any(len(game._board.get_cell(x, y)._bacteria) > 0 for (x, y) in moves_n)
  assert not bacteria_found
  game.generate_entities()
  bacteria_found = any(len(game._board.get_cell(x, y)._bacteria) > 0 for (x, y) in moves_n)
  assert bacteria_found

def test_spawn_other_antibiotic(game):
  pos = (3,3)
  game._game_mode = Game_Mode.ANTIBIOTIC
  game.start_game()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  antibiotic_found = any(game._board.get_cell(x, y)._antibiotics > 0 for (x, y) in moves_n)
  assert not antibiotic_found
  game.generate_entities()
  antibiotic_found = any(game._board.get_cell(x, y)._antibiotics > 0 for (x, y) in moves_n)
  assert antibiotic_found

def test_spawn_bacteriophage(game):
  pos = (3,3)
  game._game_mode = Game_Mode.BACTERIOPHAGE
  game.start_game()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  bacteriophage_found = any(len(game._board.get_cell(x, y)._bacteriophages) > 0 for (x, y) in moves_n)
  assert not bacteriophage_found
  game.generate_entities()
  bacteriophage_found = any(len(game._board.get_cell(x, y)._bacteriophages) > 0 for (x, y) in moves_n)
  assert bacteriophage_found

def test_count_in_adjacents_mode_antibiotic(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  game.start_game()
  game.refresh_board()
  count = game.count_in_adjacents(0,0, 'bacteria')
  assert count == 1
  count = game.count_in_adjacents(3,3, 'antibiotico')
  assert count == 1

def test_count_in_adjacents_mode_bacteriophages(game):
  game._game_mode = Game_Mode.BACTERIOPHAGE
  game.start_game()
  game.refresh_board()
  count = game.count_in_adjacents(3,3, 'v')
  assert count == 1
