# language: es

Característica: Comportamiento de las entidades
#10
  Esquema del escenario: Una bacteria normal o fuerte se reproduce
    Dado una bacteria de <tipo> con 3 movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces deberia haber 2 bacterias en la celda <pos>
    Ejemplos:

      |pos  |tipo           |
      |(1,2)|bacteria normal|
      |(5,3)|bacteria normal|
      |(5,3)|bacteria normal|
      |(1,2)|bacteria fuerte|
      |(5,0)|bacteria fuerte|
      |(2,1)|bacteria fuerte|



##11 NO VA LO DEJO POR LAS DUDAS

#  Escenario: La bacteria normal se reproduce con una mutación y produce una bacteria fuerte
#    Dado una bacteria con 3 movimientos en <pos>
#    Cuando se produce la confrontacion
#    #Preguntar esto, dificil de codear en el juego
#    Y por 1% de probabilidad sufre una mutacion
#    #Ver que pregunto aca también
#    Entonces el tablero deberia quedar con bacterias en (<end_x>,<end_y>) y en (<end2_x>,<end2_y>)
#
#    Ejemplos:
#      |pos  |
#      |(3,4)|
#      |(0,2)|
#      |(5,3)|
#
#      #|pos   |end   |end2  |
#      #|(3,4) |(4,4) |(4,5) |
#      #|(0,2) |(1,3) |(2,4) |
#      #|(5,3) |(4,3) |(4,2) |
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

#NOSE SI VA
##14 Ver escritura y ver que pasa con las variantes de tiempo para permane
#Escenario: Se produce sobrepoblacion de bacterias y sobrevive la más apta
#    Dado que hay 1 bacteria <tipo-s> en la celda (<pos_x>,<pos_y>)
#    Y 1 bacteria <tipo-p> en la celda (<pos1_x>,<pos1_y>)
#    Y 1 bacteria <tipo-p> en la celda (<pos2_x>,<pos2_y>)
#    Y 1 bacteria <tipo-p> en la celda (<pos3_x>,<pos3_y>)
#    Cuando se mueve 1 bacteria <tipo-s> de (<pos_x>,<pos_y>) a (<end_x>,<end_y>)
#    Y se mueve 1 bacteria <tipo-p> de (<pos1_x>,<pos1_y>) a (<end_x>,<end_y>)
#    Y se mueve 1 bacteria <tipo-p> de (<pos2_x>,<pos2_y>) a (<end_x>,<end_y>)
#    Y se mueve 1 bacteria <tipo-p> de (<pos3_x>,<pos3_y>) a (<end_x>,<end_y>)
#    Entonces el tablero tiene 1 bacteria <tipo-s> en (<end_x>,<end_y>)
#    Y el tablero no tiene bacterias <tipo-p>es en (<end_x>,<end_y>)
#
#    Ejemplos:
#      |pos_x|pos_y|pos1_x|pos1_y|pos2_x|pos2_y|pos3_x|pos3_y|end_x|end_y|tipo-s | tipo-p |
#      | 1   | 2   | 1    | 4    | 3    | 2    | 3    | 4    | 2   | 3   |fuerte |normales|
#      | 3   | 0   | 3    | 2    | 5    | 0    | 5    | 2    | 4   | 1   |fuerte |debiles |
#      | 2   | 1   | 2    | 3    | 4    | 1    | 4    | 3    | 3   | 2   |normal |debiles |
#      | 0   | 0   | 0    | 2    | 2    | 0    | 2    | 2    | 1   | 1   |normal |normales|
#      | 3   | 1   | 3    | 3    | 5    | 1    | 5    | 3    | 4   | 2   |debil  |debiles |
#
#      #|pos   |pos1  |pos2  |pos3  |end   |tipo-s | tipo-p |
#      #|(1,2) |(1,4) |(3,2) |(3,4) |(2,3) |fuerte |normales|
#      #|(3,0) |(3,2) |(5,0) |(5,2) |(4,1) |fuerte |debiles |
#      #|(2,1) |(2,3) |(4,1) |(4,3) |(3,2) |normal |debiles |
#      #|(0,0) |(0,2) |(2,0) |(2,2) |(1,1) |normal |normales|
#      #|(3,1) |(3,3) |(5,1) |(5,3) |(4,2) |debil  |debiles |
#
#15
  Esquema del escenario: Bacterias debiles se recuperan
    Dado una bacteria de <tipo> con 6 movimientos en <pos>
    Cuando se produce la confrontacion
    Entonces deberia haber 1 bacteria fuerte en <pos>

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
 Esquema del escenario: Varia la cualidad de infección en bacterias infectadas y bacteriofagos
   Dado  hay 1 <entidad> en la celda <pos> con poder de infeccion <grado-c>
   Cuando <entidad> se mueve de <pos> a la celda <end>
   Entonces el tablero deberia contener <entidad> en <end> con <cualidad> de <poder>
  #  Y deberia tener un <cualidad> de infeccion de <poder>]

   Ejemplos:
     |pos   |end   |grado-c|poder  |entidad               |cualidad|
     |(5,0) |(5,1) |1      |2      |una bacteria infectada|grado   |
     |(1,2) |(2,3) |2      |3      |una bacteria infectada|grado   |
     |(5,0) |(5,1) |4      |3      |un bacteriofago       |poder   |
     |(1,2) |(2,3) |3      |2      |un bacteriofago       |poder   |
     |(2,3) |(2,4) |2      |1      |un bacteriofago       |poder   |



# 19
  Esquema del escenario: Una bacteria infectada explota generando bacteriofagos
    Dado que hay 1 bacteria infectada en la celda <pos> con grado de infeccion <grado>
    Cuando se produce la confrontacion
    Entonces deberia haber 4 bacteriofago con poder de infección <poder> en <pos> 
    Ejemplos:
      |pos    |end    |poder  |grado|
      |(4,0)  |(4,1)  |4      |4    |
      |(2,0)  |(2,1)  |4      |4    |
      |(3,3)  |(3,4)  |4      |4    |

#  Comportamiento de bacteriofagos
#20
Esquema del escenario: Un bacteriofago desaparece tras cierto tiempo
    Dado hay 1 bacteriofago en la celda <pos> con poder de infeccion <poder>
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
