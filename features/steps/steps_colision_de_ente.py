from behave import *
from models.logic.Bacterium import *
from models.logic.Antibiotic import Antibiotic
from models.logic.Bacteriophage import Bacteriophage



@given('que hay {n:d} {ente} en la celda ({x:d},{y:d})')
def ubicacion_ente(context,n,x,y,ente):
    context.game.add_entities(x,y,n,ente)

@given('que hay {num:d} bacteriofago en la celda ({x:d},{y:d}) con poder de infeccion {poder:d}')
def agregar_bacteriofago(context, num, x, y, poder):
    for _ in range(num):
        context.game.add_bacteriophage(x,y,poder)

@given('que hay {num:d} bacteria infectada en la celda ({x:d},{y:d}) con grado de infeccion {grado:d}')
def agregar_bacteria_infectada(context, num, x, y, grado):
    for _ in range(num):
        context.game.add_infected(x,y,grado)

@when('se produce la confrontacion')
def crossing_table(context):
    context.game._board.crossing_board()

@then('el tablero no deberia tener {ente} en ({x:d},{y:d})')
def chequear_eliminacion_ente(context,ente,x,y):
    assert context.game.count_entities(x,y,ente) == 0
    
@then('el tablero deberia tener {num:d} {ente} en ({x:d},{y:d})')
def chequear_cantidad_entes(context,num,ente,x,y):
    assert context.game.count_entities(x,y,ente) == num

@then('deberia haber {num:d} bacteria infectada de grado {grado:d} en ({x:d},{y:d})')
def chequear_infectadas_en_celda(context,num, grado, x, y):
    assert context.game.count_infected(x,y,grado) == num

@then('deberia haber {num:d} bacteriofago con poder de infeccion {poder:d} en ({x:d},{y:d})')
def chequear_bacteriofagos(context,num, poder,x,y):
    assert context.game.count_bacteriophages(x,y,poder) == num


