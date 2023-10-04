from behave import *
from models.logic.Bacterium import *
from models.logic.Antibiotic import Antibiotic
from models.logic.Bacteriophage import Bacteriophage



@given('que hay {n:d} {ente} en la celda ({x:d},{y:d})')
def ubicacion_ente(context,n,x,y,ente):
    if ente == "antibiotico":
        for _ in range(0,n):
            context.game._board.add_antibiotic(x,y)
    elif ente == "bacteria normal":
        for _ in range(0,n):
            context.game._board.set_bacterium(x,y, BacteriumNormal(1))
    elif ente == "bacteria debil":
        for _ in range(0,n):
            context.game._board.set_bacterium(x,y, BacteriumWeak(1))
    elif ente == "bacteria fuerte":
        for _ in range(0,n):
            context.game._board.set_bacterium(x,y, BacteriumStrong(1))
    elif ente == "bacteria infectada":
        for _ in range(0,n):
            context.game._board.set_bacterium(x,y, BacteriumInfected(x))
    elif ente == "bacteriofago":
        for _ in range(0,n):
            context.game._board.set_bacteriophage(x,y, Bacteriophage(4))

@when('se mueve {n:d} {ente} de ({x1:d},{y1:d}) a ({x2:d},{y2:d})')
def movimiento_ente(context,n,x1,y1,x2,y2,ente):
    if ente == "antibiotico":
        tablero = context.game._board
        context.game.__board = context.game._board.move_entity(x2,y2,x1,y1,tablero,Antibiotic())
    elif ente == "bacteriofago":
        var = context.game._board.get_cell(x1,y1)._bacteriophage[0]
        tablero = context.game._board
        context.game.__board = context.game._board.move_entity(x2,y2,x1,y1,tablero,var)
    else:
        print(context.game._board.__str__())
        var = context.game._board.get_cell(x1,y1)._bacteria[0]
        tablero = context.game._board
        context.game.__board = context.game._board.move_entity(x2,y2,x1,y1,tablero,var)
    context.game._board.crossing_board()

    # for i in range(n):

@then('el tablero no deberia tener {ente} en ({x:d},{y:d})')
def eliminacion_ente(context,ente,x,y):
    if ente == "antibioticos":
        assert context.game._board.get_cell(x,y)._antibiotics == 0
    elif ente == "bacterias":
        assert context.game._board.get_cell(x,y)._bacteria.__len__() == 0
    elif ente == "bacteriofago":
        assert context.game._board.get_cell(x,y)._bacteriofago.__len__() == 0


#Esquema del escenario: Una bacteria fuerte se debilita al tener contacto con un antibiotico
@then('el tablero tiene {num} {ente} en ({crash_x:d},{crash_y:d})')
def checkeo_de_bacteria_debil(context,num,ente,crash_x,crash_y):
    assert isinstance(context.game._board.get_cell(crash_x,crash_y)._bacteria[0], BacteriumWeak)
