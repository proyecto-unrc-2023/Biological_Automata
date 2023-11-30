from behave import *
from models.logic.Game_Winner import Game_Winner

@given("ha pasado {cant:d} turno de juego")
def pasar_turnos(context, cant):
    for _ in range(cant):
        context.game.refresh_board()

@when("el usuario detiene el juego")
def detener_juego(context):
    context.game.stop()

@then("el ganador deberia ser {ente}")
def chequear_ganador(context, ente):
    if ente == "NO DETERMINADO":
        assert context.game._game_winner == Game_Winner.NOT_DETERMINATED
    if ente == "BACTERIA":
        assert context.game._game_winner == Game_Winner.BACTERIUM
    if ente == "ANTIBIOTICO" or ente == "BACTERIOFAGO":
        assert context.game._game_winner == Game_Winner.OTHER