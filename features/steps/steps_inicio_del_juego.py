from behave import *
from models.logic.GameController import GameController, Game_Mode
from models.logic.board import Board

# @given("que el usuario ingresa al juego")
# def inicio_el_juego(context):

@given("el usuario ingreso al modo de juego de {x}")
def ingreso_al_modo_deseado(context,x):
    context.game = GameController()
    if x == "bacteriofagos":
        context.game.set_mode(Game_Mode.BACTERIOPHAGE)
    else:
        context.game.set_mode(Game_Mode.ANTIBIOTIC)

@when("se crea un tablero de {x:d} x {y:d}")
def creo_tablero(context,x,y):
    context.game.config(x,y)

@then("el tablero es de {x:d} x {y:d}")
def tablero_de_6x6(context,x,y):
    assert context.game._board._rows == x
    assert context.game._board._columns == y

@then("el modo de juego es {modo}")
def modo_de_juego(context,modo):
    if modo == "bacteriofagos":
        assert context.game.get_mode().__eq__(Game_Mode.BACTERIOPHAGE)
    else:
        assert context.game.get_mode().__eq__(Game_Mode.ANTIBIOTIC)
        


@when('el usuario configura los parametros iniciales de {ac} con (({a:d},{b:d}),{c:d},{d:d})')
def completar_parametros(context,ac,a,b,c,d):
    if ac == "b":
        context.game.set_spawn_bacterium((a,b))
    else:
        context.game.set_spawn_other((a,b))
    context.game._reproduction_moves = d

@then('el tablero resultante tendra {c:d},{d:d}, para {ac} ({a:d},{b:d})')
def tablero_parametrizado(context,ac,a,b,c,d):
    if ac == "b":
        assert context.game._board.get_position_spawn_bacterium().__eq__((a,b))
    else:
        assert context.game._board.get_position_spawn_other().__eq__((a,b))
    assert context.game._reproduction_moves == d
    assert c == 2 or c == 4

