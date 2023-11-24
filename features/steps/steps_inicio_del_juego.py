from behave import *
from models.logic.GameController import Game_Mode, GameController, Game_State

# se abre el juego
@given("que el usuario abrio el juego")
def abrir_juego(context):
    pass

# se configuran los parametros iniciales del juego
@given("se creo el juego con los siguientes parametros ({a:d},{b:d},{c:d},{d:d},{modo})")
def configurar_juego(context,a,b,c,d,modo):
    if (modo == "antibiotico"):
        context.game = GameController(Game_Mode.ANTIBIOTIC,a,b,c,d)
    if (modo == "bacteriofago"):
        context.game =  GameController(Game_Mode.BACTERIOPHAGE,a,b,c,d)

@given("se coloco el spawn de {ente} en ({x:d},{y:d})")
def fijar_spawn(context,x,y,ente):
    if ente == "bacterias":
        context.game.set_spawn_bacterium((x,y))
    if ente == "antibiotico" or ente == "bacteriofago":
        context.game.set_spawn_other((x,y))

@when("se crea el juego con los siguientes parametros ({a:d},{b:d},{c:d},{d:d},{modo})") 
def configurar_parametros(context,a,b,c,d,modo):
    if (modo == "antibiotico"):
        context.game = GameController(Game_Mode.ANTIBIOTIC,a,b,c,d)
    if (modo == "bacteriofago"):
        context.game = GameController(Game_Mode.BACTERIOPHAGE,a,b,c,d)
        
@when("el usuario elige la posicion del spawn de bacterias en ({x:d},{y:d})")
def colocar_spawn_bacteria(context,x,y):
    context.game.set_spawn_bacterium((x,y))

@when("el usuario elige la posicion del spawn de la otra entidad en ({x:d},{y:d})")
def colocar_spawn_other(context,x,y):
    context.game.set_spawn_other((x,y))
        
@when("el usuario inicia el juego")
def iniciar_juego(context):
    context.game.start_game()

@then("se deberia crear un tablero de {x:d}x{y:d}")
def dimensiones_de_tablero(context,x,y):
    assert context.game.get_rows() == x
    assert context.game.get_columns() == y

@then("la cantidad de {ente} de inicio es {c:d}")
def chequear_entes_de_inicio(context, ente, c):
    if ente == "bacterias":
        assert context.game._cant_bacterium == c
    if ente == "antibiotico" or ente == "bacteriofago":
        assert context.game._cant_other == c

@then("la frecuencia de {ente} es {c:d}")
def chequear_frecuencia(context, ente, c):
    if ente == "bacteria":
        assert context.game._frecuency_bacterium == c
    if ente == "antibiotico" or ente == "bacteriofago":
        assert context.game._frecuency_other == c

@then("el estado de juego deberia ser {estado}")
def estado_de_juego(context,estado):
    if estado == "CONFIG":
        assert context.game._game_state == Game_State.CONFIG_GAME
    if estado == "STARTED":
        assert context.game._game_state == Game_State.START_GAME
    if estado == "FINISHED":
        assert context.game._game_state == Game_State.FINISHED

@then("deberia haber un spawn de {ente} en ({x:d},{y:d})")
def chequear_pos_spawn(context,x,y,ente):
    if ente == "bacterias":
        assert context.game._board.get_position_spawn_bacterium() == (x,y)
    if ente == "antibiotico" or ente == "bacteriofago":
        assert context.game._board.get_position_spawn_other() == (x,y)

@then("el modo de juego deberia ser {modo}")
def chequear_modo_de_juego(context, modo):
    if (modo == "antibiotico"):
        assert context.game._game_mode == Game_Mode.ANTIBIOTIC
    if (modo == "bacteriofago"):
        assert context.game._game_mode == Game_Mode.BACTERIOPHAGE