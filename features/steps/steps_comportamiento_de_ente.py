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



@given('hay 1 {type} en la celda ({x:d},{y:d}) con poder de infeccion {level:d}')
def entindad_infected(context,type,x,y,level):
    if type == "una bacteria infectada":
      context.game._board.get_cell(x,y).add_bacterium(level,'i')
    elif type == "un bacteriofago":
       context.game._board.get_cell(x,y).add_bacteriophage(level)

@when('{type} se mueve de ({x1:d},{y1:d}) a la celda ({x:d},{y:d})')
def varia_poder(context,x,y,x1,y1,type):
    if type == "una bacteria infectada":
        aux = context.game._board.get_cell(x1,y1)._bacteria[0]
        context.game._board.move_entity(x,y,x1,y1,aux)
    elif type == "un bacteriofago":
        aux = context.game._board.get_cell(x1,y1)._bacteriophages[0]
        context.game._board.move_entity(x,y,x1,y1,aux)
    
       
@then('el tablero deberia contener {type} en ({x:d},{y:d}) con {cualidad} de {level:d}')
def ente_in_pos(context,x,y,type,level):
    if type == "una bacteria infectada" :
        assert isinstance(context.game._board.get_cell(x,y)._bacteria[0],BacteriumInfected)
        assert context.game._board.get_cell(x,y)._bacteria[0].moves == level
    elif type == "un bacteriofago":
        assert isinstance(context.game._board.get_cell(x,y)._bacteriophages[0],Bacteriophage)
        assert context.game._board.get_cell(x,y)._bacteriophages[0]._infection == level
