import pytest
from models.logic.GameController import GameController, Game_State, Game_Mode
from models.logic.Game_Mode import Game_Mode
from models.logic.Game_State import Game_State

@pytest.fixture

def game_antibiotic():
    game_controller = GameController(Game_Mode.ANTIBIOTIC,10, 2, 20, 2)
    game_controller.set_spawn_bacterium((0, 0))
    game_controller.set_spawn_other((3, 3))
    return game_controller


@pytest.fixture
def game_bacteriophage():
    game_controller = GameController(Game_Mode.BACTERIOPHAGE,10, 2, 20, 2)
    game_controller.set_spawn_bacterium((0, 0))
    game_controller.set_spawn_other((3, 3))
    return game_controller


def test_initial_game(game_antibiotic):
    game = game_antibiotic
    assert game._game_state == Game_State.CONFIG_GAME
    assert game._game_mode == Game_Mode.ANTIBIOTIC
    assert game.get_rows() == 12
    assert game.get_columns() == 17
    assert game._cant_bacterium == 10
    assert game._cant_other == 20
    assert game._frecuency_bacterium == 2
    assert game._frecuency_other == 2
    assert game._movements == 0


def test_invalid_game_mode():
    with pytest.raises(ValueError) as e:
        GameController("Modo de juego invalido")
    assert str(e.value) == "El modo de juego cargado no es válido!"

def test_negative_entity_counts():
    with pytest.raises(ValueError) as e:
        GameController(Game_Mode.ANTIBIOTIC, cant_bact=-5, cant_other=-10)
    assert str(e.value) == "La cantidad de los entes no pueden ser negativas!"

def test_zero_frequencies():
    with pytest.raises(ValueError) as e:
        GameController(Game_Mode.ANTIBIOTIC, frec_bact=0, frec_other=-2)
    assert str(e.value) == "Los valores de las frecuencias deben ser positivos!"

def set_spawn_bacterium_exception():
    game = GameController(Game_Mode.ANTIBIOTIC)
    game.start_game()
    with pytest.raises(ValueError) as e:
        game.set_spawn_bacterium((0, 0))
    assert str(e.value) == "El juego no está en el estado CONFIG_GAME"

def set_spawn_other_exception():
    game = GameController(Game_Mode.ANTIBIOTIC)
    game.start_game()
    with pytest.raises(ValueError) as e:
        game.set_spawn_other((3, 3))
    assert str(e.value) == "El juego no está en el estado CONFIG_GAME"

def test_start_state_is_not_NOT_CONFIG(game_bacteriophage):
    game = game_bacteriophage
    game.start_game()
    with pytest.raises(ValueError) as e:
        game.start_game()
    assert str(e.value) == "El juego no está en el estado CONFIG_GAME"


def test_game_mode(game_antibiotic):
    game = game_antibiotic
    game.start_game()
    assert game._game_mode == Game_Mode.ANTIBIOTIC
    assert game._game_state == Game_State.START_GAME

def test_init_cant_bacterium():
    with pytest.raises(ValueError) as e:
        game_controller = GameController(Game_Mode.BACTERIOPHAGE,-1, 2, 20, 2)
    assert str(e.value) == "La cantidad de los entes no pueden ser negativas!"

def test_init_frec_bacterium():
    with pytest.raises(ValueError) as e:
        game_controller = GameController(Game_Mode.BACTERIOPHAGE,1, -1, 20, 2)
    assert str(e.value) == "Los valores de las frecuencias deben ser positivos!"


def test_advanced_config(game_antibiotic):
    game = game_antibiotic
    game.advanced_config(3,3,3,3,3,3,1,3)
    assert game._max_power_other == 3
    assert game._moves_for_explotion == 3


def test_generate_bacterium_Mode_Antibiotic(game_antibiotic):
    game = game_antibiotic
    cant_bacterium_temp = game._cant_bacterium
    game.start_game()
    game.generate_bacterium()
    assert game._cant_bacterium == cant_bacterium_temp - 1


def test_generate_bacterium_Mode_Bacteriophage(game_bacteriophage):
    game = game_bacteriophage
    game._game_mode = Game_Mode.BACTERIOPHAGE
    cant_bacterium_temp = game._cant_bacterium
    game.start_game()
    game.generate_bacterium()
    assert game._cant_bacterium == cant_bacterium_temp - 1


def test_generate_bacterium_not_START_GAME(game_antibiotic):
    game = game_antibiotic
    with pytest.raises(ValueError) as e:
        game.generate_bacterium()
    assert str(e.value) == "El juego no está en el estado START_GAME"


def test_generate_other_Mode_Antibiotic(game_antibiotic):
    game = game_antibiotic
    cant_antibiotic_temp = game._cant_other
    game.start_game()
    game.generate_other()
    assert game._cant_other == cant_antibiotic_temp - 1


def test_generate_other_Mode_Bacteriophage(game_bacteriophage):
    game = game_bacteriophage
    cant_bacteriophage_temp = game._cant_other
    game.start_game()
    game.generate_other()
    assert game._cant_other == cant_bacteriophage_temp - 1


def test_generate_other_not_START_GAME(game_antibiotic):
    game = game_antibiotic
    with pytest.raises(ValueError) as e:
        game.generate_other()
    assert str(e.value) == "El juego no está en el estado START_GAME"


def test_generate_entities_Mode_Antibiotic(game_antibiotic):
    game = game_antibiotic
    cant_bacterium_temp = game._cant_bacterium
    cant_antibiotic_temp = game._cant_other
    game.start_game()
    game.generate_entities()
    assert game._cant_bacterium == cant_bacterium_temp - 1
    assert game._cant_other == cant_antibiotic_temp - 1


def test_generate_entities_Mode_Bacteriophage(game_bacteriophage):
    game = game_bacteriophage
    cant_bacterium_temp = game._cant_bacterium
    cant_bacteriophage_temp = game._cant_other
    game.start_game()
    game.generate_entities()
    assert game._cant_bacterium == cant_bacterium_temp - 1
    assert game._cant_other == cant_bacteriophage_temp - 1


def test_generate_entities_not_START_GAME(game_antibiotic):
    game = game_antibiotic
    with pytest.raises(ValueError) as e:
        game.generate_entities()
    assert str(e.value) == "El juego no está en el estado START_GAME"


def test_refresh_board(game_antibiotic):
    game = game_antibiotic
    cant_bacterium_temp = game._cant_bacterium
    cant_antibiotic_temp = game._cant_other
    cant_movements_temp = game._movements
    game.start_game()

    game.refresh_board()

    assert game._cant_bacterium == cant_bacterium_temp - 1
    assert game._cant_other == cant_antibiotic_temp - 1
    assert game._movements == cant_movements_temp + 1


def test_refresh_board_twice(game_antibiotic):
    game = game_antibiotic
    cant_bacterium_temp = game._cant_bacterium
    cant_antibiotic_temp = game._cant_other
    cant_movements_temp = game._movements
    game.start_game()
    game.refresh_board()
    game.refresh_board()
    assert game._cant_bacterium == cant_bacterium_temp - 1
    assert game._cant_other == cant_antibiotic_temp - 1
    assert game._movements == cant_movements_temp + 2


def test_refresh_board_not_START_GAME(game_antibiotic):
    game = game_antibiotic
    with pytest.raises(ValueError) as e:
        game.refresh_board()
    assert str(e.value) == "El juego no está en el estado START_GAME"


def test_stop_NOT_STARTED():
    game_controller = GameController(Game_Mode.ANTIBIOTIC,10, 2, 20, 2)
    with pytest.raises(ValueError) as e:
        game_controller.stop()
    assert str(e.value) == "El juego no está en el estado START_GAME"
    assert game_controller._game_state != Game_State.START_GAME


def test_stop_CONFIG_GAME(game_antibiotic):
    game = game_antibiotic
    with pytest.raises(ValueError) as e:
        game.stop()
    assert str(e.value) == "El juego no está en el estado START_GAME"
    assert game._game_state != Game_State.NOT_STARTED
    game.start_game()
    game.stop()
    assert game._game_state == Game_State.FINISHED


def test_set_spawn_bacterium(game_antibiotic):
    game = game_antibiotic
    assert game._game_mode == Game_Mode.ANTIBIOTIC
    position = game._board.get_position_spawn_bacterium()
    if position != None:
        assert position[0] == 0
        assert position[1] == 0

def test_set_spawn_other(game_antibiotic):
    game = game_antibiotic
    position = game._board.get_position_spawn_other()
    if position != None:
        assert position[0] == 3
        assert position[1] == 3


def test_spawn_bacterium(game_antibiotic):
    game = game_antibiotic
    pos = (0, 0)
    assert game._game_mode == Game_Mode.ANTIBIOTIC
    game.start_game()
    moves_n = game._board.get_possible_moves(pos[0], pos[1])
    bacteria_found = any(len(game._board.get_cell(
        x, y).get_bacteria()) > 0 for (x, y) in moves_n)
    assert not bacteria_found
    game.generate_entities()
    bacteria_found = any(len(game._board.get_cell(
        x, y).get_bacteria()) > 0 for (x, y) in moves_n)
    assert bacteria_found


def test_spawn_other_antibiotic(game_antibiotic):
    game = game_antibiotic
    pos = (3, 3)
    assert game._game_mode == Game_Mode.ANTIBIOTIC
    game.start_game()
    moves_n = game._board.get_possible_moves(pos[0], pos[1])
    antibiotic_found = any(game._board.get_cell(
        x, y).get_cant_antibiotic() > 0 for (x, y) in moves_n)
    assert not antibiotic_found
    game.generate_entities()
    antibiotic_found = any(game._board.get_cell(
        x, y).get_cant_antibiotic() > 0 for (x, y) in moves_n)
    assert antibiotic_found

def test_spawn_other(game_antibiotic):
    game = game_antibiotic
    pos = (4, 4)
    assert game._game_mode == Game_Mode.ANTIBIOTIC
    game.start_game()
    with pytest.raises(ValueError) as e:
        game.set_spawn_other(pos)
    assert str(e.value) == "El juego no está en el estado CONFIG_GAME"


def test_spawn_bacterium_error(game_bacteriophage):
    game = game_bacteriophage
    pos = (4, 4)
    assert game._game_mode == Game_Mode.BACTERIOPHAGE
    game.start_game()
    with pytest.raises(ValueError) as e:
        game.set_spawn_bacterium(pos)
    assert str(e.value) == "El juego no está en el estado CONFIG_GAME"


def test_spawn_bacteriophage(game_bacteriophage):
    game = game_bacteriophage
    pos = (3, 3)
    assert game._game_mode == Game_Mode.BACTERIOPHAGE
    game.start_game()
    moves_n = game._board.get_possible_moves(pos[0], pos[1])
    bacteriophage_found = any(len(game._board.get_cell(
        x, y).get_bacteriophages()) > 0 for (x, y) in moves_n)
    assert not bacteriophage_found
    game.generate_entities()
    bacteriophage_found = any(len(game._board.get_cell(
        x, y).get_bacteriophages()) > 0 for (x, y) in moves_n)
    assert bacteriophage_found


def test_count_in_adjacents_mode_antibiotic(game_antibiotic):
    game = game_antibiotic
    game.start_game()
    game.refresh_board()
    count = game.count_in_adjacents(0, 0, 'bacteria')
    assert count == 1
    count = game.count_in_adjacents(3, 3, 'antibiotico')
    assert count == 1


def test_count_in_adjacents_mode_bacteriophages(game_bacteriophage):
    game = game_bacteriophage
    game.start_game()
    game.refresh_board()
    count = game.count_in_adjacents(3, 3, 'bacteriofago')
    assert count == 1


def test_add_and_count_entities(game_antibiotic):
    game = game_antibiotic
    game.add_bacterium(0,0,0,"normal")
    game.add_bacterium(0,0,0,"debil")
    game.add_bacterium(0,0,0,"fuerte")
    game.add_antibiotic(0,0,3)
    assert game.count_bacteria_with_moves(0,0,"normal",0) == 1
    assert game.count_antibiotics(0,0,3) == 1

    #assert game.count_total_infected() == 1
    assert game.count_entities(0,0,"bacterias") == 3
    assert game.count_entities(0,0,"antibioticos") == 1
    assert game.count_entities(0,0,"bacteria normal") == 1
    assert game.count_entities(0,0,"bacteria fuerte") == 1
    assert game.count_entities(0,0,"bacteria debil") == 1


def test_move_entity(game_antibiotic):
    game = game_antibiotic
    game.add_entities(6,6,1,"bacteria normal")
    game.add_entities(6,6,1,"bacteria debil")
    game.add_entities(6,6,1,"bacteria fuerte")
    game.add_entities(6,6,2,"antibiotico")

    game.move_entity(6,6,7,7,"bacteria normal")
    game.move_entity(6,6,7,7,"bacteria debil")
    game.move_entity(6,6,7,7,"bacteria fuerte")

    assert game.count_entities(7,7,"bacterias") == 3
    assert game.count_entities(7,7,"bacteria normal") == 1
    assert game.count_entities(7,7,"bacteria fuerte") == 1
    assert game.count_entities(7,7,"bacteria debil") == 1


