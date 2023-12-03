from behave import *
from models.logic.Bacterium import *

@given("se configuro los parametros avanzados con ({a:d},{b:d},{c:d},{d:d},{e:d},{f:d},{g:f},{h:d})")
def configurar_parametros_avanzados(context, a, b, c, d, e, f, g, h):
    context.game.advanced_config(a,b,c,d,e,f,g,h)

@then("el tablero deberia quedar con {n:d} antibioticos con poder {power:d}")
def chequear_total_antibioticos_con_poder(context,n,power):
    assert context.game.count_total_antibiotics(power) == n 

@then("el tablero deberia quedar con {n:d} {ente}")
def chequear_total_entes(context,n,ente):
    assert context.game.count_total(ente) == n 
    

