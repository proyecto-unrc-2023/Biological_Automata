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
    board = context.game._board
    context.new_board = context.game._board.move_all_entities(x, y, board)

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


# # ya se coloco el spawn de bacterias
# @given("se coloco el spawn de bacterias en ({x:d},{y:d})")
# def fijar_spawn_bacteria(context,x,y):
#     context.game.set_spawn_bacterium((x,y))

# # ya se coloco el spawn de la otra entidad
# @given("se coloco el spawn de la otra entidad en ({x:d},{y:d})")
# def fijar_spawn_other(context,x,y):
#     context.game.set_spawn_other((x,y))

# # se eligio el modo de juego 
# @given("el modo de juego elegido es {modo}")
# def setear_modo_de_juego(context,modo):
#     if (modo == "antibiotico"):
#         context.game._game_mode = Game_Mode.ANTIBIOTIC
#     if (modo == "bacteriofago"):
#         context.game._game_mode = Game_Mode.BACTERIOPHAGE


# @when("configura el juego con los siguientes parametros ({a:d},{b:d},{c:d},{d:d})") 
# def configurar_parametros(context,a,b,c,d):
#     context.game.config(a,b,c,d)

# @when("el usuario elige la posicion del spawn de bacterias en ({x:d},{y:d})")
# def colocar_spawn_bacteria(context,x,y):
#     context.game.set_spawn_bacterium((x,y))

# @when("el usuario elige la posicion del spawn de la otra entidad en ({x:d},{y:d})")
# def colocar_spawn_other(context,x,y):
#     context.game.set_spawn_other((x,y))

# @when("el usuario elige el modo de juego {modo}")
# def elegir_modo_de_juego(context, modo):
#     if (modo == "antibiotico"):
#         context.game._game_mode = Game_Mode.ANTIBIOTIC
#     if (modo == "bacteriofago"):
#         context.game._game_mode = Game_Mode.BACTERIOPHAGE
        
# @when("el usuario inicia el juego")
# def iniciar_juego(context):
#     context.game.start_game()

# @then("se deberia crear un tablero de {x:d}x{y:d}")
# def dimensiones_de_tablero(context,x,y):
#     assert context.game._board._rows == x
#     assert context.game._board._columns == y

# @then("la cantidad de bacterias de inicio es {c:d}")
# def chequear_bacterias_inicio(context,c):
#     assert context.game._cant_bacterium == c

# @then("la cantidad de la otra entidad de inicio es {c:d}")
# def chequear_otra_entidad_inicio(context,c):
#     assert context.game._cant_other == c

# @then("la frecuencia de bacterias es {c:d}")
# def chequear_frec_bacterias(context,c):
#     assert context.game._frecuency_bacterium == c

# @then("la frecuencia de la otra entidad es {c:d}")
# def chequear_frec_otra_entidad(context,c):
#     assert context.game._frecuency_other == c

# @then("el estado de juego deberia ser {estado}")
# def estado_de_juego(context,estado):
#     if estado == "CONFIG":
#         assert context.game._game_state == Game_State.CONFIG_GAME
#     if estado == "STARTED":
#         assert context.game._game_state == Game_State.START_GAME

# @then("deberia haber un spawn de bacterias en ({x:d},{y:d})")
# def chequear_pos_spawn_bac(context,x,y):
#     assert context.game._board.get_position_spawn_bacterium() == (x,y)

# @then("deberia haber un spawn de la otra entidad en ({x:d},{y:d})")
# def chequear_pos_spawn_other(context,x,y):
#     assert context.game._board.get_position_spawn_other() == (x,y)

# @then("el modo de juego deberia ser {modo}")
# def chequear_modo_de_juego(context, modo):
#     if (modo == "antibiotico"):
#         assert context.game._game_mode == Game_Mode.ANTIBIOTIC
#     if (modo == "bacteriofago"):
#         assert context.game._game_mode == Game_Mode.BACTERIOPHAGE




