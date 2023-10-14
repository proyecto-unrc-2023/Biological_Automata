from behave import *
from models.logic.Bacterium import *
from models.logic.Antibiotic import Antibiotic
from models.logic.Bacteriophage import Bacteriophage

@given('una bacteria de {tipo} con {num:d} movimientos en ({pos_x:d},{pos_y:d})' )
def antes_reproduccion(context,tipo,num,pos_x,pos_y):
    if tipo == "bacteria normal":
      context.game._board.get_cell(pos_x,pos_y).add_bacterium(num,'b')
    
    elif tipo == "bacteria fuerte":
       context.game._board.get_cell(pos_x,pos_y).add_bacterium(num,'f')
    
    elif tipo == "bacteria debil":
       context.game._board.get_cell(pos_x,pos_y).add_bacterium(num,'d')

@then('deberia haber 2 bacterias en la celda ({pos_x:d},{pos_y:d})')
def checkeo_reproduccion(context,pos_x,pos_y): 
  assert context.game._board.get_cell(pos_x,pos_y).cant_bacteria() == 2

@then('deberia haber {num:d} bacteria fuerte en ({crash_x:d},{crash_y:d})')
def checkeo_de_bacteria_fuerte(context,num,crash_x,crash_y):
    assert isinstance(context.game._board.get_cell(crash_x,crash_y)._bacteria[0],BacteriumStrong)
