# language: es

Característica: Comportamiento de las entidades
#10
  Esquema del escenario: Una bacteria normal o fuerte se reproduce
    Dado que hay 1 bacteria <tipo-s> con 3 movimientos en la celda <pos>
    Cuando se mueve 1 bacteria <tipo-s> de <pos> a <end>
    #Entonces el tablero deberia quedar con bacterias <type-p> en <end> y en <end2>
    #Alternativa
    Entonces el tablero en total tiene 2 bacterias

    Ejemplos:
      |pos   |end   |end2  |tipo-s | tipo-p |
      |(1,2) |(1,3) |(2,2) |normal |normales|
      |(5,3) |(5,4) |(4,5) |normal |normales|
      |(4,2) |(3,2) |(3,1) |normal |normales|
      |(1,2) |(1,3) |(2,2) |fuerte |fuertes |
      |(5,0) |(5,1) |(4,2) |fuerte |fuertes |
      |(2,1) |(1,1) |(1,0) |fuerte |fuertes |

#11
  Esquema del escenario: La bacteria normal se reproduce con una mutación y produce una bacteria fuerte
    Dado que hay 1 bacteria con 3 movimientos en la celda <pos>
    Cuando se mueve 1 bacteria de <pos> a <end>
    #Preguntar esto, dificil de codear en el juego
    Y por 1% de probabilidad sufre una mutacion
    #Ver que pregunto aca también
    Entonces el tablero deberia quedar con bacterias en <end> y en <end2>

    Ejemplos:
      |pos   |end   |end2  |
      |(3,4) |(4,4) |(4,5) |
      |(0,2) |(1,3) |(2,4) |
      |(5,3) |(4,3) |(4,2) |

#13
Esquema del escenario: Una bacteria debil no se reproduce
    Dado que hay 1 bacteria debil con 3 movimientos en la celda <pos>
    Cuando se mueve 1 bacteria debil de <pos> a <end>
    Entonces el tablero tiene 1 bacteria debil en <end>
    Y el tablero no tiene bacterias en <pos>

    Ejemplos:
      |pos   |end   |
      |(1,2) |(1,3) |
      |(4,4) |(4,5) |
      |(2,5) |(1,5) |
      |(0,3) |(1,4) |
      |(3,1) |(3,2) |


#14 Ver escritura y ver que pasa con las variantes de tiempo para permane
Esquema del escenario: Se produce sobrepoblacion de bacterias y sobrevive la más apta
    Dado que hay 1 bacteria <tipo-s> en la celda <pos>
    Y 1 bacterias <tipo-p> en la celda <pos1>
    Y 1 bacterias <tipo-p> en la celda <pos2>
    Y 1 bacterias <tipo-p> en la celda <pos3>
    Cuando se mueve 1 bacteria <tipo-s> de <pos> a <end>
    Y se mueve 1 bacteria <tipo-p> de <pos1> a <end>
    Y se mueve 1 bacteria <tipo-p> de <pos2> a <end>
    Y se mueve 1 bacteria <tipo-p> de <pos3> a <end>
    Entonces el tablero tiene 1 bacteria <tipo-s> en <end>
    Y el tablero no tiene bacterias <tipo-p>es en <end>

    Ejemplos:
      |pos   |pos1  |pos2  |pos3  |end   |tipo-s | tipo-p |
      |(1,2) |(1,4) |(3,2) |(3,4) |(2,3) |fuerte |normales|
      |(3,0) |(3,2) |(5,0) |(5,2) |(4,1) |fuerte |debiles |
      |(2,1) |(2,3) |(4,1) |(4,3) |(3,2) |normal |debiles |
      |(0,0) |(0,2) |(2,0) |(2,2) |(1,1) |normal |normales|
      |(3,1) |(3,3) |(5,1) |(5,3) |(4,2) |debil  |debiles |


#15
  Esquema del escenario: Bacterias se vuelven fuertes despues de un tiempo
    Dado que hay 1 bacteria debil con 5 movimientos en la celda <pos>
    Cuando se mueve 1 bacteria debil de <pos> a <end>
    Entonces el tablero tiene 1 bacteria fuerte en <end>

    Ejemplos:
      |pos   |end   |
      |(5,0) |(5,1) |
      |(1,2) |(2,3) |
      |(0,4) |(1,5) |
      |(2,4) |(3,5) |
      |(1,0) |(2,1) |
      |(3,3) |(4,4) |




#  Comportamiento de las bacterias en modo bacteriofago
#18
  Esquema del escenario: Varia la cualidad de infección de en los entes
    Dado que hay <entidad> en la posicion <pos>
    Y un <cualidad> de infeccion <grado-c>
    Cuando se mueve a la celda <end>
    Entonces el tablero deberia contener <entidad> en <end>
    Y deberia tener un <cualidad> de infeccion de <grado-p>

    Ejemplos:
      |pos   |end   |grado-c|grado-p|entidad               |cualidad|
      |(5,0) |(5,1) |1      |2      |una bacteria infectada|grado   |
      |(1,2) |(2,3) |2      |3      |una bacteria infectada|grado   |
      |(5,0) |(5,1) |4      |3      |un bacteriofago       |poder   |
      |(1,2) |(2,3) |3      |2      |un bacteriofago       |poder   |
      |(2,3) |(2,4) |2      |1      |un bacteriofago       |poder   |


#19
  Esquema del escenario: Una bacteria infectada explota generando bacteriofagos
    Dado que hay una bacteria infectada en la posicion <pos>
    Y la bacteria tiene grado de infeccion <grado-c>
    Cuando la bacteria se mueve a la celda <end>
    Entonces el tablero deberia contener 4 bacteriofagos en <f1>, <f2>, <f3> y <f4>
    Y los cuatro bacteriofagos deberian tener poder de infeccion <grado-p>

    Ejemplos:
      |pos    |end    |grado-c|grado-p|f1     |f2     |f3     |f4     |
      |(4,0)  |(4,1)  |3      |4      |(3,0)  |(3,2)  |(5,0)  |(5,2)  |
      |(2,0)  |(2,1)  |3      |4      |(1,0)  |(1,2)  |(3,0)  |(3,2)  |
      |(3,3)  |(3,4)  |3      |4      |(2,3)  |(2,5)  |(4,3)  |(4,5)  |


#  Comportamiento de bacteriofagos
#20
Esquema del escenario: Un bacteriofago desaparece tras cierto tiempo
    Dado que hay un bacteriofago en la posicion <pos>
    Y el bacteriofago tiene poder de infeccion 1
    Cuando el bacteriofago se mueva a la celda <end>
    Entonces el bacteriofago de saparece del tablero, dejando la celda <end> vacia

    Ejemplos:
      |pos   |end   |
      |(5,0) |(5,1) |
      |(1,2) |(2,3) |
      |(3,0) |(4,1) |
      |(2,4) |(3,5) |
      |(0,3) |(1,4) |
      |(1,1) |(2,2) |
      |(1,0) |(2,1) |

