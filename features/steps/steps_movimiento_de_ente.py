from behave import *
from models.logic.board import Board
from models.logic.GameController import Game_Mode, GameController, Game_State

@given('que hay {cant:d} bacteria {tipo} con {num:d} movimientos en ({x:d},{y:d})' )
def agregar_bacterias_con_movimiento(context,cant,tipo,num,x,y):
    for _ in range (cant):
        context.game.add_bacterium(x,y,num,tipo)

@when('se mueve {n:d} {ente} de la celda ({x1:d},{y1:d}) a ({x2:d},{y2:d})')
def mover_ente(context,n,x1,y1,x2,y2, ente):
    for _ in range (n):
        context.game.move_entity(x1,y1,x2,y2,ente)  

@when("un {ente} se mueve desde la celda ({x:d},{y:d}) a una celda aleatoria")
def entity_se_mueve(context,x,y,ente):
    board = Board(context.game._game_mode,30,50,4)
    context.new_board = context.game._board.move_entities(x, y, board)

@then('deberia haber {num:d} bacteria {tipo} con {mov:d} movimientos en ({x:d},{y:d})')
def chequear_bacterias_con_mov(context,num, tipo, mov, x, y):
    assert context.game.count_bacteria_with_moves(x,y,tipo,mov) == num

