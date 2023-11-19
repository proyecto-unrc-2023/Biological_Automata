from behave import *
from models.logic.GameController import Game_Mode, GameController, Game_State

# se abre el juego
@given("que el usuario abrio el juego")
def abrir_juego(context):
    context.game = GameController()

# se configuran los parametros iniciales del juego
@given("los parametros iniciales del juego son ({a:d},{b:d},{c:d},{d:d},{modo})")
def configurar_juego(context,a,b,c,d,modo):
    if (modo == "antibiotico"):
        context.game.config(a,b,c,d,Game_Mode.ANTIBIOTIC)
    if (modo == "bacteriofago"):
        context.game.config(a,b,c,d,Game_Mode.BACTERIOPHAGE)

# ya se coloco el spawn de bacterias
@given("se coloco el spawn de bacterias en ({x:d},{y:d})")
def fijar_spawn_bacteria(context,x,y):
    context.game.set_spawn_bacterium((x,y))

# ya se coloco el spawn de la otra entidad
@given("se coloco el spawn de la otra entidad en ({x:d},{y:d})")
def fijar_spawn_other(context,x,y):
    context.game.set_spawn_other((x,y))

@when("configura el juego con los siguientes parametros ({a:d},{b:d},{c:d},{d:d},{modo})") 
def configurar_parametros(context,a,b,c,d,modo):
    if (modo == "antibiotico"):
        context.game.config(a,b,c,d,Game_Mode.ANTIBIOTIC)
    if (modo == "bacteriofago"):
        context.game.config(a,b,c,d,Game_Mode.BACTERIOPHAGE)

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

@then("la cantidad de bacterias de inicio es {c:d}")
def chequear_bacterias_inicio(context,c):
    assert context.game._cant_bacterium == c

@then("la cantidad de la otra entidad de inicio es {c:d}")
def chequear_otra_entidad_inicio(context,c):
    assert context.game._cant_other == c

@then("la frecuencia de bacterias es {c:d}")
def chequear_frec_bacterias(context,c):
    assert context.game._frecuency_bacterium == c

@then("la frecuencia de la otra entidad es {c:d}")
def chequear_frec_otra_entidad(context,c):
    assert context.game._frecuency_other == c

@then("el estado de juego deberia ser {estado}")
def estado_de_juego(context,estado):
    if estado == "CONFIG":
        assert context.game._game_state == Game_State.CONFIG_GAME
    if estado == "STARTED":
        assert context.game._game_state == Game_State.START_GAME
    if estado == "FINISHED":
        assert context.game._game_state == Game_State.FINISHED

@then("deberia haber un spawn de bacterias en ({x:d},{y:d})")
def chequear_pos_spawn_bac(context,x,y):
    assert context.game._board.get_position_spawn_bacterium() == (x,y)

@then("deberia haber un spawn de la otra entidad en ({x:d},{y:d})")
def chequear_pos_spawn_other(context,x,y):
    assert context.game._board.get_position_spawn_other() == (x,y)

@then("el modo de juego deberia ser {modo}")
def chequear_modo_de_juego(context, modo):
    if (modo == "antibiotico"):
        assert context.game._game_mode == Game_Mode.ANTIBIOTIC
    if (modo == "bacteriofago"):
        assert context.game._game_mode == Game_Mode.BACTERIOPHAGE



