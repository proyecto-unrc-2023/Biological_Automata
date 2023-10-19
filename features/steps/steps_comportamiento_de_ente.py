from behave import *
from models.logic.Bacterium import *
from models.logic.Antibiotic import Antibiotic
from models.logic.Bacteriophage import Bacteriophage

@given('una bacteria de {tipo} con {num:d} movimientos en ({x:d},{y:d})' )
def agregar_bacterias_con_movimiento(context,tipo,num,x,y):
    context.game.add_bacterium(x,y,num,tipo)

@when('se mueve {n:d} {ente} de la celda ({x1:d},{y1:d}) a ({x2:d},{y2:d})')
def mover_ente(context,n,x1,y1,x2,y2, ente):
    for _ in range (n):
        context.game.move_entity(x1,y1,x2,y2,ente)    
       
