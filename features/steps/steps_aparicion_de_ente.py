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
    if ente == "b":
        assert context.game._cant_bacterium == cant
    else:
        assert context.game._cant_other == cant

@then("deberia haber {cant:d} {ente} en las celdas adyacentes a ({x:d},{y:d})")
def conteo_en_celdas_adyacentes(context, ente, cant, x, y):
    vecinos = context.game._board.get_possible_moves(x,y)
    contador = 0
    for celda in vecinos:
        a = celda[0]
        b = celda[1]
        if ente == "b":
            contador += context.game._board.get_cell(a,b).cant_bacteria()
        if ente == "a":
            contador += context.game._board.get_cell(a,b)._antibiotics
        if ente == "v":
            contador += context.game._board.get_cell(a,b).cant_bacteriophages()

    assert contador == cant