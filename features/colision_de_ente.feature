# language: es

Característica: Colisión de entidades

# Bacterias y antibioticos
#9
  Esquema del escenario: Los antibioticos desaparecen al tener contacto con cualquier tipo de bacteria
    Dado que hay <num> antibiotico en la celda (<ax>,<ay>)
    Y que hay <num> <tipo> en la celda (<bx>,<by>)
    Cuando se mueve <num> antibiotico de (<ax>,<ay>) a (<ex>,<ey>)
    Y se mueve <num> <tipo> de (<bx>,<by>) a (<ex>,<ey>)
    Entonces el tablero no deberia tener antibioticos en (<ex>,<ey>)

    Ejemplos:
    | ax | ay | bx | by |tipo           | ex | ey |num|
    | 2  | 2  | 2  | 4  |bacteria debil | 2  | 3  | 1 |
    | 1  | 3  | 2  | 5  |bacteria normal| 1  | 4  | 1 |
    | 4  | 1  | 5  | 3  |bacteria fuerte| 4  | 2  | 1 |

# #10
#   Esquema del escenario: Una bacteria que no sea fuerte muere al encontrarse con un antibiótico
#     Dado que hay 1 antibiotico en la celda (<ax>,<ay>)
#     Y que hay 1 bacteria <tipo> en la celda (<bx>,<by>)
#     Cuando se mueve 1 antibiotico de (<ax>,<ay>) a (<cx>,<cy>)
#     Y se mueve 1 bacteria <tipo> de (<bx>,<by>) a (<cx>,<cy>)
#     Entonces el tablero no tiene antibioticos en (<cx>,<cy>)
#     Y el tablero no tiene bacterias en (<cx>,<cy>)

#     Ejemplos:
#     | ax | ay | bx | by |tipo  | cx | cy |
#     | 3  | 2  | 3  | 4  |debil | 3  | 3  |
#     | 1  | 3  | 2  | 4  |normal| 1  | 3  |


# # #11

#   Esquema del escenario: Una bacteria fuerte se debilita al tener contacto con un antibiotico
#     Dado que hay 1 antibiotico en la celda <apos>
#     Y que hay 1 bacteria fuerte en la celda <bpos>
#     Cuando se mueve 1 antibiotico de <apos> a <crash>
#     Y se mueve 1 bacteria de <bpos> a <crash>
#     Entonces el tablero no tiene antibioticos en <crash>
#     Y el tablero tiene 1 bacteria debil en <crash>

#     Ejemplos:
#     |apos   |bpos   |crash  |
#     |(3,2)  |(3,4)  |(3,3)  |
#     |(1,0)  |(2,2)  |(1,1)  |
#     |(3,3)  |(3,5)  |(3,4)  |
#     |(4,5)  |(5,5)  |(5,4)  |
#     |(0,2)  |(1,3)  |(0,3)  |
#     |(3,1)  |(4,2)  |(3,2)  |

# #12
   Esquema del escenario: Las bacterias mueren cuando hay mas antibioticos que bacterias en la misma celda
     Dado que hay 4 antibiotico en la celda <pos>
     Y que hay 1 bacteria normal en la celda <pos>
     Y que hay 1 bacteria debil en la celda <pos>
     Y que hay 1 bacteria fuerte en la celda <pos>
     Cuando se produce el confrontamiento
     Entonces el tablero no deberia tener antibioticos en <pos>
     Y el tablero no deberia tener bacterias en <pos>
     Ejemplos:
     |pos  |
     |(3,1)|
     |(2,3)|
     |(4,2)|



# Bacterias y bacteriófagos
#22
   Esquema del escenario: Una bacteria se cruza con un bacteriofago
     Dado que hay 1 <tipo> en la celda <bpos>
     Y hay 1 bacteriofago en la celda <bfpos> con poder de infeccion <poder>
     Cuando se mueve 1 <tipo> de <bpos> a <crash>
     Y se mueve 1 bacteriofago de <bfpos> a <crash>
     Cuando se produce el confrontamiento
     Entonces deberia haber 1 bacteria infectada de <grado> en <crash>
     Y el tablero no deberia tener bacteriofagos en <crash>

     Ejemplos:
     |bfpos  |bpos   |crash  |poder|grado|tipo           |
     |(3,2)  |(3,4)  |(3,3)  |4    |3    |bacteria normal|
     |(1,2)  |(2,4)  |(1,3)  |3    |2    |bacteria normal|
     |(0,0)  |(0,2)  |(0,1)  |2    |1    |bacteria normal|
     |(4,3)  |(5,3)  |(5,2)  |4    |3    |bacteria fuerte|
     |(2,4)  |(3,5)  |(2,5)  |3    |2    |bacteria fuerte|
     |(3,1)  |(5,1)  |(3,1)  |2    |1    |bacteria fuerte|


 #23
   Esquema del escenario: Una bacteria infectada no le ocurre nada cuando se cruza con un bacteriófago
     Dado que hay 1 bacteria infectada en la celda <pos> con grado de infeccion <grado>
     Y hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
     Cuando se produce el confrontamiento
     Entonces deberia haber 1 bacteria infectada de <grado> en <pos>
     Y deberia haber 1 bacteriofago con poder de infección <poder> en <pos>
     Ejemplos:
     |pos  |poder|grado|
     |(3,3)|4    |1    |
     |(1,1)|3    |2    |
     |(2,4)|2    |2    |
# #24
#   Esquema del escenario: Una bacteria es infectada por dos bacteriófagos
#     Dado que hay una bacteria <tipo> en la celda <bpos>
#     Y un bacteriofago en la celda <bfpos> con poder de infeccion <poder>
#     Y un bacteriofago en la celda <bfpos2> con poder de infeccion <poder2>
#     Cuando la bacteria y los bacteriofagos se mueven a la posición <crash>
#     Entonces el tablero deberia contener una bacteria infectada de grado <grado>

#     Ejemplos:
#     |bfpos  |bfpos2 |bpos   |crash  |poder|poder2|grado|tipo  |
#     |(3,2)  |(4,3)  |(3,4)  |(3,3)  |3    |2     |3    |normal|
#     |(1,5)  |(2,4)  |(2,5)  |(1,4)  |4    |1     |3    |fuerte|
#     |(1,3)  |(2,5)  |(2,4)  |(1,4)  |2    |2     |2    |normal|
#     |(3,3)  |(3,5)  |(4,4)  |(3,4)  |1    |2     |1    |fuerte|


# #25
#   Esquema del escenario: Sobrepoblación de bacterias se cruzan al mismo tiempo con un bacteriofago
#     Dado que hay una bacteria <tipo> en la celda <bpos>
#     Y hay una bacteria <tipo> en la celda <bpos2>
#     Y hay una bacteria <tipo> en la celda <bpos3>
#     Y hay una bacteria <tipo> en la celda <bpos4>
#     Y un bacteriofago en la celda <bfpos> con poder de infeccion <poder>
#     Cuando las bacteria y el bacteriofago se mueven a la posición <crash>
#     Entonces el tablero deberia contener una bacteria infectada de grado <grado>

#     Ejemplos:
#     |bfpos  |bpos  |bpos2  |bpos3 |bpos4  |crash  |poder|grado|tipo  |
#     |(3,2)  |(2,2) |(4,3)  |(2,4) |(3,4)  |(3,3)  |3    |2    |normal|
#     |(1,3)  |(0,3) |(2,4)  |(0,5) |(1,5)  |(1,4)  |2    |1    |fuerte|
#     |(4,0)  |(3,0) |(5,1)  |(3,2) |(4,2)  |(4,1)  |4    |3    |normal|

