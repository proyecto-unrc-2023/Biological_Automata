from behave import *
from models.logic.Bacterium import *
from models.logic.Antibiotic import Antibiotic
from models.logic.Bacteriophage import Bacteriophage

@then("el tablero deberia quedar con {n:d} {ente}")
def chequear_total_entes(context,n,ente):
    assert context.game.count_total(ente) == n 
       
