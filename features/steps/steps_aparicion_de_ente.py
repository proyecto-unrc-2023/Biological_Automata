from behave import *
# from models.logic.Bacterium import Bacterium
# from models.logic.Bacteriophage import Bacteriophage

# se configuran los parametrso iniciales
@given('el usuario inicio el juego')
def juego_iniciado(context):
    context.game.start_game()

# se pasan cierta cantidad de turnos de juego
@when('ha pasado {turnos:d} turno de juego')
def pasar_turnos(context, turnos):
    for _ in range(turnos):
        context.game.refresh_board()

@then("deberian quedar {cant:d} {ente} por salir del spawn")
def chequeo_salida_spawn(context, ente, cant):
    if ente == "bacteria" or ente == "bacterias":
        assert context.game._cant_bacterium == cant
    else:
        assert context.game._cant_other == cant

@then("deberia haber {cant:d} {ente} en las celdas adyacentes a ({x:d},{y:d})")
def conteo_en_celdas_adyacentes(context, ente, cant, x, y):
    assert context.game.count_in_adjacents(x, y, ente) == cant
