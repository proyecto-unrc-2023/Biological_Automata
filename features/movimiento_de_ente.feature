# language: es

Característica: Movimientos de una entidad

#1
  Esquema del escenario: Un ente tiene una cantidad de movimientos permitidos determinados por su posicion
    Dado que hay 1 <ente> en la celda <x>
    Cuando se obtienen los posibles movimientos desde la celda <x>
    Entonces tiene <n> posibles de movimiento
    # En un tablero de tamaño 30x50
    Ejemplos:
      |ente              |x      |n    |
      |antibiotico       |(0,0)  |3    |
      |bacteriofago      |(0,49) |3    |
      |bacteria normal   |(29,0) |3    |
      |bacteria debil    |(29,49)|3    |
      |bacteria fuerte   |(0,20) |5    |
      |bacteria infectada|(15,0) |5    |
      |antibiotico       |(29,25)|5    |
      |bacteriofago      |(15,49)|5    |
      |bacteria normal   |(10,20)|8    |

#2
  Esquema del escenario: Un ente se mueve de posicion a una celda contigua
    Dado que hay 1 <nombre> en la celda <x>
    Cuando un <ente> se mueve desde la celda <x> a una celda aleatoria
    Entonces la celda <x> del <ente> es contigua a la celda destino
    
    Ejemplos:
      |nombre            |x       |ente |
      |antibiotico       |(0,0)   |a    |
      |bacteriofago      |(15,0)  |v    |
      |bacteria normal   |(10,20) |b    |
      |bacteria debil    |(2,4)   |d    |
      |bacteria fuerte   |(10,20) |f    |
      |bacteria infectada|(15,0)  |i    |
    # Ejemplos:
    #   |ente         |a    |b    |c    |d    |e    |f    |g    |h    |x    |
    #   |bacterias    |(1,2)|(1,3)|(1,4)|(2,2)|(2,4)|(3,2)|(3,3)|(3,4)|(2,3)|
    #   |antibioticos |(1,2)|(1,3)|(1,4)|(2,2)|(2,4)|(3,2)|(3,3)|(3,4)|(2,3)|
    #   |bacteriofagos|(1,2)|(1,3)|(1,4)|(2,2)|(2,4)|(3,2)|(3,3)|(3,4)|(2,3)|

# #1
#   Esquema del escenario: Un ente se mueve de posicion a un casillero contiguo
#     Dado que hay 1 <ente> en la celda <x>
#     Y tiene 8 posibilidades de movimiento <a>, <b>, <c>, <d>, <e>, <f>, <g> y <h>
#     Cuando se mueve 1 <ente> de la celda <x> a <d>
#     Entonces el tablero tiene 1 <ente> en <d>
#     Y el tablero no tiene <ente>s en <x>

#     Ejemplos:
#       |ente         |a    |b    |c    |d    |e    |f    |g    |h    |x    |
#       |bacterias    |(1,2)|(1,3)|(1,4)|(2,2)|(2,4)|(3,2)|(3,3)|(3,4)|(2,3)|
#       |antibioticos |(1,2)|(1,3)|(1,4)|(2,2)|(2,4)|(3,2)|(3,3)|(3,4)|(2,3)|
#       |bacteriofagos|(1,2)|(1,3)|(1,4)|(2,2)|(2,4)|(3,2)|(3,3)|(3,4)|(2,3)|

# #2
#   Esquema del escenario: Un ente se mueve de algun borde a un casillero valido
#     Dado que hay 1 <ente> en la celda <x>
#     Y tiene 5 posibilidades de movimiento <a>, <b>, <c>, <d> y <e>
#     Cuando se mueve 1 <ente> de la celda <x> a <d>
#     Entonces el tablero tiene 1 <ente> en <d>
#     Y el tablero no tiene <ente>s en <x>

# # en caso de los bateriofagos, usaremos poder de infeccion dentro del test
#     Ejemplos:
#       |ente         |modo         |x    |a    |b    |c    |d    |e    |pwr|res|
#       |bacteria     |antibioticos |(1,4)|(1,5)|(1,3)|(2,5)|(2,3)|(2,4)|   |   |
#       |antibiotico  |antibioticos |(1,4)|(1,5)|(1,3)|(2,5)|(2,3)|(2,4)|   |   |
#       |bacteriofago |antibioticos |(1,4)|(1,5)|(1,3)|(2,5)|(2,3)|(2,4)|3  |2  |


# #3
#   Esquema del escenario: Un ente se mueve de una esquina a un casillero valido
#     Dado que hay 1 <ente> en la celda <a>
#     Y tiene 3 posibilidades de movimiento <b>, <c> y <d>
#     Cuando se mueve 1 <ente> de la celda <a> a <d>
#     Entonces el tablero tiene 1 <ente> en <d>
#     Y el tablero no tiene <ente>s en <a>

#     Ejemplos:
#       |ente         |a      |b      |c      |d      |
#       |bacterias    |(1,5)  |(2,4)  |(1,4)  |(2,5)  |
#       |bacterias    |(5,5)  |(5,4)  |(4,4)  |(4,5)  |
#       |bacterias    |(3,3)  |(3,4)  |(2,4)  |(2,3)  |
#       |bacterias    |(1,0)  |(1,1)  |(2,1)  |(2,0)  |
#       |antibioticos |(1,3)  |(2,2)  |(1,2)  |(2,3)  |
#       |antibioticos |(4,4)  |(4,3)  |(3,3)  |(3,4)  |
#       |antibioticos |(2,0)  |(2,1)  |(1,1)  |(1,0)  |
#       |antibioticos |(4,1)  |(4,2)  |(5,2)  |(5,1)  |
#       |bacteriofagos|(1,5)  |(2,4)  |(1,4)  |(2,5)  |
#       |bacteriofagos|(3,3)  |(3,2)  |(2,2)  |(2,3)  |
#       |bacteriofagos|(5,1)  |(0,2)  |(4,2)  |(4,1)  |
#       |bacteriofagos|(1,1)  |(1,2)  |(2,2)  |(2,1)  |

# #4
#   Esquema del escenario: Las entidades no interactuan entre si
#     Dado que hay 1 <ente> en la celda <a>
#     Y que hay 1 <ente> en la celda <b>
#     Y que hay 1 <ente> en la celda <c>
#     Cuando se mueve 1 <ente> de la celda <a> a <d>
#     Y se mueve 1 <ente> de la celda <b> a <d>
#     Y se mueve 1 <ente> de la celda <c> a <d>
#     Entonces el tablero tiene 3 <ente>s en <d>

#     Ejemplos:
#       |ente         |a    |b    |c    |d    |
#       |bacteria     |(3,1)|(3,3)|(4,2)|(3,2)|
#       |antibiotico  |(3,1)|(3,3)|(4,2)|(3,2)|
#       |bacteriofago |(3,1)|(3,3)|(4,2)|(3,2)|