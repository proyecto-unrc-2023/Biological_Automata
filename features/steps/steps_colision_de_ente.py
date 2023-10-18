
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


@when('se produce la confrontacion')
def crossing_table(context):
    context.game._board.crossing_board()

@then('el tablero no deberia tener {ente} en ({x:d},{y:d})')
def eliminacion_ente(context,ente,x,y):
    if ente == "antibioticos":
        assert context.game._board.get_cell(x,y)._antibiotics == 0
    elif ente == "bacterias":
        assert context.game._board.get_cell(x,y)._bacteria.__len__() == 0
    elif ente == "bacteriofagos":
        assert context.game._board.get_cell(x,y)._bacteriophages.__len__() == 0

#El numero de antibioticos es menor o igual al numero de bacterias en una celda
#Una bacteria fuerte se debilita al tener contacto con un antibiotico
@then('el tablero deberia tener {num} {ente} en ({crash_x:d},{crash_y:d})')
def checkeo_de_bacteria_debil(context,num,ente,crash_x,crash_y):
    assert isinstance(context.game._board.get_cell(crash_x,crash_y)._bacteria[0], BacteriumWeak)


#Una bacteria se cruza con un bacteriofago
@given('hay {num:d} bacteriofago en la celda ({crash_x:d},{crash_y:d}) con poder de infeccion {poder:d}')
def ubicacion_bacteriophage(context, num, crash_x, crash_y, poder):
    for _ in range(0,num):
        context.game._board.set_bacteriophage(crash_x,crash_y, Bacteriophage(poder))
    
@then('deberia haber {num:d} bacteria infectada de {grado:d} en ({crash_x:d},{crash_y:d})')
def checkeo_de_bacteria_infectad(context,num , grado,crash_x,crash_y):
    assert isinstance(context.game._board.get_cell(crash_x,crash_y)._bacteria[0],BacteriumInfected)
    assert context.game._board.get_cell(crash_x,crash_y)._bacteria[0].moves == grado

#Esquema del escenario: Una bacteria infectada no le ocurre nada cuando se cruza con un bacteriófago
@given('que hay {num:d} bacteria infectada en la celda ({x:d},{y:d}) con grado de infeccion {grado:d}')
def agreago_bacteria_infectada(context, num, x, y, grado):
    for _ in range(0,num):
        context.game._board.set_bacterium(x,y, BacteriumInfected(grado))
        assert isinstance(context.game._board.get_cell(x,y)._bacteria[0], BacteriumInfected)


@then('deberia haber {num:d} bacteriofago con poder de infección {poder:d} en ({x:d},{y:d})')
def checkeo_bacteriofago(context,num, poder,x,y):
    for i in range(0,num):
        assert isinstance(context.game._board.get_cell(x,y)._bacteriophages[i], Bacteriophage)
        assert context.game._board.get_cell(x,y)._bacteriophages[i].infection == poder


@then('deberia haber {num:d} bacteriofago con poder de infeccion {poder:d} en ({x:d},{y:d})')
def burst_bacteriofago(context,num,poder,x,y):
    context.game._board.get_cell(x,y).burst_bacteriophage()
    assert context.game._board.get_cell(x,y)._bacteriophages[0].infection == poder
    assert context.game._board.get_cell(x,y)._bacteriophages[1].infection == poder
    assert context.game._board.get_cell(x,y)._bacteriophages[2].infection == poder
    