from behave import *
from models.logic.GameController import Game_Mode, GameController, Game_State



# se crea un tablero para el juego
@given("el usuario ingreso al modo de juego de {x}")
def ingreso_al_modo_deseado(context,x):
    context.game.game_state = Game_State.CONFIG_GAME
    if x == "bacteriofagos":
        context.game.set_mode(Game_Mode.BACTERIOPHAGE)
    else:
        context.game.set_mode(Game_Mode.ANTIBIOTIC)

@when("se da inicio al juego")
def creo_tablero(context):
    pass

@then("se deberia crear un tablero de {x:d} x {y:d}")
def tablero_de_30x50(context,x,y):
    context.game.config(x,y)
    assert context.game._board._rows == x
    assert context.game._board._columns == y

@then("el modo de juego deberia ser {modo}")
def modo_de_juego(context,modo):
    if modo == "bacteriofagos":
        assert context.game.get_mode().__eq__(Game_Mode.BACTERIOPHAGE)
    else:
        assert context.game.get_mode().__eq__(Game_Mode.ANTIBIOTIC)



# se configuran los parametrso iniciales
@when('el usuario configura los parametros iniciales de {ac} con (({a:d},{b:d}),{c:d},{d:d})')
def completar_parametros(context,ac,a,b,c,d):
    if ac == "b":
        context.game.set_spawn_bacterium((a,b))
        context.game.set_cant_bacterium(c)
        context.game.set_frecuency_bacterium(d)
    else:
        context.game.set_spawn_other((a,b))
        if ac == "a":
            context.game.set_cant_antibiotic(c)
            context.game.set_frecuency_antibiotic(d)
        else:
            context.game.set_cant_bacteriophage(c)
            context.game.set_frecuency_bacteriophage(d)
    context.game.game_state = Game_State.START_GAME



@then('el tablero resultante tendra {c:d},{d:d}, para {ac} ({a:d},{b:d})')
def tablero_parametrizado(context,ac,a,b,c,d):
    if ac == "b":
        assert context.game._board.get_position_spawn_bacterium().__eq__((a,b))
        assert context.game._cant_bacterium == c
        assert context.game._frecuency_bacterium == d
    else:
        assert context.game._board.get_position_spawn_other().__eq__((a,b))
        if ac == "a":
            assert context.game._cant_antibiotic == c
            assert context.game._frecuency_antibiotic == d
        else:
            assert context.game._cant_bacteriophage == c
            assert context.game._frecuency_bacteriophage == d
    assert context.game.game_state == Game_State.START_GAME


