from behave import *
from models.logic.Bacterium import Bacterium
from models.logic.Bacteriophage import Bacteriophage

# se configuran los parametrso iniciales
@given('el usuario configura los parametros iniciales de {ac} con (({a:d},{b:d}),{c:d},{d:d})')
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

# se pasan cierta cantidad de turnos de juego
@when('ha pasado {turnos:d} turno para la generacion de entidades')
def pasar_turnos(context, turnos):
    for _ in range(turnos):
        context.game.generate_entities()

@then("deberian quedar {cant:d} {ente} por salir del spawn")
def chequeo_salida_spawn(context, ente, cant):
    if ente == "b":
        assert context.game._cant_bacterium == cant
    elif ente == "a":
        assert context.game._cant_antibiotic == cant
    else: 
        assert context.game._cant_bacteriophage == cant

