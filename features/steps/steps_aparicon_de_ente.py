from behave import *
from models.logic.Bacterium import Bacterium
from models.logic.Bacteriophage import Bacteriophage



# aparicion de ente cerca de un spawn
@when("el usuario da inicio al juego, con un {e} en ({x:d},{y:d})")
def empieza_el_juego(context,e,x,y):
    if e == "b":
        context.game._board.get_cell(x,y).add_bacterium(1,"b")
    elif e == "a":
        context.game._board.get_cell(x,y).add_antibiotic()
    else:
        context.game._board.get_cell(x,y).add_bacteriophage(4)

@then("en la posicion ({x:d},{y:d}) aparece 1 {e}")
def se_produce_ente(context,x,y,e):
    if e == "bacteria":
        assert isinstance(context.game._board.get_cell(x,y)._bacteria[0],Bacterium)
        assert context.game._board.get_cell(x,y)._bacteria.__len__() == 1
    elif e == "antibiotico":
        assert context.game._board.get_cell(x,y)._antibiotics == 1
    else:
        assert isinstance(context.game._board.get_cell(x,y)._bacteriophages[0],Bacteriophage)
        assert context.game._board.get_cell(x,y)._bacteriophages.__len__() == 1
