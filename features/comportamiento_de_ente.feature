# language: es

Característica: Comportamiento de las entidades
#10
  Esquema del escenario: Una bacteria normal o fuerte se reproduce
    Dado una bacteria de <tipo> con 3 movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 2 bacterias en <pos>
    #deberia haber 2 bacterias en la celda <pos>
    Ejemplos:

      |pos  |tipo           |
      |(1,2)|bacteria normal|
      |(5,3)|bacteria normal|
      |(5,3)|bacteria normal|
      |(1,2)|bacteria fuerte|
      |(5,0)|bacteria fuerte|
      |(2,1)|bacteria fuerte|

##12
##13
 Esquema del escenario: Una bacteria debil no se reproduce
    Dado una bacteria de <tipo> con 5 movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 1 bacteria debil en <pos>
    Ejemplos:
      |pos  |tipo          |
      |(1,2)|bacteria debil|
      |(4,4)|bacteria debil|
      |(2,5)|bacteria debil|
      |(0,3)|bacteria debil|
      |(3,1)|bacteria debil|

#15
  Esquema del escenario: Bacterias debiles se recuperan
    Dado una bacteria de <tipo> con 6 movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces el tablero deberia tener 1 bacteria fuerte en <pos>

    Ejemplos:
      |pos   |tipo          |
      |(5,0) |bacteria debil|
      |(1,2) |bacteria debil|
      |(0,4) |bacteria debil|
      |(2,4) |bacteria debil|
      |(1,0) |bacteria debil|
      |(3,3) |bacteria debil|

#  Comportamiento de las bacterias en modo bacteriofago
# 18
 Esquema del escenario: El grado de infeccion aumenta con los movimientos
   Dado que hay 1 bacteria infectada en la celda <pos> con grado de infeccion <grado>
   Cuando se mueve 1 bacteria infectada de la celda <pos> a <end>
   Entonces deberia haber 1 bacteria infectada de grado <grado_act> en <end>

  #  Y deberia tener un <cualidad> de infeccion de <poder>]

   Ejemplos:
     |pos   |end   |grado  |grado_act|
     |(5,0) |(5,1) |1      |2        |
     |(1,2) |(2,3) |2      |3        |
     |(2,3) |(2,4) |3      |4        |


 Esquema del escenario: El poder de infeccion disminuye con los movimientos
   Dado que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
   Cuando se mueve 1 bacteriofago de la celda <pos> a <end>
   Entonces deberia haber 1 bacteriofago con poder de infeccion <poder_act> en <end> 


   Ejemplos:
     |pos   |end   |poder  |poder_act|
     |(5,0) |(5,1) |4      |3        |
     |(1,2) |(2,3) |2      |1        |
     |(5,0) |(5,1) |3      |2        |



# 19
  Esquema del escenario: Una bacteria infectada explota generando bacteriofagos
    Dado que hay 1 bacteria infectada en la celda <pos> con grado de infeccion <grado>
    Cuando se produce la confrontacion
    Entonces deberia haber 4 bacteriofago con poder de infeccion <poder> en <pos> 
    Ejemplos:
      |pos    |end    |poder  |grado|
      |(4,0)  |(4,1)  |4      |4    |
      |(2,0)  |(2,1)  |4      |4    |
      |(3,3)  |(3,4)  |4      |4    |

#  Comportamiento de bacteriofagos
#20
Esquema del escenario: Un bacteriofago desaparece tras cierto tiempo
    Dado que hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
    Cuando se produce la confrontacion
    Entonces el tablero no deberia tener bacteriofago en <pos>

    Ejemplos:
      |pos   |poder|
      |(5,0) |0    |
      |(1,2) |0    |
      |(3,0) |0    |
      |(2,4) |0    |
      |(0,3) |0    |
      |(1,1) |0    |
      |(1,0) |0    |
