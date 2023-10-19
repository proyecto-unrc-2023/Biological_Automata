from behave import *
from models.logic.board import Board
from models.logic.GameController import Game_Mode, GameController, Game_State


# se configuran los parametros iniciales del juego
@when("se obtienen los posibles movimientos desde la celda ({x:d},{y:d})") 
def movimientos_posibles(context,x,y):
    context.movimientos = context.game._board.get_possible_moves(x,y)

@then("tiene {n:d} posibles de movimiento")
def posibilidades_de_movimiento(context, n):
    assert len(context.movimientos) == n


@when("un {ente} se mueve desde la celda ({x:d},{y:d}) a una celda aleatoria")
def entity_se_mueve(context,x,y,ente):
    board = Board(30,50)
    context.new_board = context.game._board.move_entities(x, y, board)

@then("la celda ({x:d},{y:d}) del {ente} es contigua a la celda destino")
def celdas_contiguas(context,x,y,ente):
    occupied_cell = context.new_board.where_are_entities()
    cell = occupied_cell[0]
    a = cell[0]
    b = cell[1]
    assert len(occupied_cell) == 1
    assert context.new_board.how_many_entities(ente) == 1
    # calculo para determinar si son adyacentes las celdas de origen y destino
    assert (a - x)**2 + (b - y)**2 <= 2
