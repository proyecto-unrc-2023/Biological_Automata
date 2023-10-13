import pytest
from models.logic.GameController import *
from models.logic.Bacterium import *

@pytest.fixture
def game():
    game_controller = GameController()
    game_controller.config(10, 2, 20, 2)
    game_controller.set_spawn_bacterium((0,0))
    game_controller.set_spawn_other((2,2))
    return game_controller

def test_initial_game():
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

def test_game_mode(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  game.start_game()
  assert game._game_mode == Game_Mode.ANTIBIOTIC
  assert game._game_state == Game_State.START_GAME

def test_game_mode_without_configuration():
  game = GameController()
  game._game_mode = Game_Mode.BACTERIOPHAGE
  assert game._game_mode == None
  assert game._game_state != Game_State.CONFIG_GAME

def test_game_mode_without_spawn():
  game = GameController()
  game.config(10, 2, 20, 2)
  game._game_mode = Game_Mode.BACTERIOPHAGE
  assert game._game_mode == None
  assert game._game_state == Game_State.CONFIG_GAME

def test_generate_bacterium_Mode_Antibiotic(game):
  game._game_mode = Game_Mode.ANTIBIOTIC          # Para iniciar el juego
  cant_bacterium_temp = game._cant_bacterium
  game.start_game()
  game.generate_bacterium()
  assert game._cant_bacterium == cant_bacterium_temp - 1

def test_generate_bacterium_Mode_Bacteriophage(game):
  game._game_mode = Game_Mode.BACTERIOPHAGE       # Para iniciar el juego
  cant_bacterium_temp = game._cant_bacterium
  game.start_game()
  game.generate_bacterium()
  assert game._cant_bacterium == cant_bacterium_temp - 1

## ESTE VA FUNCIONAR SI EN el seteo de game_mode ponemos:
#if (self.__game_state == Game_State.CONFIG_GAME and spawn_bacterium != None or (spawn_other != None)):

# def test_generate_bacterium_without_spawn():
  # game = GameController()
  # game.config(10, 2, 20, 2)
  # game.set_spawn_other((5,5))
  # game._game_mode = Game_Mode.ANTIBIOTIC          # Para iniciar el juego
  # cant_bacterium_temp = game._cant_bacterium
  # game.start_game()
  # game.generate_bacterium()
  # assert game._cant_bacterium == cant_bacterium_temp

def test_generate_other_Mode_Antibiotic(game):
  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego
  cant_antibiotic_temp = game._cant_other
  game.start_game()
  game.generate_other()
  assert game._cant_other == cant_antibiotic_temp - 1

def test_generate_other_Mode_Bacteriophage(game):
  game._game_mode = Game_Mode.BACTERIOPHAGE       # Para iniciar el juego
  cant_bacteriophage_temp = game._cant_other
  game.start_game()
  game.generate_other()
  assert game._cant_other == cant_bacteriophage_temp - 1

#def test_generate_other_without_spawn_other():
#  game = GameController()
#  game.config(10, 2, 20, 2)
#  game.set_spawn_bacterium((5,5))
#  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego
#  cant_bacteriophage_temp = game._cant_other
#  game.start_game()
#  game.generate_other()
#  assert game._cant_other == cant_bacteriophage_temp

def test_generate_entities_Mode_Antibiotic(game):
  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego
  cant_bacterium_temp = game._cant_bacterium
  cant_antibiotic_temp = game._cant_other
  game.start_game()
  game.generate_entities()
  assert game._cant_bacterium == cant_bacterium_temp - 1
  assert game._cant_other == cant_antibiotic_temp - 1

def test_generate_entities_Mode_Bacteriophage(game):
  game._game_mode = Game_Mode.BACTERIOPHAGE       # Para iniciar el juego
  cant_bacterium_temp = game._cant_bacterium
  cant_bacteriophage_temp = game._cant_other
  game.start_game()
  game.generate_entities()
  assert game._cant_bacterium == cant_bacterium_temp - 1
  assert game._cant_other == cant_bacteriophage_temp - 1

#def test_generate_entities_without_spwan_other():
#  game = GameController()
#  game.config(10, 2, 20, 2)
#  game.set_spawn_bacterium((5,5))
#  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego
#  cant_bacterium_temp = game._cant_bacterium
#  cant_antibiotic_temp = game._cant_other
#  game.start_game()
#  game.generate_entities()
#  assert game._cant_bacterium == cant_bacterium_temp - 1
#  assert game._cant_other == cant_antibiotic_temp

def test_refresh_board(game):
  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego
  cant_bacterium_temp = game._cant_bacterium
  cant_antibiotic_temp = game._cant_other
  cant_movements_temp = game._movements
  game.start_game()
  game.refresh_board()
  assert game._cant_bacterium == cant_bacterium_temp - 1
  assert game._cant_other == cant_antibiotic_temp - 1
  assert game._movements == cant_movements_temp + 1

def test_refresh_board_twice(game):
  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego
  cant_bacterium_temp = game._cant_bacterium
  cant_antibiotic_temp = game._cant_other
  cant_movements_temp = game._movements
  game.start_game()
  game.refresh_board()
  game.refresh_board()
  assert game._cant_bacterium == cant_bacterium_temp - 1
  assert game._cant_other == cant_antibiotic_temp - 1
  assert game._movements == cant_movements_temp + 2

def test_stop_True(game):
  game._game_mode = Game_Mode.ANTIBIOTIC
  game.stop()
  assert game._game_state != Game_State.FINISH_GAME   # Game_State.NOT_STARTER
  game.stop()
  assert game._game_state != Game_State.FINISH_GAME   # Game_State.CONFIG_GAME
  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego, Game_State.START_GAME
  game.start_game()
  game.stop()
  assert game._game_state == Game_State.FINISH_GAME

def test_stop_False(game):
  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego
  game.stop()
  assert game._game_state != Game_State.FINISH_GAME

def test_set_spawn_bacterium(game):
  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego
  assert game._game_mode == Game_Mode.ANTIBIOTIC
  position = game._board.get_position_spawn_bacterium()
  if position != None:
    assert position[0] == 0
    assert position[1] == 0

def test_set_spawn_other(game):
  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego
  position = game._board.get_position_spawn_other()
  if position != None:
    assert position[0] == 2
    assert position[1] == 2

def test_spawn_bacterium(game):
  pos = (0,0)
  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego
  game.start_game()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  bacteria_found = any(len(game._board.get_cell(x, y)._bacteria) > 0 for (x, y) in moves_n)
  assert not bacteria_found
  game.generate_entities()
  bacteria_found = any(len(game._board.get_cell(x, y)._bacteria) > 0 for (x, y) in moves_n)
  assert bacteria_found

def test_spawn_other_antibiotic(game):
  pos = (2,2)
  game._game_mode = Game_Mode.ANTIBIOTIC       # Para iniciar el juego
  game.start_game()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  antibiotic_found = any(game._board.get_cell(x, y)._antibiotics > 0 for (x, y) in moves_n)
  assert not antibiotic_found
  game.generate_entities()
  antibiotic_found = any(game._board.get_cell(x, y)._antibiotics > 0 for (x, y) in moves_n)
  assert antibiotic_found



def test_spawn_bacteriophage(game):
  pos = (2,2)
  game._game_mode = Game_Mode.BACTERIOPHAGE       # Para iniciar el juego
  game.start_game()
  moves_n = game._board.get_possible_moves(pos[0],pos[1])
  bacteriophage_found = any(len(game._board.get_cell(x, y)._bacteriophages) > 0 for (x, y) in moves_n)
  assert not bacteriophage_found
  game.generate_entities()
  bacteriophage_found = any(len(game._board.get_cell(x, y)._bacteriophages) > 0 for (x, y) in moves_n)
  assert bacteriophage_found
